from main.python.model import Model, WriteFile


class Driver:

    def runModel():
        outputData = []
        
        outputData.append(["Add varibles in output file"])
        
        outputData = Model.runModel(outputData)
        
        WriteFile(outputData)