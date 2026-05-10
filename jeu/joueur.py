from utils import decks

class Joueur:
    """
    Représente un joueur du jeu.

    Chaque joueur possède :
    - un deck
    - une main
    - un score de manche
    - un nombre de manches gagnées
    - un état de passage
    - les cartes jouées durant la manche
    """

    def __init__(self, nom: str, init_deck: bool = True):
        """
        Initialise un nouveau joueur.

        Args:
            nom (str): Nom du joueur.

            init_deck (bool):
                Indique si le deck et la main doivent être générés.
                Utilisé principalement pour les copies d'état
                dans le Minimax.
        """

        self.score_manche = 0
        self.manches_gagnees = 0
        self.a_passe = False
        self.nom = nom
        self.cartes_jouees = []

        if init_deck:
            self.deck = decks.creer_deck_joueur()
            self.main = decks.distribuer_cartes(self.deck)

        else:
            self.deck = []
            self.main = []

    def jouer_carte(self, index: int):
        """
        Joue une carte depuis la main du joueur.

        La carte :
        - est retirée de la main
        - est ajoutée aux cartes jouées
        - augmente le score de la manche

        Args:
            index (int): Index de la carte à jouer.
        """

        carte = self.main.pop(index)
        self.cartes_jouees.append(carte)
        self.score_manche += carte.valeur

    def passer_manche(self):
        """
        Fait passer le joueur pour la manche actuelle.
        """

        self.a_passe = True

    def manche_suivante(self, a_gagne_manche: bool):
        """
        Prépare le joueur pour la manche suivante.

        Réinitialise :
        - le score de manche
        - l'état de passage
        - les cartes jouées

        Incrémente également le nombre de manches gagnées
        si nécessaire.

        Args:
            a_gagne_manche (bool):
                True si le joueur a gagné la manche.
        """

        if a_gagne_manche:
            self.manches_gagnees += 1

        self.a_passe = False
        self.score_manche = 0
        self.cartes_jouees = []

    def afficher_main(self):
        """
        Affiche toutes les cartes de la main du joueur.
        """

        for i, carte in enumerate(self.main):
            print(f"{i} : {carte}")  