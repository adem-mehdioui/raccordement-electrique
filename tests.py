
class Infra:
    def __init__(self, infra_id:int, infra_length:float, is_broken:bool) -> int:
        self.infra_id = infra_id
        self.infra_length = infra_length
        self.is_broken = is_broken
    pass



class Bat:
    def __init__(self, bat_id, nb_houses) -> None:
        self.bat_id = bat_id
        self.nb_houses = nb_houses
        self.connected_infras = []
    
    def add_infra(self, infra:Infra) -> None:
        self.connected_infras.append(infra)

        



""" 
Utiliser pandas pour lire le csv
Ensuite pour chaque ligne :
    On récupère l'id batiment, on vérifie s'il est déjà dans le graphe
    S'il n'y est pas on instancie Bat avec les deux premières colonnes
    Ensuite on récupère l'id infra, on vérifie si elle est déjà dans le graphe
    Si elle n'y est pas on intstancie Infra avec les trois dernières colonnes
    Puis dans tous les cas on utilise Bat.add_infra pour rajouter l'infra dans Bat.connected_infras
"""