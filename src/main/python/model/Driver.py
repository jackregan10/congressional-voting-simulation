from ReadFile import ReadFile
from WriteFile import WriteFile
import pandas as pd


class Driver:
    

    def runModel(self):
        outputData = pd.DataFrame({
                "Output Data One": [0], 
                "Output Data Two": [0], 
                "Output Data Three": [0], 
                "Output Data Four": [0], 
                "Output Data Five": [0],
                "Output Data Six": [0]
            })
        
        fileReader = ReadFile("src/main/resources/simulation_input.txt")
        
        parameters = fileReader.readFile()
        
        parameterData = pd.DataFrame({
                "Periods End": [parameters[0]], 
                "Runs": [parameters[1]], 
                "Print Period Data": [parameters[2]], 
                "Print Every N Periods": [parameters[3]], 
                "DataTakingForm": [parameters[4]]
            })
        
        
        # outputData = Model.runModel(outputData)
        fileWriter = WriteFile()
        
        fileWriter.writeFile(parameterData, outputData)
        
        
if __name__ == "__main__":

    simulation = Driver()

    simulation.runModel()