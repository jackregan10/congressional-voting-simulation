import pandas as pd
from os.path import exists

class WriteFile:
    """
    Saves output data frame as a csv called "Defection-Simulation-Output.csv"
    The file is saved to the output folder.
        
    Author: Jack Regan
    """
    def writeFile (self, output_parameters, output_data):
        try:
           if not  isinstance(output_data, pd.DataFrame) and isinstance(output_parameters, pd.DataFrame):
                raise ValueError("Output data must be a Pandas DataFrame.")
        except Exception as e:
            print("Output data reading error")  
            return
                  
        try:
            outFile = "src/main/output/Defection-Simulation-Output.xlsx"
            if exists(outFile):
                i = 1
                outFile = "src/main/output/Defection-Simulation-Output-" + str(i) + ".xlsx"
                while exists(outFile):
                    i += 1
                    outFile = "src/main/output/Defection-Simulation-Output-" + str(i) + ".xlsx"
            with pd.ExcelWriter(outFile) as writer:       
                output_parameters.to_excel(writer, sheet_name = "Parameter Data", index = False)
                output_data.to_excel(writer, sheet_name = "Output Data", index=False)
        
        except Exception as e:
            print(f"Error writing DataFrame: {str(e)} to csv.")
