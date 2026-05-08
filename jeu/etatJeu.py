from jeu.carte import Carte
from jeu.joueur import Joueur
from jeu.action import Action

class EtatJeu:
    def __init__(self, joueur1: Joueur, joueur2: Joueur):
        self.joueurs = [joueur1, joueur2]
        self.joueur_courant = 0
        self.numero_manche = 1

    def get_joueur_courant(self):
        return self.joueurs[self.joueur_courant]
    
    def get_adversaire(self):
        return self.joueurs[1 - self.joueur_courant]
    
    def changer_joueur(self):
        self.joueur_courant = 1 - self.joueur_courant
        if self.get_joueur_courant().a_passe and not self.manche_terminee():
            self.joueur_courant = 1 - self.joueur_courant

    def manche_terminee(self):
        return all(j.a_passe for j in self.joueurs)
    
    def partie_terminee(self):
        return any(j.manches_gagnees == 2 for j in self.joueurs) 
    
    def terminer_manche(self):
        j1, j2 = self.joueurs

        if j1.score_manche > j2.score_manche:
            j1.manche_suivante(True)
            j2.manche_suivante(False)
            self.joueur_courant = 0
        elif j2.score_manche > j1.score_manche:
            j2.manche_suivante(True)
            j1.manche_suivante(False)
            self.joueur_courant = 1
        elif j1.score_manche == j2.score_manche:
            j1.manche_suivante(True)
            j2.manche_suivante(True)
            self.joueur_courant = 0

        self.numero_manche += 1

    def actions_possibles(self):
        joueur = self.get_joueur_courant()

        actions = []

        for i in range(len(joueur.main)):
            actions.append(Action("jouer", i))

        actions.append(Action("passer"))

        return actions

    def appliquer_action(self, action: Action):
        joueur = self.get_joueur_courant()

        if action.est_jouer():
            index = action.index_carte

            if index is None:
                raise ValueError("Index de carte manquant")

            if index < 0 or index >= len(joueur.main):
                raise ValueError("Index de carte invalide")

            joueur.jouer_carte(index)

        elif action.est_pass():
            joueur.passer_manche()

        else:
            raise ValueError("Type d'action invalide")

        if not self.manche_terminee():
            self.changer_joueur()

    def copier(self):
        j1 = self.joueurs[0]
        j2 = self.joueurs[1]

        nouveau_j1 = Joueur(j1.nom,init_deck=False)
        nouveau_j2 = Joueur(j2.nom,init_deck=False)

        nouveau_j1.main = [Carte(c.nom, c.valeur, c.type_carte) for c in j1.main]
        nouveau_j2.main = [Carte(c.nom, c.valeur, c.type_carte) for c in j2.main]

        nouveau_j1.cartes_jouees = [Carte(c.nom, c.valeur, c.type_carte) for c in j1.cartes_jouees]
        nouveau_j2.cartes_jouees = [Carte(c.nom, c.valeur, c.type_carte) for c in j2.cartes_jouees]

        nouveau_j1.score_manche = j1.score_manche
        nouveau_j2.score_manche = j2.score_manche

        nouveau_j1.a_passe = j1.a_passe
        nouveau_j2.a_passe = j2.a_passe

        nouveau_j1.manches_gagnees = j1.manches_gagnees
        nouveau_j2.manches_gagnees = j2.manches_gagnees

        etat = EtatJeu(nouveau_j1, nouveau_j2)
        etat.joueur_courant = self.joueur_courant
        etat.numero_manche = self.numero_manche
        return etat

    def __repr__(self):
        return (f"Manche {self.numero_manche} | "
                f"{self.joueurs[0].nom}: {self.joueurs[0].score_manche} | "
                f"{self.joueurs[1].nom}: {self.joueurs[1].score_manche} | "
                f"{self.get_joueur_courant().afficher_main}")