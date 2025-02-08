from genericpath import exists
import pandas as pd

class ReadFile:

    def __Init__ (self, file_path):
        try:
            self.file_path = file_path
        except:
            print("File reading error.")
    
    """
    Reads csv file into a pandas data frame called input_data
        
    Author: Jack Regan
    """
    def readFile (self):
        input_data = pd.read_csv(self.file_path)
    
        print(input_data.head)
        print(input_data.columns)
        
        return input_data
    
    