import os
from pathlib import Path
import uuid

import petname
import numpy as np
import matplotlib.pyplot as plt

from pprint import pprint
from scipy import fftpack
from tqdm import tqdm

from lens_simulation import utils
from lens_simulation.Lens import Lens, LensType, GratingSettings
from lens_simulation.Medium import Medium
from lens_simulation.structures import (
    SimulationOptions,
    SimulationParameters,
    SimulationStage,
    SimulationResult,
)

# DONE:
# sweepable parameters
# database management
# visualisation, analytics, comparison
# initial beam definition (tilt, convergence, divergence)

# TODO:
# TODO: user interface
# TODO: tools (cleaning, sheet measurement, validation, lens creation)
# total internal reflection check (exponential profile)
# TODO: performance (cached results, gpu, parallelism)


class Simulation:
    def __init__(self, config: dict) -> None:

        self.sim_id = str(uuid.uuid4())
        self.petname = petname.Generate(2)
        self.read_configuration(config=config)
        self.setup_simulation()

    def read_configuration(self, config):

        # TODO: add a check to the config
        self.config = config
        self.config["sim_id"] = self.sim_id
        self.config["petname"] = self.petname
        self.mediums = config["mediums"]
        self.lenses = config["lenses"]
        self.stages = config["stages"]

        # TODO: change to petname? careful of collisions
        log_dir = os.path.join(self.config["log_dir"], str(self.petname))
        os.makedirs(log_dir, exist_ok=True)

        # options
        self.options = SimulationOptions(
            log_dir=log_dir,
            save=config["options"]["save"],
            save_plot=config["options"]["save_plot"],
            verbose=config["options"]["verbose"],
            debug=config["options"]["debug"],
        )

    def setup_simulation(self):

        # common sim parameters
        self.parameters = SimulationParameters(
            A=self.config["sim_parameters"]["A"],
            pixel_size=self.config["sim_parameters"]["pixel_size"],
            sim_width=self.config["sim_parameters"]["sim_width"],
            sim_height=self.config["sim_parameters"]["sim_height"], 
            sim_wavelength=self.config["sim_parameters"]["sim_wavelength"],
            lens_type=LensType[self.config["sim_parameters"]["lens_type"]],
        )

        # generate all mediums for simulation
        self.medium_dict = self.generate_mediums()

        # generate all lenses for the simulations
        self.lens_dict = self.generate_lenses()

        # generate all simulation stages
        self.generate_simulation_stages()

        # TODO: figure out how to implement this better
        # self.sim_run = SimulationRun(
        #     id = self.sim_id,
        #     petname = self.petname,
        #     parameters = self.parameters,
        #     config=self.config,
        #     options = self.options,
        #     stages = self.sim_stages
        # )

        # pprint(self.sim_run)

    def generate_simulation_stages(self):

        # validate all lens, mediums exist?
        for stage in self.stages:
            assert (
                stage["output"] in self.medium_dict
            ), f"{stage['output']} has not been defined in the configuration"
            assert (
                stage["lens"] in self.lens_dict
            ), f"{stage['lens']} has not been defined in the configuration"

            assert "n_slices" in stage, f"Stage requires n_slices"
            assert "start_distance" in stage, f"Stage requires start_distance"
            assert "finish_distance" in stage, f"Stage requires finish_distance"

        self.sim_stages = []

        # first stage is a beam
        from lens_simulation.beam import generate_beam

        beam = generate_beam(self.config["beam"], self.parameters)

        utils.plot_lens_profile_2D(beam.lens)
        plt.show()

        beam_stage = SimulationStage(
            lens=beam.lens,
            output=Medium(1.33),
            n_slices=10,
            start_distance=beam.start_distance,
            finish_distance=beam.finish_distance,
            tilt={"x": beam.tilt[0], "y": beam.tilt[1]},
        )

        # self.sim_stages.append(beam_stage) #TODO: START_HERE beam integration in sim

        # TODO: refactor this to incorporate the first beam stage

        for i, stage in enumerate(self.stages):

            sim_stage = SimulationStage(
                lens=self.lens_dict[stage["lens"]],
                output=self.medium_dict[stage["output"]],
                n_slices=stage["n_slices"],
                start_distance=stage["start_distance"],
                finish_distance=stage["finish_distance"],
                options=stage["options"],
                lens_inverted=False,
                _id=i,
            )

            # TODO: determine the best way to do double sided lenses (and define them in the config?)
            # TODO: should we separate double sided lens from inverting?
            if i != 0:

                # NOTE: if the lens and the output have the same medium, the lens is assumed to be 'double-sided'
                # therefore, we invert the lens profile to create an 'air lens' to properly simulate the double sided lens
                if (
                    sim_stage.lens.medium.refractive_index
                    == sim_stage.output.refractive_index
                ):  # TODO: figure out why dataclass comparison isnt working

                    # TODO: finish this
                    # def invert_lens_and_output_medium(stage: SimulationStage, previous_stage: SimulationStage, parameters: SimulationParameters) -> SimulationStage:
                    #     pass

                    # sim_stage = invert_lens_and_output_medium(sim_stage, self.sim_stages[i - 1], self.parameters)

                    if (
                        sim_stage.lens.medium.refractive_index
                        == self.sim_stages[i - 1].output.refractive_index
                    ):
                        raise ValueError(
                            "Lens and Medium on either side are the same Medium, Lens has no effect."
                        )  # TODO: might be useful for someone...

                    # change to 'air' lens, and invert the profile
                    sim_stage.lens = Lens(
                        diameter=sim_stage.lens.diameter,
                        height=sim_stage.lens.height,
                        exponent=sim_stage.lens.exponent,
                        medium=self.sim_stages[i - 1].output,
                    )  # replace the lens with lens of previous output medium

                    sim_stage.lens.generate_profile(
                        self.parameters.pixel_size, lens_type=self.parameters.lens_type
                    )
                    sim_stage.lens.invert_profile()
                    sim_stage.lens_inverted = True

            if sim_stage.options["use_equivalent_focal_distance"]:
                eq_fd = calculate_equivalent_focal_distance(
                    sim_stage.lens, sim_stage.output
                )

                sim_stage.start_distance = (
                    sim_stage.options["focal_distance_start_multiple"] * eq_fd
                )
                sim_stage.finish_distance = (
                    sim_stage.options["focal_distance_multiple"] * eq_fd
                )

                # update the metadata if this option is used...
                self.config["stages"][i]["start_distance"] = sim_stage.start_distance
                self.config["stages"][i]["finish_distance"] = sim_stage.finish_distance

            # update config
            self.config["stages"][i]["lens_inverted"] = sim_stage.lens_inverted

            self.sim_stages.append(sim_stage)

    def run_simulation(self):
        """Run the simulation propagation over all simulation stages."""

        passed_wavefront = None
        progress_bar = tqdm(self.sim_stages, leave=False)
        for stage in progress_bar:

            progress_bar.set_description(
                f"Sim: {self.petname} ({str(self.sim_id)[-10:]}) - Propagating Wavefront"
            )
            result = propagate_wavefront(
                stage=stage,
                parameters=self.parameters,
                options=self.options,
                passed_wavefront=passed_wavefront,
            )

            # save path
            save_path = os.path.join(self.options.log_dir, str(stage._id))

            if self.options.save:
                progress_bar.set_description(
                    f"Sim: {self.petname} ({str(self.sim_id)[-10:]}) - Saving Simulation"
                )
                utils.save_simulation(result.sim, os.path.join(save_path, "sim.npy"))

            if self.options.save_plot:
                progress_bar.set_description(
                    f"Sim: {self.petname} ({str(self.sim_id)[-10:]}) - Plotting Simulation"
                )

                save_result_plots(result, stage, self.parameters, save_path)

            # pass the wavefront to the next stage
            passed_wavefront = result.propagation

        utils.save_metadata(self.config, self.options.log_dir)

    def generate_mediums(self):
        """Generate all the mediums for the simulation"""

        medium_dict = {}
        for med in self.mediums:

            medium_dict[med["name"]] = Medium(med["refractive_index"])

        return medium_dict

    def generate_lenses(self):
        """Generate all the lenses for the simulation"""
        lens_dict = {}
        for lens_config in self.lenses:

            assert (
                lens_config["medium"] in self.medium_dict
            ), "Lens Medium not found in simulation mediums"

            lens = Lens(
                diameter=lens_config["diameter"],
                height=lens_config["height"],
                exponent=lens_config["exponent"],
                medium=self.medium_dict[lens_config["medium"]],
            )

            # check lens fits in the simulation
            if lens.diameter > self.parameters.sim_width:
                raise ValueError(
                    f"Lens diameter must be smaller than the simulation width: lens: {lens.diameter:.2e}, sim: {self.parameters.sim_width:.2e}"
                )

            # load a custom lens profile
            if lens_config["custom"]:
                lens.load_profile(fname=lens_config["custom"])

            # generate the profile from the configuration
            else:
                lens.generate_profile(
                    pixel_size=self.parameters.pixel_size,
                    lens_type=self.parameters.lens_type,
                )

                # TODO: do we want to be able to apply masks to custom profiles?
                if lens_config["grating"] is not None:
                    grating_settings = GratingSettings(
                        width=lens_config["grating"]["width"],
                        distance=lens_config["grating"]["distance"],
                        depth=lens_config["grating"]["depth"],
                        centred=lens_config["grating"]["centred"],
                    )
                    lens.calculate_grating_mask(
                        grating_settings,
                        x_axis=lens_config["grating"]["x"],
                        y_axis=lens_config["grating"]["y"],
                    )

                if lens_config["truncation"] is not None:
                    lens.calculate_truncation_mask(
                        truncation=lens_config["truncation"]["height"],
                        radius=lens_config["truncation"]["radius"],
                        type=lens_config["truncation"]["type"],
                    )

                if lens_config["aperture"] is not None:
                    lens.calculate_aperture(
                        inner_m=lens_config["aperture"]["inner"],
                        outer_m=lens_config["aperture"]["outer"],
                        type=lens_config["aperture"]["type"],
                        inverted=lens_config["aperture"]["invert"],
                    )

                # apply masks
                use_grating = True if lens_config["grating"] is not None else False
                use_truncation = (
                    True if lens_config["truncation"] is not None else False
                )
                use_aperture = True if lens_config["aperture"] is not None else False

                lens.apply_masks(
                    grating=use_grating,
                    truncation=use_truncation,
                    aperture=use_aperture,
                )

            lens_dict[lens_config["name"]] = lens

        return lens_dict


