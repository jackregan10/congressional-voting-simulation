from genericpath import exists
import pandas as pd
import re

class ReadFile:

    def __init__ (self, filePath):
        singleValues = {}
        rangeValues = {}
        
        try:
            self.filePath = filePath
        except:
            print("File reading error.")
    
    """
    Reads csv file into a pandas data frame called input_data
        
    Author: Jack Regan
    """
    def readFile (self):
    
        
       with open(self.filePath, "r") as file:
        for line in file:
            # Extract numbers from each line
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            numbers = [float(n) if '.' in n else int(n) for n in numbers]

            # Extract parameter name from the comment (after "/* ... */")
            comment_match = re.search(r"/\*\s*(.*?)\s*\*/", line)
            param_name = comment_match.group(1) if comment_match else f"param_{len(single_values) + len(range_values) + 1}"

            # Store in the appropriate dictionary
            if len(numbers) == 1:
                self.singleValues[param_name] = numbers[0]
            elif len(numbers) == 3:
                self.rangeValues[param_name] = numbers
            else:
                print(f"Warning: Unexpected format in line -> {line.strip()}")
    
    def getSingleValues(self):
        return self.singleValues
    
    def getRangeValues(self):
        return self.rangeValues