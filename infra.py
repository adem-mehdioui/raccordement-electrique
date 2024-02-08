class Infra:

    def __init__(self, infra_id, infra_type, longueur):
          
          self.infra_id = infra_id
          self.infra_type = infra_type
          self.longueur = longueur


    
    def calculate_difficulty(self, num_houses_connected):
        """
        Calculate the difficulty of the infrastructure based on the formula:
        Difficulty(infra) = longueur / number of houses it connects
        """
        return self.longueur / num_houses_connected