def propagate_wavefront(
    stage: SimulationStage,
    parameters: SimulationParameters,
    options: SimulationOptions,
    passed_wavefront: np.ndarray = None,
) -> SimulationResult:
    """Propagate the light wavefront using the supplied settings and parameters.

    Args:
        sim_stage (SimulationStage): the setup of the simulation stage, lens -> output
        parameters (SimulationParameters): the global simulation parameters (shared for all stages)
        options (SimulationOptions): global simulation options
        passed_wavefront (np.ndarray, optional): the previous wavefront to propagate from. Defaults to None.

    Raises:
        ValueError: lens is larger than the simulation width

    Returns:
        SimulationResult: results of the wave propagation (including intermediates if debugging)
    """

    lens = stage.lens
    output_medium = stage.output
    n_slices = stage.n_slices
    start_distance = stage.start_distance
    finish_distance = stage.finish_distance
    amplitude = parameters.A if passed_wavefront is None else 1.0

    DEBUG = options.debug
    save_path = os.path.join(options.log_dir, str(stage._id))

    # pad the lens profile to be the same size as the simulation
    sim_profile = pad_simulation(lens, parameters=parameters)

    # generate frequency array
    freq_arr = generate_sq_freq_arr(sim_profile, pixel_size=parameters.pixel_size)

    delta = calculate_tilted_delta_profile(sim_profile, lens, output_medium, stage.tilt)

    phase = calculate_phase_profile(delta=delta, wavelength=parameters.sim_wavelength)

    wavefront = calculate_wavefront(
        phase=phase,
        passed_wavefront=passed_wavefront,
        A=amplitude,
        aperture_mask=lens.aperture_mask_2,
    )

    # fourier transform of wavefront
    fft_wavefront = fftpack.fft2(wavefront)

    # pre-allocate view arrays
    sim = np.zeros(shape=(n_slices, *sim_profile.shape), dtype=np.float32)
    top_down_view = np.zeros(shape=(n_slices, sim_profile.shape[1]), dtype=np.float32)
    side_on_view = np.zeros(shape=(n_slices, sim_profile.shape[0]), dtype=np.float32)

    # propagate the wavefront over distance
    distances = np.linspace(start_distance, finish_distance, n_slices)

    prop_progress_bar = tqdm(distances, leave=False)
    for i, distance in enumerate(prop_progress_bar):
        prop_progress_bar.set_description(
            f"Propagating Wavefront at Distance {distance:.4f} / {distances[-1]:.4f}m"
        )

        rounded_output, propagation = propagate_over_distance(
            fft_wavefront, distance, freq_arr, output_medium.wave_number
        )

        if options.save:
            # save output
            utils.save_simulation(
                rounded_output,
                fname=os.path.join(save_path, f"{distance*1000:.8f}mm.npy"),
            )

        # calculate views
        centre_px_h = rounded_output.shape[0] // 2
        centre_px_v = rounded_output.shape[1] // 2
        top_down_slice = rounded_output[centre_px_h, :]
        side_on_slice = rounded_output[:, centre_px_v]

        # append views
        top_down_view[i, :] = top_down_slice
        side_on_view[i, :] = side_on_slice
        sim[i, :, :] = rounded_output


    # return results (TODO: reduce in non-debug mode)
    result = SimulationResult(
        propagation=propagation,
        top_down=top_down_view,
        side_on=side_on_view,
        sim=sim,
        sim_profile=sim_profile,
        lens=lens,
        freq_arr=freq_arr,
        delta=delta,
        phase=phase,
    )


    return result


