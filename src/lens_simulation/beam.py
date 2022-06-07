from dataclasses import dataclass, field
from multiprocessing.sharedctypes import Value
import matplotlib.pyplot as plt
import numpy as np
from pytest import param
from scipy import fftpack
from enum import Enum, auto

from lens_simulation.Medium import Medium 
from lens_simulation.Lens import Lens, LensType
from lens_simulation.structures import SimulationParameters

class BeamSpread(Enum):
    Plane = auto()
    Diverging = auto()
    Converging = auto()

class DistanceMode(Enum):
    Direct = auto()
    Width = auto()
    Focal = auto()

class BeamShape(Enum):
    Circular = auto()
    Square = auto()
    Rectangular = auto()

############
# Bsp/ DM:      Direct      Width       Focal   
# Plane:          Y                       N
# Converging:     Y                       Y
# Diverging:      Y                       Y


@dataclass
class BeamSettings:
    distance_mode: DistanceMode
    beam_spread: BeamSpread
    beam_shape: BeamShape
    width: float
    height: float
    position: list = field(default_factory=[0, 0])
    theta: float = 0.0                      # degrees
    numerical_aperture: float = None        
    tilt: list = None                       # degrees
    source_distance: float = None
    final_width: float = None
    focal_multiple: float = None
    n_slices: int = 10



