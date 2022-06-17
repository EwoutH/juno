
from lens_simulation.constants import LENS_SWEEPABLE_KEYS, MODIFICATION_SWEEPABLE_KEYS, BEAM_SWEEPABLE_KEYS, STAGE_SWEEPABLE_KEYS, GRATING_SWEEPABLE_KEYS, TRUNCATION_SWEEPABLE_KEYS, APERTURE_SWEEPABLE_KEYS

def _validate_default_lens_config(lens_config: dict) -> dict:

    # required settings
    if "name" not in lens_config:
        raise ValueError(f"Lens config requires name. None provided")
    if "medium" not in lens_config:
        raise ValueError(f"Lens config requires medium. None provided")

    # if generating profile:

    if "diameter" not in lens_config:
        raise ValueError(f"Lens config requires diameter. None provided")

    if "height" not in lens_config:
        raise ValueError(f"Lens config requires height. None provided")
    if "exponent" not in lens_config:
        raise ValueError(f"Lens config requires exponent. None provided")


    # if loading profile:
    # if "custom" not in lens_config:
    #     raise ValueError(f"Lens config requires custom to load a profile. None provided.")

    # default settings
    lens_config["custom"] = None if "custom" not in lens_config else lens_config["custom"]
    lens_config["length"] = None if "length" not in lens_config else lens_config["length"]
    lens_config["grating"] = None if "grating" not in lens_config else lens_config["grating"]
    lens_config["truncation"] = None if "truncation" not in lens_config else lens_config["truncation"]
    lens_config["aperture"] = None if "aperture" not in lens_config else lens_config["aperture"]
    lens_config["escape_path"] = None if "escape_path" not in lens_config else lens_config["escape_path"]
    lens_config["lens_type"] = "Spherical" if "lens_type" not in lens_config else lens_config["lens_type"].title()
    lens_config["inverted"] = False if "inverted" not in lens_config else lens_config["inverted"]

    # validate sweepable parameters
    lens_config = _validate_sweepable_parameters(lens_config, LENS_SWEEPABLE_KEYS)

    # validate lens modifications
    lens_config = _validate_default_lens_modification_config(lens_config)

    # validate modification sweepable parameters
    if lens_config["grating"] is not None:
        lens_config["grating"] = _validate_sweepable_parameters(lens_config["grating"], GRATING_SWEEPABLE_KEYS)
    if lens_config["truncation"] is not None:
        lens_config["truncation"] = _validate_sweepable_parameters(lens_config["truncation"], TRUNCATION_SWEEPABLE_KEYS)
    if lens_config["aperture"] is not None:
        lens_config["aperture"] = _validate_sweepable_parameters(lens_config["aperture"], APERTURE_SWEEPABLE_KEYS)

    # QUERY
    # do we want to require height, diameter, exponent if the user loads a custom profile. What is required?
    # is lens_type a required parameters? how much error checking on the lens_type, e.g. if not in LensType.name etc

    return lens_config

def _validate_sweepable_parameters(config, sweep_keys):

    for k in sweep_keys:
        
        k_stop, k_step = f"{k}_stop", f"{k}_step"
        
        # start, stop, step
        if k not in config:
            config[k] = None

        if k_stop not in config:
            config[k_stop] = None 


        if k_step not in config:
            config[k_step] = None

    return config

