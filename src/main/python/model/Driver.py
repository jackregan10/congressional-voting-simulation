from ReadFile import ReadFile
from WriteFile import WriteFile
from Model import Model

import pandas as pd


"""
Call main funciton to read input file, run simulation, and output excel sheet
    
Author: Jack Regan
"""
class Driver:
    

    def runModel(self):
        
        fileReader = ReadFile("src/main/resources/simulation_input.txt")
        fileReader.readFile()
        parameters = fileReader.getSingleValues()
        
        model = Model(parameters)
        output = model.runRoutine()
        
        parameterData = pd.DataFrame({
            "Runs": [parameters["Iterations"]], 
            "Historical Rate": [parameters["HistoricalRate"]],
            "Decay Rate": [parameters["DecayRate"]],
            "Min Polarization Mean": [parameters["PolarizationMean"]],
            "Max Polarization Mean": [parameters["PolarizationMean"] * parameters["Cycles"]],
            "Min Reelection Proximity Mean": [parameters["ReelectionProxMean"]],
            "Max Reelection Proximity Mean": [parameters["ReelectionProxMean"] * parameters["Cycles"]],
            "Min Group Think Score Mean": [parameters["GroupThinkScoreMean"]],
            "Max Group Think Score Mean": [parameters["GroupThinkScoreMean"] * parameters["Cycles"]],
            "Min Conformity Mean": [parameters["ConformityMean"]],
            "Max Conformity Mean": [parameters["ConformityMean"] * parameters["Cycles"]]
        })
       
        
        fileWriter = WriteFile()
        
        fileWriter.writeFile(parameterData, output)
        
        
if __name__ == "__main__":

    simulation = Driver()
    
    simulation.runModel()