def generate_squared_frequency_array(n_pixels: int, pixel_size: float) -> np.ndarray:
    """Generates the squared frequency array used in the fresnel diffraction integral

    Parameters
    ----------
    n_pixels : int
        number of pixels in the lens array
    pixel_size : float
        realspace size of each pixel in the lens array

    Returns
    -------
    np.ndarray
        squared frequency array
    """
    return np.power(fftpack.fftfreq(n_pixels, pixel_size), 2)


def generate_sq_freq_arr(sim_profile: np.ndarray, pixel_size: float) -> np.ndarray:
    """Generate the squared frequency array for the simulation"""

    if sim_profile.ndim != 2:
        raise TypeError(
            f"Only 2D Simulation Profile is supported. Simulation profile of shape {sim_profile.shape} not supported."
        )

    x = generate_squared_frequency_array(sim_profile.shape[1], pixel_size)
    y = generate_squared_frequency_array(sim_profile.shape[0], pixel_size)
    X, Y = np.meshgrid(x, y)
    freq_arr = X + Y

    return freq_arr.astype(np.float32)


def calculate_equivalent_focal_distance(lens: Lens, medium: Medium) -> float:
    """Calculates the focal distance of a lens with any exponent as if it had
    an exponent of 2.0 (assuming plano-concave focusing lens)

    Parameters
    ----------
    lens : Lens
        Lens instance as defined in Lens.py
    medium : Medium
        Medium instance as defined in Lens.py

    Returns
    -------
    float
        returns the calculated focal distance
    """
    equivalent_radius_of_curvature = 0.5 * (
        lens.height + (lens.diameter / 2) ** 2 / lens.height
    )
    equivalent_focal_distance = (
        equivalent_radius_of_curvature * medium.refractive_index
    ) / (lens.medium.refractive_index - medium.refractive_index)

    return equivalent_focal_distance