def _validate_default_lens_modification_config(config: dict) -> dict:

    # not providing defaults, checking types

    if config["grating"] is not None:
        if "width" not in config["grating"]:
            raise ValueError(f"Lens grating config requires width. None provided.")
        if "distance" not in config["grating"]:
            raise ValueError(f"Lens grating config requires distance. None provided.")
        if "depth" not in config["grating"]:
            raise ValueError(f"Lens grating config requires depth. None provided.")
        if "x" not in config["grating"]:
            raise ValueError(f"Lens grating config requires x. None provided.")
        if "y" not in config["grating"]:
            raise ValueError(f"Lens grating config requires y. None provided.")
        if "centred" not in config["grating"]:
            raise ValueError(f"Lens grating config requires centred. None provided.")

        # type validation
        config["grating"]["width"] = float(config["grating"]["width"])
        config["grating"]["distance"] = float(config["grating"]["distance"])
        config["grating"]["depth"] = float(config["grating"]["depth"])
        config["grating"]["x"] = bool(config["grating"]["x"])
        config["grating"]["y"] = bool(config["grating"]["y"])
        config["grating"]["centred"] = bool(config["grating"]["centred"])

    if config["truncation"] is not None:
        if "height" not in config["truncation"]:
            raise ValueError(f"Lens truncation config requires height. None provided.")
        if "radius" not in config["truncation"]:
            raise ValueError(f"Lens truncation config requires radius. None provided.")
        if "type" not in config["truncation"]:
            raise ValueError(f"Lens truncation config requires type. None provided.")
        if "aperture" not in config["truncation"]:
            raise ValueError(f"Lens truncation config requires aperture. None provided.")

        # type validation
        config["truncation"]["height"] = float(config["truncation"]["height"])
        config["truncation"]["radius"] = float(config["truncation"]["radius"])
        config["truncation"]["type"] = str(config["truncation"]["type"])
        config["truncation"]["aperture"] = bool(config["truncation"]["aperture"])

    if config["aperture"] is not None:
        if "inner" not in config["aperture"]:
            raise ValueError(f"Lens aperture config requires inner. None provided.")
        if "outer" not in config["aperture"]:
            raise ValueError(f"Lens aperture config requires outer. None provided.")
        if "type" not in config["aperture"]:
            raise ValueError(f"Lens aperture config requires type. None provided.")
        if "invert" not in config["aperture"]:
            raise ValueError(f"Lens aperture config requires invert. None provided.")

        # type validation
        config["aperture"]["inner"] = float(config["aperture"]["inner"])
        config["aperture"]["outer"] = float(config["aperture"]["outer"])
        config["aperture"]["type"] = str(config["aperture"]["type"])
        config["aperture"]["invert"] = bool(config["aperture"]["invert"])

    return config



def _validate_default_beam_config(config: dict) -> dict:
    # required settings
    if "width"  not in config:
        raise ValueError("Beam configuration requires width. None provided.")
    if "height"  not in config:
        raise ValueError("Beam configuration requires height. None provided.")

    # default settings
    config["distance_mode"] = config["distance_mode"].title() if "distance_mode" in config else "Direct"
    config["spread"] = config["spread"].title() if "spread" in config else "Plane"
    config["shape"] = config["shape"].title() if "shape" in config else "Circular"

    if "n_slices" not in config and "step_size" not in config:
        config["n_slices"] = 10

    config["n_slices"] = config["n_slices"] if "n_slices" in config else 0
    config["step_size"] = config["step_size"] if "step_size" in config else 0

    config["position_x"] = config["position_x"] if "position_x" in config else 0.0
    config["position_y"] = config["position_y"] if "position_y" in config else 0.0
    config["theta"] = config["theta"] if "theta" in config else 0.0
    config["numerical_aperture"] = config["numerical_aperture"] if "numerical_aperture" in config else None
    config["tilt_x"] = config["tilt_x"] if "tilt_x" in config else 0.0
    config["tilt_y"] = config["tilt_y"] if "tilt_y" in config else 0.0
    config["source_distance"] = config["source_distance"] if "source_distance" in config else None
    config["final_width"] = config["final_width"] if "final_width" in config else None
    config["focal_multiple"] = config["focal_multiple"] if "focal_multiple" in config else None
    config["lens_type"] = config["lens_type"].title() if "lens_type" in config else "Spherical"
    config["output_medium"] = config["output_medium"] if "output_medium" in config else 1.0

    # validate the sweepable parameters
    bc = _validate_sweepable_parameters(config, BEAM_SWEEPABLE_KEYS)
    config.update(bc)

    return config

def _validate_simulation_stage_list(stages: list, simulation_lenses: dict) -> None:
    """Validate that all lenses and mediums have been defined, and all simulation stages have been
    defined correctly.
    """

    for stage in stages:
        # validate all lens, mediums exist,
        if stage["lens"] not in simulation_lenses:
            raise ValueError(f"{stage['lens']} has not been defined in the configuration")

        stage = _validate_default_simulation_stage_config(stage)

    return stages

