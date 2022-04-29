from dataclasses import dataclass
import numpy as np

from scipy import ndimage
from enum import Enum

from lens_simulation.Medium import Medium

# TODO:
# - grating


class LensType(Enum):
    Cylindrical = 1
    Spherical = 2


class Lens:
    def __init__(
        self, diameter: float, height: float, exponent: float, medium: Medium = Medium()
    ) -> None:

        self.diameter = diameter
        self.height = height
        self.exponent = exponent
        self.medium = medium
        self.escape_path = None
        self.profile = None

    def __repr__(self):

        return f""" Lens (diameter: {self.diameter:.2e}, height: {self.height:.2e}, \nexponent: {self.exponent:.3f}, refractive_index: {self.medium.refractive_index:.3f}),"""

    def generate_profile(self, pixel_size, lens_type: LensType = LensType.Cylindrical) -> np.ndarray:
        """[summary]

        Returns:
            np.ndarray: [description]
        """
        # TODO: someone might define using the n_pixels

        radius = self.diameter / 2
        n_pixels = int(radius / pixel_size) # n_pixels in radius
        # n_pixels must be odd (symmetry). 
        if n_pixels % 2 == 0:
            n_pixels += 1

        self.pixel_size = pixel_size
        self.n_pixels = n_pixels
        self.lens_type = lens_type

        if self.lens_type == LensType.Cylindrical:
        
            self.profile = self.create_profile_1d(radius, n_pixels)
        
        if self.lens_type == LensType.Spherical:

            self.profile = self.revolve_profile()

        return self.profile

    def create_profile_1d(self, radius, n_pixels):

        # x coordinate of pixels
        radius_px = np.linspace(0, radius, n_pixels)
        self.radius_px = radius_px

        # determine coefficent at boundary conditions
        # TODO: will be different for Hershel, Paraxial approximation)
        coefficient = self.height / (radius ** self.exponent)

        # generic lens formula
        # H = h - C*r ^ e
        heights = self.height - coefficient * radius_px ** self.exponent

        # generate symmetric height profile (NOTE: assumed symmetric lens).
        profile = np.append(np.flip(heights[1:]), heights)

        # always smooth
        profile = ndimage.gaussian_filter(profile, sigma=3)

        return profile


    def invert_profile(self):
        """Invert the lens profile"""
        if self.profile is None:
            raise RuntimeError(
                "This lens has no profile. Please generate the lens profile before inverting"
            )

        self.profile = abs(self.profile - np.max(self.profile))

        return self.profile

    def load_profile(self, arr: np.ndarray):
        """Load the lens profile from np array"""

        # assume lens diameter is sim width
        if arr.shape[-1] != self.n_pixels:
            raise ValueError(
                f"Custom lens profiles must match the simulation width. Custom Profile Shape: {arr.shape}, Simulation Pixels: {self.n_pixels}."
            )

        # TODO: we need pad the lens if the size is smaller than the sim n_pixels?

        self.profile = arr

        return self.profile

    def extrude_profile(self, length: float) -> np.ndarray:
        """Extrude the lens profile to create a cylindrical lens profile.
        
        args:
            length: (int) the length of the extruded lens (metres)
        
        """
        if self.profile is None:
            raise RuntimeError(
                "This lens has no profile. Please generate the lens profile before extruding"
            )

        # regenerate the profile
        self.generate_profile(self.pixel_size)

        # length in pixels
        length_px = int(length // self.pixel_size)

        # extrude profile
        self.profile = np.ones((length_px, *self.profile.shape)) * self.profile

        return self.profile

    def revolve_profile(self):
        """Revolve the lens profile around the centre of the lens"""

        # len/sim parameters
        lens_width = self.diameter 
        lens_length = self.diameter
        n_pixels_x = self.n_pixels * 2
        n_pixels_y = self.n_pixels * 2
                
        # revolve the profile around the centre (distance)
        x = np.linspace(0, lens_width, n_pixels_x)
        y = np.linspace(0, lens_length, n_pixels_y)
        X, Y = np.meshgrid(x, y)
        distance = np.sqrt(((lens_width / 2) - X) ** 2 + ((lens_length / 2) - Y) ** 2)

        # general profile formula...
        # coefficient is defined on the radius, not diameter

        coefficient = self.height / (lens_width/2) ** self.exponent
        profile = self.height - coefficient * distance ** self.exponent

        # clip the profile to zero
        profile = np.clip(profile, 0, np.max(profile))

        # override 1D profile
        self.profile = profile

        return self.profile

    """
    x: zero, equal
    M: max
    #####################
    #         x         #
    #                   #
    #                   #
    #x        M        x#
    #                   #
    #                   #
    #         x         #
    #####################

P

    """
