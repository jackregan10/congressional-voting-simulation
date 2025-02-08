from genericpath import exists
from networkx import is_path
import pandas as pd

class ReadFile:
    
    is_path
    
    def __Init__ (self, file_path):
        if (exists(file_path)):
            self.file_path = file_path
            
    def readFile (self):
        input_data = pd.read_csv(file_path)
    
        print(input_data.head)
        print(input_data.columns)
        
        return input_data
    
    