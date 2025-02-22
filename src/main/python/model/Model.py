import numpy as np
import pandas as pd

from Agent import Agent

"""
Initializes agent list, runs simulatin routine on data and sets output data

Author: Jack Regan
"""

class Model:    
    
    def __init__ (self, agentParameters):
        self.agentParameters = agentParameters
        self.agentMean = np.double([
            agentParameters["PolarizationMean"], 
            agentParameters["ReelectionProxMean"], 
            agentParameters["GroupThinkScoreMean"], 
            agentParameters["ConformityMean"]
        ])
        self.decayRate = agentParameters["DecayRate"]
        self.historicalRate = agentParameters["HistoricalRate"]
        self.iterations = agentParameters["Iterations"]
        self.cycles = agentParameters["Cycles"]
        self.numParameters = agentParameters["NumParameters"]
        
    # Main iterated loop
    def runRoutine(self):
        outputData = pd.DataFrame({
            "Num Vote": list(range(1, self.iterations + 1)), 
        })
        for params in range(int(self.numParameters)):
            innerIndex = 4
            for cycle in range(innerIndex):
                parameterValues = [
                        self.agentMean[0],
                        self.agentMean[1],
                        self.agentMean[2],
                        self.agentMean[3]
                ]
                # Append the new DataFrame to outputData
                paramsHeader = f"Parameters {params}:{cycle}"
                outputData[paramsHeader] = pd.Series(parameterValues)
                            
                defectionRateHistory = []
                            # Update defection history and agent mean for each iteration
                for iteration in range(self.iterations):
                    prob = self.determineDefectionRate()
                    if iteration == 0:
                        defectionRateHistory.append(prob)
                    else:
                        defectionRateHistory.append(self.determineTimeDecay(prob, defectionRateHistory))
                                
                        # Update agent mean after the cycle (assuming you meant to update this)
                defectionHeader = f"Defection Rate {params}:{cycle}"
                outputData[defectionHeader] = defectionRateHistory
                self.agentMean[params] += 0.2
                if params == 3 and cycle == 2:
                    cycle -= 1
            if params == 0:
                innerIndex -= 1
        return outputData
        
    
    # Determine current defection rate with a logisitca equation
    # Logistic Parameters: polarization, reelection proximity, group think score, conformity score
    def determineDefectionRate(self):
        agent = self.defineAgent(self.agentParameters)
        linearCombination = agent.getPolarization() + agent.getReelectionProx() + agent.getGroupThinkScore() + agent.getConformity()
        currentDefectionRate = 1 / (1 + np.exp(-linearCombination))
        return currentDefectionRate
  
    # Determine effect of time decay on current defection rate using an exponential decay model
    def determineTimeDecay(self, currentDefectionRate, defectionRateHistory):
        defectionRateDifference = defectionRateHistory[len(defectionRateHistory) - 1] - currentDefectionRate
        
        defection_influence = np.tanh(defectionRateDifference) * self.historicalRate * np.exp(self.decayRate * len(defectionRateHistory))
        return currentDefectionRate + defection_influence
    
    # Define an agent's random parameters using a normal distribution
    def defineAgent(self, agentParameters):
        p = np.random.normal(agentParameters["PolarizationMean"], agentParameters["Polarizationstdev"])
        rep = np.random.normal(agentParameters["ReelectionProxMean"], agentParameters["ReelectionProxstdev"])
        g = np.random.normal(agentParameters["GroupThinkScoreMean"], agentParameters["GroupThinkScorestdev"])
        c = np.random.normal(agentParameters["ConformityMean"], agentParameters["Conformitystdev"])
        
        agent = Agent(p, rep, g, c)
        
        return agent
        