def _validate_default_simulation_stage_config(stage_config: dict) -> dict:

    # required settings
    if "n_slices" not in stage_config and "step_size" not in stage_config:
        raise ValueError(f"Stage config requires n_slices or step_size")
    if "start_distance" not in stage_config:
        raise ValueError(f"Stage config requires start_distance. None provided.")
    if "finish_distance" not in stage_config:
        raise ValueError(f"Stage config requires finish_distance. None provided.")
    if "output" not in stage_config:
        raise ValueError(f"Stage config requires output. None provided.")


    # default settings
    stage_config["n_slices"] = 0 if "n_slices" not in stage_config else stage_config["n_slices"]
    stage_config["step_size"] = 0 if "step_size" not in stage_config else stage_config["step_size"]
    stage_config["use_equivalent_focal_distance"] = False if "use_equivalent_focal_distance" not in stage_config else stage_config["use_equivalent_focal_distance"]
    stage_config["focal_distance_start_multiple"] = 0.0 if "focal_distance_start_multiple" not in stage_config else stage_config["focal_distance_start_multiple"]
    stage_config["focal_distance_multiple"] = 1.0 if "focal_distance_multiple" not in stage_config else stage_config["focal_distance_multiple"]

    # default conditional settings
    if stage_config["use_equivalent_focal_distance"] is True:
        stage_config["focal_distance_start_multiple"] = 0.0 if stage_config["focal_distance_start_multiple"] is None else stage_config["focal_distance_start_multiple"]
        stage_config["focal_distance_multiple"] = 1.0 if stage_config["focal_distance_multiple"] is None else stage_config["focal_distance_multiple"]

        # TODO: check the more complicated cases for these, e.g. need a height and exponent to calculate equiv focal distance

    # validate_sweepable parameters
    stage_config = _validate_sweepable_parameters(stage_config, STAGE_SWEEPABLE_KEYS)

    return stage_config


def _validate_simulation_parameters_config(config: dict) -> dict:

    if "A" not in config:
        raise ValueError(f"Sim Parameters config requires A. None provided")

    if "pixel_size" not in config:
        raise ValueError(f"Sim Parameters config requires pixel_size. None provided")

    if "sim_height" not in config:
        raise ValueError(f"Sim Parameters config requires sim_height. None provided")

    if "sim_width" not in config:
        raise ValueError(f"Sim Parameters config requires sim_width. None provided")

    if "sim_wavelength" not in config:
        raise ValueError(f"Sim Parameters config requires sim_wavelength. None provided")

    return config

def _validate_simulation_options_config(config: dict) -> dict:

    # required_settings
    if "log_dir" not in config:
        raise ValueError("Options config requires log_dir. None provided.")

    # default settings
    config["save_plot"] = True if "save_plot" not in config else config["save_plot"]
    config["save"] = False if "save" not in config else config["save"]
    config["verbose"] = False if "verbose" not in config else config["verbose"]
    config["debug"] = False if "debug" not in config else config["debug"]

    return config

def _validate_simulation_config(config: dict):

    SIM_PARAMETERS_KEY = "sim_parameters"
    OPTIONS_KEY = "options"
    BEAM_KEY = "beam"
    LENS_KEY = "lenses"
    STAGE_KEY = "stages"

    if SIM_PARAMETERS_KEY not in config:
        raise ValueError(f"Simulation config requires {SIM_PARAMETERS_KEY}. Not provided.")

    _validate_simulation_parameters_config(config[SIM_PARAMETERS_KEY])

    if OPTIONS_KEY not in config:
        raise ValueError(f"Simulation config requires {OPTIONS_KEY}. Not provided.")

    _validate_simulation_options_config(config[OPTIONS_KEY])

    if BEAM_KEY not in config:
        raise ValueError(f"Simulation config requires {BEAM_KEY}. Not provided.")

    _validate_default_beam_config(config[BEAM_KEY])

    if LENS_KEY not in config:
        raise ValueError(f"Simulation config requires {LENS_KEY}. Not provided.")

    for lens_config in config[LENS_KEY]:
        lens_config = _validate_default_lens_config(lens_config)

    if STAGE_KEY not in config:
        raise ValueError(f"Simulation config requires {STAGE_KEY}. Not provided.")

    for stage_config in config[STAGE_KEY]:

        _validate_default_simulation_stage_config(stage_config)

    return config