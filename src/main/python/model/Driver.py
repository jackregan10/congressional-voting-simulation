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
        singleValues = fileReader.getSingleValues()
        
        model = Model(singleValues)
        history = model.runRoutine()
        
        parameterData = pd.DataFrame({
                "Periods End": [singleValues["periodsEnd"]], 
                "Runs": [singleValues["Iterations"]], 
                "Print Period Data": [singleValues["printPeriodData"]], 
                "Print Every N Periods": [singleValues["printEveryNPeriods"]], 
                "DataTakingForm": [singleValues["dataTakingForm"]]
            })
        
        
        outputData = pd.DataFrame({
                "Num Vote": list(range(1,101)), 
                "Probability of Defection": history
            })
        
       
        
        fileWriter = WriteFile()
        
        fileWriter.writeFile(parameterData, outputData)
        
        
if __name__ == "__main__":

    simulation = Driver()
    
    simulation.runModel()