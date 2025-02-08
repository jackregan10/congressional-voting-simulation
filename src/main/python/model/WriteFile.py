import pandas as pd

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
            self.output_data.to_csv("./main/output/Defection-Simulation-Output.csv", index=False)
        
        except Exception as e:
            print(f"Error writing DataFrame: {str(e)} to csv.")
