import os
import sys

import lens_simulation
from lens_simulation import SimulationRunner
from lens_simulation import Simulation
from lens_simulation import utils

def main(args):

    sim_runner = SimulationRunner.SimulationRunner(args)
    sim_runner.initialise_simulation()
    sim_runner.setup_simulation()
    sim_runner.run_simulations()


def run_single_simulation(config_filename: str = "config.yaml"):

    # load config
    config = utils.load_simulation_config(config_filename)
    print("Run Name: ", config["run_id"])

    # create and run simulation
    sim = Simulation.Simulation(config)
    sim.run_simulation()

if __name__ == "__main__":

    args = os.path.join(os.path.dirname(lens_simulation.__file__), "config.yaml")
    if len(sys.argv) >= 2:
        args = sys.argv[1]

    main(args)
