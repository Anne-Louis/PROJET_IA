from jeu.joueur import Joueur
from jeu.etatJeu import EtatJeu
from jeu.action import Action

import ia.ia_facile as ia_facile
import ia.ia_moyenne as ia_moyenne
import ia.ia_difficile as ia_difficile


# ==========================================
# AFFICHAGE
# ==========================================

def afficher_main(joueur: Joueur):
    print(f"\nMain de {joueur.nom} :")
    for i, carte in enumerate(joueur.main):
        print(f"  {i}: {carte}")

def afficher_scores(etat: EtatJeu):
    j1, j2 = etat.joueurs
    print(f"\nScores — {j1.nom}: {j1.score_manche} | {j2.nom}: {j2.score_manche}")
    print(f"Manches gagnées — {j1.nom}: {j1.manches_gagnees} | {j2.nom}: {j2.manches_gagnees}")

def afficher_gagnant(etat: EtatJeu):
    gagnants = [j for j in etat.joueurs if j.manches_gagnees >= 2]
    if gagnants:
        print(f"\n=== Partie terminée ! {gagnants[0].nom} a gagné ! ===")
    else:
        print("\n=== Partie terminée ! Égalité ! ===")


# ==========================================
# TOUR HUMAIN
# ==========================================

def tour_humain(etat: EtatJeu) -> Action:
    joueur = etat.get_joueur_courant()
    afficher_main(joueur)

    while True:
        entree = input("Tapez l'index de la carte à jouer ou 'p' pour passer : ").strip()

        if entree.lower() == "p":
            return Action("passer")

        try:
            index = int(entree)
            if 0 <= index < len(joueur.main):
                return Action("jouer", index)
            else:
                print("Index invalide, réessayez.")
        except ValueError:
            print("Entrée invalide, réessayez.")


# ==========================================
# TOUR IA
# ==========================================

def tour_ia(etat: EtatJeu, ia) -> Action:
    print("\nL'IA réfléchit...")
    action = ia.choisir_action(etat)
    print(f"L'IA joue : {action}")
    return action


# ==========================================
# BOUCLE DE JEU GÉNÉRIQUE
# ==========================================

def boucle_jeu(etat: EtatJeu, ia=None):
    """
    ia=None  -> humain vs humain
    ia=module -> joueur 2 est une IA
    """

    while not etat.partie_terminee():
        print(f"\n{'='*40}")
        print(f"  MANCHE {etat.numero_manche}")
        print(f"{'='*40}")

        while not etat.manche_terminee():
            joueur = etat.get_joueur_courant()
            afficher_scores(etat)
            print(f"\nTour de {joueur.nom}")

            # Déterminer si c'est un humain ou une IA
            est_ia = (ia is not None and joueur == etat.joueurs[1])

            if est_ia:
                action = tour_ia(etat, ia)
            else:
                action = tour_humain(etat)

            etat.appliquer_action(action)

        # Fin de manche
        etat.terminer_manche()

        print(f"\n--- Fin de la manche ---")
        for j in etat.joueurs:
            print(f"  {j.nom} | Manches gagnées : {j.manches_gagnees}")

    afficher_gagnant(etat)


# ==========================================
# MENU
# ==========================================

def choisir_ia():
    print("\nChoisissez le niveau de l'IA :")
    print("  1 - Facile")
    print("  2 - Moyenne")
    print("  3 - Difficile")

    while True:
        choix = input("Votre choix : ").strip()
        if choix == "1":
            return ia_facile
        elif choix == "2":
            return ia_moyenne
        elif choix == "3":
            return ia_difficile
        else:
            print("Choix invalide.")

def menu():
    print("\n=== Bienvenue dans le Gwent simplifié ===")

    while True:
        print("\n========================")
        print("1 - Joueur vs Joueur")
        print("2 - Joueur vs IA")
        print("3 - Quitter")
        print("========================")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            j1 = Joueur("Joueur 1")
            j2 = Joueur("Joueur 2")
            etat = EtatJeu(j1, j2)
            boucle_jeu(etat, ia=None)

        elif choix == "2":
            ia = choisir_ia()
            humain = Joueur("Joueur")
            adversaire = Joueur("IA")
            etat = EtatJeu(humain, adversaire)
            boucle_jeu(etat, ia=ia)

        elif choix == "3":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    menu()