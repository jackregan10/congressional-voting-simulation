from ReadFile import ReadFile
from WriteFile import WriteFile
import pandas as pd

from main.python.model import Model


"""
Call main funciton to read input file, run simulation, and output excel sheet
    
Author: Jack Regan
"""
class Driver:
    

    def runModel(self):
        
        fileReader = ReadFile("src/main/resources/simulation_input.txt")
        fileReader.readFile()
        singleValues = fileReader.getSingleValues()
        
        model = Model(singleValues)
        history = model.runRoutine()
        
        parameterData = pd.DataFrame({
                "Periods End": [singleValues[0]], 
                "Runs": [singleValues[1]], 
                "Print Period Data": [singleValues[2]], 
                "Print Every N Periods": [singleValues[3]], 
                "DataTakingForm": [singleValues[4]]
            })
        
        
        outputData = pd.DataFrame({
                "Num Vote": [0], 
                "Probability of Defection": [0], 
                "Output Data Three": [0], 
                "Output Data Four": [0], 
                "Output Data Five": [0],
                "Output Data Six": [0]
            })
        
       
        
        fileWriter = WriteFile()
        
        fileWriter.writeFile(parameterData, outputData)
        
        
if __name__ == "__main__":

    simulation = Driver()

    simulation.runModel()