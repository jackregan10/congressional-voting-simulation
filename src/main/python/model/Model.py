import numpy as np

from Agent import Agent

"""
Initializes agent list, runs simulatin routine on data and sets output data

Author: Jack Regan
"""

class Model:    
    
    def _init__ (self, agentParameters):
        self.agent = self.defineAgent(agentParameters)
        self.decayRate = agentParameters["DecayRate"]
        self.historicalRate = agentParameters["HistoricalRate"]
        self.iterations = agentParameters["Iterations"]
        self.defectionRateHistory = []
        
    # Main iterated loop
    def runRoutine(self):
        for i in range(0, self.iterations):
            prob = self.determineDefectionRate()
            # If first vote, no historical impact will be considered
            if i == 0:
                self.history.append(prob)
            else:
                self.history.append(self.determineTimeDecay(prob))
        return self.history
        
    
    # Determine current defection rate with a logisitca equation
    # Logistic Parameters: polarization, reelection proximity, group think score, conformity score
    def determineDefectionRate(self):
        linearCombination = self.agent.getPolarization + self.agent.getReelectionProx + self.agent.getGroupThinkScore, self.agent.getConformtiy
        currentDefectionRate = 1 / (1 + np.exp(-linearCombination))
        return currentDefectionRate
  
    # Determine effect of time decay on current defection rate using an exponential decay model
    def determineTimeDecay(self, currentDefectionRate):
        defectionRateDifference = self.history[self.history.len] - currentDefectionRate
        
        defection_influence = np.tanh(defectionRateDifference) * self.historicalWeight * np.exp(self.decayRate * (self.history.len + 1))
        
        return currentDefectionRate + defection_influence
    
    # Define an agent's random parameters using a normal distribution
    def defineAgent(self, agentParameters):
        p = np.random.normal(agentParameters["PolarizationMean"], agentParameters["Polarizationstdev"])
        rep = np.random.normal(agentParameters["ReelecetionProxMean"], agentParameters["Reelectionproxstdev"])
        g = np.random.normal(agentParameters["GroupThinkScoreMean"], agentParameters["GroupThinkSocrestdev"])
        c = np.random.normal(agentParameters["ConformityMean"], agentParameters["Conformitystdev"])
        
        agent = Agent(p, rep, g, c)
        
        return agent
        