def pad_simulation(lens: Lens, parameters: SimulationParameters) -> np.ndarray:
    """Pad the lens profile to match the simulation dimensions. Padding is used to 
        prevent reflection in the simulation

    Args:
        lens (Lens): simulation lens
        parameters (SimulationParameters): simulation parameters

    Raises:
        TypeError: Lens profile is the wrong shape. Only 2D lens are supported.

    Returns:
        np.ndarray: padded lens profile
    """
    if lens.profile.ndim != 2:
        raise TypeError(
            f"Padding is only supported for 2D lens. Lens shape was: {lens.profile.shape}."
        )

    # calculate the number of pixels in the simulation
    sim_n_pixels_height = utils._calculate_num_of_pixels(parameters.sim_height, parameters.pixel_size)
    sim_n_pixels_width = utils._calculate_num_of_pixels(parameters.sim_width, parameters.pixel_size)

    # calculate different in size
    diff_h = (sim_n_pixels_height - lens.profile.shape[0]) // 2
    diff_w = (sim_n_pixels_width - lens.profile.shape[1]) // 2

    # pad the lens profile
    lens.profile = np.pad(lens.profile, pad_width=((diff_h, diff_h), (diff_w, diff_w)), mode="constant")
   
    return lens.profile

# def _pad_lens_profile_to_sim_dimensions(lens: Lens, width: float, height: float, pixel_size: float) -> Lens:
#     """Pad the lens profile to match the specified simulation dimensions

#     Args:
#         lens (Lens): Lens
#         width (float): simulation width
#         height (float): simulation height
#         pixel_size (float): _description_

#     Returns:
#         Lens: _description_
#     """



#     return lens


def calculate_delta_profile(
    sim_profile: np.ndarray, lens: Lens, output_medium: Medium
) -> np.ndarray:
    """Calculate the delta profile of the wave"""
    delta = (
        lens.medium.refractive_index - output_medium.refractive_index
    ) * sim_profile

    return delta


