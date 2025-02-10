class Agent:
    
    def __init__ (self, paramOne, paramTwo, paramThree, paramFour):
        self.paramOne = paramOne
        self.paramTwo = paramTwo
        self.paramThree = paramThree
        self.paramFour = paramFour
        
    def setParamOne (self, newValue):
        paramOne = newValue
        
    def setParamTwo (self, newValue):
        paramTwo = newValue
        
    def setParamThree (self, newValue):
        paramThree = newValue
        
    def setParamFour (self, newValue):
        paramFour = newValue
        
    def getParamOne (self):
        return self.paramOne
    
    def getParamTwo (self):
        return self.paramTwo
    
    def getParamThree (self):
        return self.paramThree
    
    def getParamFour (self):
        return self.paramFour