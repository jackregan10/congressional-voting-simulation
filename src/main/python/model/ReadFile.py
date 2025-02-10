from genericpath import exists
import pandas as pd

class ReadFile:

    def __init__ (self, file_path):
        try:
            self.file_path = file_path
        except:
            print("File reading error.")
    
    """
    Reads csv file into a pandas data frame called input_data
        
    Author: Jack Regan
    """
    def readFile (self):
        parameterString = [[]]
        input = open(self.file_path)
        
        for line in input:
            words = line.split()
            for word in words:
                try: parameterString.append(float(word))
                except: break
                
        input.close()
        return parameterString
    
    