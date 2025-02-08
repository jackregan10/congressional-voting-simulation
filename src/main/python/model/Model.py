class Model:    
    
    def _init__ (self, numIterations, numAgents, agentData):
        iterations = numIterations
        agents = numAgents
        self.agentData = agentData
        
        
        """
        Initializes agent list, runs simulatin routine on data and sets output data
        
        Author: Jack Regan
        """
    def runRoutine(self):
        agentList = []
        for i in range(self.agents):
        # Add parameter values from agentData
           # agentList.append(Agent(Param, Param, Param, Param))
            