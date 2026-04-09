from utils import decks 

class Joueur :
    def __init__(self, nom : str):
        self.deck = decks.creer_deck_joueur()
        self.main = decks.distribuer_cartes(self.deck)
        self.score_manche = 0
        self.manches_gagnees = 0
        self.a_passe = False
        self.nom = nom
        self.cartes_jouees = []

    def jouer_carte(self, index : int):
        carte = self.main.pop(index)
        self.cartes_jouees.append(carte)
        self.score_manche += carte.valeur

    def passer_manche(self):
        self.a_passe = True

    def manche_suivante(self, a_gagne_manche : bool):
        if a_gagne_manche :
            self.manches_gagnees += 1
        self.score_manche = 0
        self.a_passe = False

    def afficher_main(self):
        for i,carte in enumerate(self.main):
            print(f"{i} : {carte}")
    
    