class Beam:
    def __init__(self, settings: BeamSettings) -> None:

        # validate the beam configuration
        settings = validate_beam_configuration(settings)

        self.distance_mode: DistanceMode = settings.distance_mode
        self.spread: BeamSpread = settings.beam_spread
        self.shape: BeamShape = settings.beam_shape

        self.width: float = settings.width
        self.height: float  = settings.height
        self.position: list[float] = settings.position

        self.theta: float  = np.deg2rad(settings.theta) # degrees -> rad
        self.source_distance: float = settings.source_distance
        self.final_width: float = settings.final_width

        self.tilt: list[float] = settings.tilt

        self.output_medium = Medium(1.33)

        self.settings: BeamSettings = settings # TODO: remove?

    def __repr__(self) -> str:
        
        return f"""Beam: {self.settings}"""


    def generate_profile(self, sim_parameters: SimulationParameters) -> np.ndarray:

        pixel_size = sim_parameters.pixel_size
        sim_width = sim_parameters.sim_width
        sim_height = sim_parameters.sim_height
        lens_type = sim_parameters.lens_type

        # validation
        if self.width > sim_width:
            raise ValueError(f"Beam width is larger than simulation width: beam={self.width:.2e}m, sim={sim_width:.2e}m")
        if self.height > sim_width:
            raise ValueError(f"Beam height is larger than simulation width: beam={self.height:.2e}m, sim={sim_width:.2e}m")

        if self.position[0] > sim_width or self.position[1] > sim_width:
            raise ValueError(f"Beam position is outside simulation: position: x:{self.position[0]:.2e}m, y:{self.position[1]:.2e}m, sim_size: {sim_width:.2e}m")

        # Default beam specifications
        lens = Lens(
            diameter=max(self.width, self.height),
            height=100,                     # arbitrary non-zero
            exponent=2,                     # must be 2 for focusing
            medium=Medium(100)              # arbitrary non-zero
        )

        lens.generate_profile(pixel_size=pixel_size, lens_type=lens_type)

        # generate the lens profile
        if self.spread is BeamSpread.Plane:

            if self.shape is BeamShape.Circular:
                lens.profile = (lens.profile != 0) * 1 # removes corner areas from lens
            
            if self.shape is BeamShape.Square:
                lens.profile = np.ones(shape=lens.profile.shape)
            
            if self.shape is BeamShape.Rectangular:
                lens.profile = np.zeros(shape=lens.profile.shape)

                # make sure to fill out in the correct order, otherwise this creates a square        
                if self.height > self.width:
                    profile_width = int(self.width/pixel_size/2)   # half width
                    lens.profile[lens.profile.shape[0]//2-profile_width:lens.profile.shape[0]//2+profile_width, :] = 1
            
                elif self.width > self.height:
                    profile_height = int(self.height/pixel_size/2) # half height
                    lens.profile[:, lens.profile.shape[0]//2-profile_height:lens.profile.shape[0]//2+profile_height] = 1

        # diverging/converging cases
        elif self.spread in [BeamSpread.Converging, BeamSpread.Diverging]:
            # calculate the equivalent focal distance of the required convergence angle
            self.focal_distance = focal_distance_from_theta(beam=lens, theta=self.theta)
            
            # calculate and set the height of the apertures 'virtual' lens, re-generate the profile with new height
            lens.height = height_from_focal_distance(lens, output_medium=self.output_medium, focal_distance=self.focal_distance)

            # regenerate lens profile
            lens.generate_profile(pixel_size=pixel_size, lens_type=lens_type)

            if self.spread is BeamSpread.Diverging:
                lens.invert_profile()
                lens.profile = (lens.profile < lens.height) * lens.profile

        else:
            raise TypeError(f"Unsupport Beam Spread: {self.spread}")

        # set up the part of the lens square that isn't the lens for aperturing
        non_lens_profile = lens.profile == 0 
        aperturing_value = -1 #-1e-9 # NOTE: needs to be a relatively large value for numerical comparison # QUERY why not zero, parts of lens at zero might not be apertures e.g. escape path...
        lens.profile[non_lens_profile] = aperturing_value # the non-lens-profile is the size of the lens before padding...
        
        # calculate padding parameters
        beam_position = self.position
        pad_height = (int(sim_height/pixel_size)-lens.profile.shape[0])//2 + 1    # px
        pad_width = (int(sim_width/pixel_size)-lens.profile.shape[1])//2 + 1    # px
        relative_position_x = int(beam_position[1]/pixel_size)                  # px
        relative_position_y = int(beam_position[0]/pixel_size)                  # px
        # NOTE: ^ always symmetric

        # pad the profile to the sim width (Top - Bottom - Left - Right)
        lens.profile = np.pad(lens.profile, ((pad_height + relative_position_y, pad_height - relative_position_y),
                                                    (pad_width + relative_position_x, pad_width - relative_position_x)), 
                                                    mode="constant", constant_values=aperturing_value)
        # assign lens
        self.lens = lens
        self.lens.aperture = (lens.profile == aperturing_value)
        
        # reset apertures back to zero height
        self.lens.profile[self.lens.aperture]= 0

        # calculate propagation distance
        self.start_distance, self.finish_distance = self.calculate_propagation_distance()


    def calculate_propagation_distance(self):
        """Calculate the total distance to propagate the beam depending on configuration"""

        # distance_mode
        # beam_spread
        # source_distance
        # focal_distance
        # final_width
        # theta
        # lens

        start_distance = 0

        # If you just want the source to be a certain distance away:
        if self.distance_mode is DistanceMode.Direct or self.spread is BeamSpread.Plane:
            finish_distance = self.source_distance

        elif self.distance_mode is DistanceMode.Focal:
            finish_distance = self.focal_distance

        # if you want the beam to converge/diverge to a specific width
        elif self.distance_mode is DistanceMode.Width:
            final_beam_radius = self.final_width/2
            if self.spread is BeamSpread.Converging:
                finish_distance = self.focal_distance - (final_beam_radius/np.tan(self.theta+1e-12))
            else:
                finish_distance = ((final_beam_radius-(self.lens.diameter/2))/np.tan(self.theta+1e-12))
        else:
            raise TypeError(f"Unsupported DistanceMode for calculated propagation distance: {self.distance_mode}")

        return start_distance, finish_distance
    

def validate_beam_configuration(settings: BeamSettings):
    """Validate the user has passed the correct parameters for the given configuration"""
    # beam spread
    if settings.beam_spread is BeamSpread.Plane:

        if settings.source_distance is None:
            raise ValueError(f"A source_distance must be provided for {settings.beam_spread}")

        # plane wave is constant width along optical axis
        settings.final_width = settings.width
        print(f"The plane wave if constant along the optical axis. The beam final_width has been set to the initial width: {settings.width:.2e}m")

        if settings.distance_mode != DistanceMode.Direct:
            # plane waves only enabled for direct mode
            settings.distance_mode = DistanceMode.Direct
            print(f"Only DistanceMode.Direct is supported for BeamSpread.Plane. The distance_mode has been set to {settings.distance_mode}.")

    # can't do converging/divering square beams
    if settings.beam_spread in [BeamSpread.Converging, BeamSpread.Diverging]:
        settings.beam_shape = BeamShape.Circular
        print(f"Only BeamShape.Circular is supported for {settings.beam_spread}. The beam_shape has been set to {settings.beam_shape}.")

        # QUERY?
        if settings.theta == 0.0:
            raise ValueError(f"A non-zero theta must be provided for a {settings.beam_spread} beam.")

    # beam shape
    # non-rectangular beams are symmetric
    if settings.beam_shape in [BeamShape.Circular, BeamShape.Square]:
        settings.height = settings.width
        print(f"The beam_shape ({settings.beam_shape}) requires a symmetric beam. The beam height has been set to the beam width: {settings.width:.2e}m ")

    # distance mode
    if settings.distance_mode == DistanceMode.Direct:
        if settings.source_distance is None:
            raise ValueError(f"A source_distance must be provided for {settings.distance_mode}")

    if settings.distance_mode == DistanceMode.Focal:
        if settings.beam_spread not in [BeamSpread.Converging, BeamSpread.Diverging]:
            raise ValueError(f"BeamSpread must be Converging, or Diverging for {settings.distance_mode} (currently {settings.beam_spread})")

    if settings.distance_mode == DistanceMode.Width:
        if settings.final_width is None:
            raise ValueError(f"A final_width must be provided for {settings.distance_mode}")

    return settings

def theta_from_NA(numerical_aperture: float, output_medium: Medium):

    return np.arcsin(numerical_aperture/output_medium.refractive_index)

def focal_distance_from_theta(beam: Lens, theta: float):
    return beam.diameter/2 / np.tan(theta + 1e-12)

def height_from_focal_distance(beam: Lens, output_medium: Medium, focal_distance: float):
    a = 1
    b = -2*focal_distance*(beam.medium.refractive_index-output_medium.refractive_index)/output_medium.refractive_index
    c = (beam.diameter/2)**2

    if (b**2 - 4*a*c < 0):
        raise ValueError("Negative value encountered in sqrt.  Can't find a lens height to give this focal distance")
    else: return (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

def load_beam_config(config: dict) -> BeamSettings:
    """Load the beam settings from dictionary

    Args:
        config (dict): beam configuration as dictionary

    Returns:
        BeamSettings: beam configuration as BeamSettings
    """
    
    distance_mode = config["distance_mode"].title() if "distance_mode" in config else "Direct"
    beam_spread = config["beam_spread"].title() if "beam_spread" in config else "Plane"
    beam_shape = config["beam_shape"].title() if "beam_shape" in config else "Square"

    position = config["position"] if "position" in config else [0.0, 0.0]
    theta = config["theta"] if "theta" in config else 0.0
    numerical_aperture = config["numerical_aperture"] if "numerical_aperture" in config else None 
    tilt = config["tilt"] if "tilt" in config else [0.0, 0.0]
    source_distance = config["source_distance"] if "source_distance" in config else None
    final_width = config["final_width"] if "final_width" in config else None
    focal_multiple = config["focal_multiple"] if "focal_multiple" in config else None
    n_slices = config["n_slices"] if "n_slices" in config else 10

    beam_settings = BeamSettings(
        distance_mode=DistanceMode[distance_mode],
        beam_spread=BeamSpread[beam_spread], 
        beam_shape=BeamShape[beam_shape],
        width=config["width"],
        height= config["height"],
        position=position,
        theta=theta,
        numerical_aperture=numerical_aperture,
        tilt=tilt,
        source_distance=source_distance,
        final_width=final_width,
        focal_multiple=focal_multiple,
        n_slices=n_slices
    )

    return beam_settings

def generate_beam(config: dict, parameters: SimulationParameters):
    """Create a beam for simulation

    Args:
        config (dict): beam configuration
        parameters (SimulationParameters): global simulation parameters 

    Returns:
        Beam: initial simulation beam
    """
    # load beam settings
    beam_settings = load_beam_config(config)

    # create beam
    beam = Beam(settings=beam_settings)

    # generate profile
    beam.generate_profile(sim_parameters=parameters)

    return beam