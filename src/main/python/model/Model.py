import numpy as np
import pandas as pd

from Agent import Agent

class Model:
    """
    This class is in charge of the model routine. It runs the model for a set number of iterations
    and cycles, updating the defection rate for each agent at each iteration. The model uses a logistic
    equation to determine the defection rate for each agent, and then uses an exponential decay model to
    determine the effect of time decay on the defection rate. The model then updates the agent mean for each
    cycle, and continues to run the model until the agent mean reaches a certain threshold.

    Author: Jack Regan
    """  
    def __init__ (self, agent_parameters):
        self.agent_parameters = agent_parameters
        self.agent_mean = np.double([
            agent_parameters["PolarizationMean"],
            agent_parameters["ReelectionProxMean"],
            agent_parameters["GroupThinkScoreMean"],
            agent_parameters["ConformityMean"]
        ])
        self.decay_rate = agent_parameters["DecayRate"]
        self.historical_rate = agent_parameters["HistoricalRate"]
        self.iterations = agent_parameters["Iterations"]
        self.cycles = agent_parameters["Cycles"]
        self.num_parameters = agent_parameters["NumParameters"]
    def run_routine(self):
        """
        This method runs the model routine for a set number of iterations and cycles. It updates the defection
        rate for each agent at each iteration, and then uses an exponential decay model to determine the effect
        of time decay on the defection rate. The model then updates the agent mean for each cycle, and continues
        to run the model until the agent mean reaches a certain threshold.

        Returns:
            DataFrame: contains the output data
        """
        output_data = pd.DataFrame({
            "Num Vote": list(range(1, self.iterations + 1)), 
        })
        for params in range(int(self.num_parameters)):
            cycle = 1
            if params > 0:
                self.agent_mean[params] += 0.2
            while self.agent_mean[params] <= 0.9:
                parameter_values = [
                        self.agent_mean[0],
                        self.agent_mean[1],
                        self.agent_mean[2],
                        self.agent_mean[3]
                ]
                params_header = f"Parameters {params}:{cycle}"
                output_data[params_header] = pd.Series(parameter_values)                
                defection_rate_history = []
                for iteration in range(self.iterations):
                    prob = self.determine_defection_rate()
                    if iteration == 0:
                        defection_rate_history.append(prob)
                    else:
                        defection_rate_history.append(self.determine_time_decay(prob, defection_rate_history))
                defection_header = f"Defection Rate {params}:{cycle}"
                output_data[defection_header] = defection_rate_history
                if self.agent_mean[params] < 0.8:
                    self.agent_mean[params] += 0.2
                else:
                    break
                cycle += 1
        return output_data
    def determine_defection_rate(self):
        """
        This method determines the defection rate for the agent based on the agent's attributes.

        Returns:
            double: The value of the defection rate.
        """
        agent = self.define_agent(self.agent_parameters)
        linear_combination = agent.get_polarization() + agent.get_reelection_prox() + agent.get_group_think_score() + agent.get_conformity()
        current_defection_rate = 1 / (1 + np.exp(-linear_combination))
        return current_defection_rate
    def determine_time_decay(self, current_defection_rate, defection_rate_history):
        """
        This method determines the time decay of the defection rate.

        Args:
            current_defection_rate (double): The value of the current defection rate.
            defection_rate_history (list): A list of prior defection rates.

        Returns:
            double: The value of the current defection rate with time decay.
        """
        defection_rate_difference = defection_rate_history[len(defection_rate_history) - 1] - current_defection_rate
        
        defection_influence = np.tanh(defection_rate_difference) * self.historical_rate * np.exp(self.decay_rate * len(defection_rate_history))
        return current_defection_rate + defection_influence
    def define_agent(self, agent_parameters):
        """
        This method defines an agent with the given parameters.

        Args:
            agent_parameters (list): The parameters to define the agent with.

        Returns:
            Agent: Custom object holding state for a paraterized agent.
        """
        p = np.random.normal(agent_parameters["PolarizationMean"], agent_parameters["Polarizationstdev"])
        rep = np.random.normal(agent_parameters["ReelectionProxMean"], agent_parameters["ReelectionProxstdev"])
        g = np.random.normal(agent_parameters["GroupThinkScoreMean"], agent_parameters["GroupThinkScorestdev"])
        c = np.random.normal(agent_parameters["ConformityMean"], agent_parameters["Conformitystdev"])
        agent = Agent(p, rep, g, c)
        return agent
