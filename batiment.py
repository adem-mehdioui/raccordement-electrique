# Import the Infra class
from infra import Infra

class Batiment:

# Class attributes and methods go here
    

# Initializer method (constructor)
    def __init__(self, id_batiment, nb_maisons):
        self.id_batiment = id_batiment
        self.nb_maisons = nb_maisons
        self.connected_infras = []  # Initialize an empty list to store infrastructures

    
    def ajouter_infra(self, infrastructure) : 

        self.connected_infras.append(infrastructure)


    def supprimer_infra(self, infrastructure) :

        if infrastructure in self.connected_infras:
            self.connected_infras.remove(infrastructure)


    def calculate_difficulty(self):
        """
        Calculate the difficulty of the building based on the formula:
        Difficulty(batiment) = sum of difficulties of infras connecting it
        """
        total_difficulty = 0
        for infra in self.connected_infras:
            total_difficulty += infra.calculate_difficulty(self.nb_maisons)
        return total_difficulty
