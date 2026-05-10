class Carte:
    """
    Représente une carte du jeu.
    Chaque carte possède :
    - un nom
    - une valeur de puissance
    - un type de carte
      (melee, distance ou siege) (non utilisé)
    """

    def __init__(self, nom: str, valeur: int, type_carte: str):
        """
        Initialise une nouvelle carte.
        Args:
            nom (str): Nom de la carte.
            valeur (int): Valeur de puissance de la carte.
            type_carte (str): Type de la carte.
        """

        self.nom = nom
        self.valeur = valeur
        self.type_carte = type_carte

    def __repr__(self):
        """
        Retourne une représentation textuelle de la carte.

        Returns:
            str: Chaîne représentant la carte.
        """

        return f"{self.nom} ({self.valeur}) ({self.type_carte})"