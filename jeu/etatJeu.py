from jeu.joueur import Joueur

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
        elif j2.score_manche > j1.score_manche:
            j2.manche_suivante(True)
            j1.manche_suivante(False)
        elif j1.score_manche == j2.score_manche:
            j1.manche_suivante(True)
            j2.manche_suivante(True)

        self.numero_manche += 1

    def jouer_carte(self, index):
        joueur = self.get_joueur_courant()
        if index < 0 or index >= len(joueur.main):
            raise ValueError("Index de carte invalide")
        joueur.jouer_carte(index)
        if not self.manche_terminee():
            self.changer_joueur()
    
    def passer(self):
        joueur = self.get_joueur_courant()
        joueur.passer_manche()
        if not self.manche_terminee():
            self.changer_joueur()

    def __repr__(self):
        return (f"Manche {self.numero_manche} | "
                f"{self.joueurs[0].nom}: {self.joueurs[0].score_manche} | "
                f"{self.joueurs[1].nom}: {self.joueurs[1].score_manche} | "
                f"{self.get_joueur_courant().afficher_main}")