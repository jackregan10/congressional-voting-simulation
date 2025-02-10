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
        parameters = list()
        input = open(self.file_path)
        
        for line in input:
            words = line.split()
            parameterString = list()
            for word in words:
                try: parameterString.append(float(word))
                except: break
                
        parameters.append(parameterString)
        input.close()
    
        print(parameters.toString())
        return parameters
    
    