class Carte:
    def __init__(self, nom: str, valeur: int, type_carte: str):
        self.nom = nom
        self.valeur = valeur
        self.type_carte = type_carte

    def __repr__(self):
        return f"{self.nom} ({self.valeur}) ({self.type_carte})"