def calculate_tilted_delta_profile(
    sim_profile: np.ndarray, lens: Lens, output_medium: Medium, tilt: dict = None
) -> np.ndarray:
    """Calculate the delta profile of the wave, and tilt if required.

    Args:
        lens (Lens): lens
        output_medium (Medium): output medium
        tilt: (dict): dictionary containing the titlt values

    Returns:
        np.ndarray: delta profile
    """

    # regular delta calculation
    delta = calculate_delta_profile(sim_profile, lens, output_medium)

    # tilt the beam
    if tilt is not None:
        x = np.arange(len(sim_profile)) * lens.pixel_size
        y = np.arange(len(sim_profile)) * lens.pixel_size

        y_tilt_rad = np.deg2rad(tilt["y"])
        x_tilt_rad = np.deg2rad(tilt["x"])

        # modify the optical path of the light based on tilt
        delta = delta + np.add.outer(y * np.tan(y_tilt_rad), -x * np.tan(x_tilt_rad))

    return delta


def calculate_phase_profile(delta: np.ndarray, wavelength: float) -> np.ndarray:
    """Calculate the phase profile of the wave"""
    phase = 2 * np.pi * delta / wavelength  # % (2 * np.pi)

    return phase


def calculate_wavefront(
    phase: np.ndarray,
    passed_wavefront: np.ndarray,
    A: float,
    aperture_mask: np.ndarray = None,
) -> np.ndarray:
    """Calculate the wavefront of light"""

    # only amplifiy the first stage propagation
    if passed_wavefront is not None:
        assert A == 1, "Amplitude should be 1.0. Only amplify the first stage."
        wavefront = A * np.exp(1j * phase) * passed_wavefront
    else:
        wavefront = A * np.exp(1j * phase)

    # padded area should be 0+0j
    if passed_wavefront is not None:
        wavefront[phase == 0] = 0 + 0j

    # mask out apertured area
    if aperture_mask is not None:
        wavefront[aperture_mask] = 0 + 0j

    return wavefront


def propagate_over_distance(
    fft_wavefront, distance, freq_arr, wave_number
) -> np.ndarray:
    prop = np.exp(1j * wave_number * distance) * np.exp(
        (-1j * 2 * np.pi ** 2 * distance * freq_arr) / wave_number
    )
    propagation = fftpack.ifft2(prop * fft_wavefront)

    output = np.sqrt(propagation.real ** 2 + propagation.imag ** 2) ** 2

    rounded_output = np.round(output.astype(np.float32), 10)

    return rounded_output, propagation


def save_result_plots(
    result: SimulationResult,
    stage: SimulationStage,
    parameters: SimulationParameters,
    save_path: Path,
):
    """Plot and save the simulation results

    Args:
        result (SimulationResult): _description_
        stage (SimulationStage): _description_
        parameters (SimulationParameters): _description_
        save_path (Path): _description_
    """

    # save top-down
    fig = utils.plot_simulation(
        arr=result.top_down,
        pixel_size_x=parameters.pixel_size,
        start_distance=stage.start_distance,
        finish_distance=stage.finish_distance,
    )

    utils.save_figure(fig, os.path.join(save_path, "topdown.png"))
    plt.close(fig)

    fig = utils.plot_simulation(
        np.log(result.top_down + 10e-12),
        pixel_size_x=parameters.pixel_size,
        start_distance=stage.start_distance,
        finish_distance=stage.finish_distance,
    )

    utils.save_figure(fig, os.path.join(save_path, "log_topdown.png"))
    plt.close(fig)

    fig = utils.plot_simulation(
        arr=result.side_on,
        pixel_size_x=parameters.pixel_size,
        start_distance=stage.start_distance,
        finish_distance=stage.finish_distance,
    )
    utils.save_figure(fig, os.path.join(save_path, "sideon.png"))
    plt.close(fig)

    if result.freq_arr is not None:
        fig = utils.plot_image(
            result.freq_arr,
            "Frequency Array",
            save=True,
            fname=os.path.join(save_path, "freq.png"),
        )
        plt.close(fig)

    if result.delta is not None:
        fig = utils.plot_image(
            result.delta,
            "Delta Profile",
            save=True,
            fname=os.path.join(save_path, "delta.png"),
        )
        plt.close(fig)

    if result.phase is not None:
        utils.plot_image(
            result.phase,
            "Phase Profile",
            save=True,
            fname=os.path.join(save_path, "phase.png"),
        )
        plt.close(fig)

    if result.lens is not None:
        fig = utils.plot_lens_profile_2D(result.lens)
        utils.save_figure(fig, fname=os.path.join(save_path, "lens_profile.png"))

        fig = utils.plot_lens_profile_slices(result.lens)
        utils.save_figure(fig, fname=os.path.join(save_path, "lens_slices.png"))

