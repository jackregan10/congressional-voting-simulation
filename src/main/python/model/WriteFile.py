import pandas as pd
from os.path import exists

class WriteFile:

        """
        Saves output data frame as a csv called "Defection-Simulation-Output.csv"
        The file is saved to the output folder.
        
        Author: Jack Regan
        """
def writeFile (self, output_data):
    try:
        if not  isinstance(output_data, pd.DataFrame):
            raise ValueError("Output data must be a Pandas DataFrame.")
    except Exception as e:
        print("Output data reading error")  
        return
                  
    try:
        outFile = "./main/output/Defection-Simulation-Output.csv"
        if exists(outFile):
            i = 1
            outFile = "./main/output/Defection-Simulation-Output-" + str(i) + ".csv"
            while exists(outFile):
                i += 1
                outFile = "./main/output/Defection-Simulation-Output-" + str(i) + ".csv"
                    
        output_data.to_csv(outFile, index=False)
        
    except Exception as e:
        print(f"Error writing DataFrame: {str(e)} to csv.")
