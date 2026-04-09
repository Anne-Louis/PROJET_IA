from jeu.etatJeu import EtatJeu
from jeu.joueur import Joueur


def boucle_jeu_console():
    j1 = Joueur("Joueur 1")
    j2 = Joueur("Joueur 2")
    
    etat = EtatJeu(j1, j2)

    print("=== Bienvenue dans le Gwent simplifié ===\n")

    while not etat.partie_terminee():
        print(f"\n--- Manche {etat.numero_manche} ---\n")
        
        for j in etat.joueurs:
            j.a_passe = False

        while not etat.manche_terminee():
            joueur = etat.get_joueur_courant()
            print(f"\nTour de {joueur.nom} | Score actuel: {joueur.score_manche} | Score de l'adversaire: {etat.get_adversaire().score_manche}")
            
            print("Votre main:")
            for i, carte in enumerate(joueur.main):
                print(f"{i}: {carte}")
            
            action = input("Tapez l'index de la carte à jouer ou 'p' pour passer : ").strip()
            
            if action.lower() == "p":
                etat.passer()
                print(f"{joueur.nom} passe.")
            else:
                try:
                    index = int(action)
                    etat.jouer_carte(index)
                    print(f"{joueur.nom} joue {joueur.main[index-1] if index-1 >=0 else ''}")
                except (ValueError, IndexError):
                    print("Index invalide, recommencez.")
        
        etat.terminer_manche()
        print("\n--- Fin de la manche ---")
        for j in etat.joueurs:
            print(f"{j.nom} - manches gagnées: {j.manches_gagnees}, score manche: {j.score_manche}")

    gagnants = [j for j in etat.joueurs if j.manches_gagnees == 2]
    if gagnants:
        print(f"\n=== Partie terminée ! {gagnants[0].nom} a gagné ! ===")
    else:
        print("\n=== Partie terminée ! Égalité ! ===")

boucle_jeu_console()