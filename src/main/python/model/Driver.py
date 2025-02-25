from ReadFile import ReadFile
from WriteFile import WriteFile
from Model import Model

import pandas as pd

class Driver:
    """
    This class serves as the driver for the model. It reads in the 
    parameters from the input file, calls the routine, and writes the 
    output data to the output file.
    
    Author: Jack Regan
    """
    def run_model(self):
        """
        This method reads in the parameters from the input file, calls the
        routine, and writes the output data to the output file.
        """
        file_reader = ReadFile("src/main/resources/simulation_input.txt")
        file_reader.read_file()
        parameters = file_reader.get_single_values()
        model = Model(parameters)
        output = model.run_routine()
        parameter_data = pd.DataFrame({
            "Runs": [parameters["Iterations"]], 
            "Historical Rate": [parameters["HistoricalRate"]],
            "Decay Rate": [parameters["DecayRate"]],
            "Min Polarization Mean": [parameters["PolarizationMean"]],
            "Max Polarization Mean": [parameters["PolarizationMean"] + 0.2 * parameters["Cycles"]],
            "Min Reelection Proximity Mean": 
                [parameters["ReelectionProxMean"]],
            "Max Reelection Proximity Mean": 
                [parameters["ReelectionProxMean"] + 0.2 * parameters["Cycles"]],
            "Min Group Think Score Mean": [parameters["GroupThinkScoreMean"]],
            "Max Group Think Score Mean": 
                [parameters["GroupThinkScoreMean"] + 0.2 * parameters["Cycles"]],
            "Min Conformity Mean": [parameters["ConformityMean"]],
            "Max Conformity Mean": [parameters["ConformityMean"] + 0.2 * parameters["Cycles"]]
        })
        file_writer = WriteFile()
        file_writer.write_file(parameter_data, output)
if __name__ == "__main__":
    simulation = Driver()
    simulation.run_model()
