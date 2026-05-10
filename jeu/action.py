class Action:
    """
    Représente une action possible dans le jeu.
    Une action peut être :
    - jouer une carte
    - passer la manche

    Si l'action est "jouer",
    un index de carte est nécessaire.
    """

    def __init__(self, type_action: str, index_carte: int | None = None):
        """
        Initialise une nouvelle action.

        Args:
            type_action (str):
                Type de l'action ("jouer" ou "passer").

            index_carte (int | None):
                Index de la carte à jouer dans la main.
                Inutile pour l'action "passer".
        """

        self.type_action = type_action
        self.index_carte = index_carte

    def est_pass(self):
        """
        Vérifie si l'action correspond à un passage.

        Returns:
            bool: True si l'action est "passer".
        """

        return self.type_action == "passer"

    def est_jouer(self):
        """
        Vérifie si l'action correspond à un jeu de carte.

        Returns:
            bool: True si l'action est "jouer".
        """

        return self.type_action == "jouer"

    def __repr__(self):
        """
        Retourne une représentation textuelle de l'action.

        Returns:
            str: Chaîne représentant l'action.
        """

        if self.est_pass():
            return "Action(PASSER)"

        return f"Action(JOUER, index={self.index_carte})"