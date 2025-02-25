class Agent:
    """
    This class keeps track of the individual agents in the model. 
    Each agent has a set of parameters that define their behavior. 
    Currently, the parameters are weighted equally within the model,
    but this could be changed in the future to allow for more complex 
    interactions between the parameters. The parameters are as follows: 
    polarization, reelection proximity, group think score, and conformity.
    The parameters are all floats between 0 and 1, with 0 being the 
    lowest value and 1 being the highest. The parameters are used to determine 
    the agent's behavior in the model.
    
    Author: Jack Regan
    """
    def __init__ (self, p, rep, g, c):
        self.polarization = float(p)
        self.reelection_prox = float(rep)
        self.group_think_score = float(g)
        self.conformity = float(c)
    def set_polarization (self, new_value):
        """
        Sets the polarization score for the agent.

        Parameters:
        newValue (float): The new value to set for the polarization score.
        """
        self.polarization = new_value
    def set_reelection_prox (self, new_value):
        """
        Sets the relection proximity think score for the agent.

        Parameters:
        newValue (float): The new value to set for the reelection proximity.
        """
        self.reelection_prox = new_value
    def set_group_think_score (self, new_value):
        """
        Sets the group think score for the agent.

        Parameters:
        newValue (float): The new value to set for the group think score.
        """
        self.group_think_score = new_value
    def set_conformity (self, new_value):
        """
        Sets the conformity attribute to a new value.

        Parameters:
        newValue (float): The new value to set for the conformity attribute.
        """
        self.conformity = new_value
    def get_polarization (self):
        """
        Returns the polarization value of the agent.

        Returns:
        float: The polarization value.
        """
        return self.polarization
    def get_reelection_prox (self):
        """
        Returns the reelection proximity value of the agent.

        Returns:
        float: The reelection proximity value.
        """
        return self.reelection_prox
    def get_group_think_score (self):
        """
        Retrieve the group think score of the agent.

        Returns:
            float: The group think score of the agent.
        """
        return self.group_think_score
    def get_conformity (self):
        """
        Retrieve the conformity value of the agent.

        Returns:
            float: The conformity value of the agent.
        """
        return self.conformity
