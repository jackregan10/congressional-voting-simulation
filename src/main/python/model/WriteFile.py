import pandas as pd
from os.path import exists

class WriteFile:
    
    def __Init__ (self, output_data):
        try:
            if isinstance(output_data, pd.DataFrame):
                self.output_data = output_data
        except:
            print("Output data reading error")
    
        """
        Saves output data frame as a csv called "Defection-Simulation-Output.csv"
        The file is saved to the output folder.
        
        Author: Jack Regan
        """
    def writeFile (self):        
        try:
            outFile = "./main/output/Defection-Simulation-Output.csv"
            if exists(outFile):
                i = 1
                outFile = "./main/output/Defection-Simulation-Output-" + str(i) + ".csv"
                while exists(outFile):
                    i += 1
                    outFile = "./main/output/Defection-Simulation-Output-" + str(i) + ".csv"
                    
            self.output_data.to_csv(outFile, index=False)
        
        except Exception as e:
            print(f"Error writing DataFrame: {str(e)} to csv.")
