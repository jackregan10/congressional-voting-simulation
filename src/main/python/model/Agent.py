class Agent:
    """
    Keeps track of parameter data for each agent
    
    Author: Jack Regan
    """
    
    def __init__ (self, p, rep, g, c):
        self.polarization = p
        self.reelectionProx = rep
        self.groupThinkScore = g
        self.conformity = c
    
    ## Agent parameter set methods
    def setPolarization (self, newValue):
        polarization = newValue
        
    def setReelectionProx (self, newValue):
        reelectionProx = newValue
        
    def setGroupThinkScore (self, newValue):
        groupThinkScore = newValue
        
    def setConformity (self, newValue):
        conformity = newValue
        
        
    ## Agent parameter get methods
    def getPolarization (self):
        return self.polarization
    
    def getReelectionProx (self):
        return self.relectionProx
    
    def getGroupThinkScore (self):
        return self.groupThinkScore
    
    def getConformity (self):
        return self.conformity