from jeu.action import Action
from jeu.etatJeu import EtatJeu
from jeu.joueur import Joueur

def alphabeta(etat: EtatJeu, profondeur: int, alpha: float, beta: float, joueur_max: Joueur, eval_fn):
    
    # =========================
    # CAS TERMINAL
    # =========================
    if profondeur == 0 or etat.partie_terminee() or etat.manche_terminee():
        return eval_fn(etat, joueur_max), None

    # =========================
    # MAXIMISANT OU MINIMISANT ?
    # =========================
    maximisant = etat.get_joueur_courant().nom == joueur_max.nom

    if maximisant:
        meilleur_score = float("-inf")
        meilleure_action = None

        for action in etat.actions_possibles():
            copie = etat.copier()
            copie.appliquer_action(action)

            score, _ = alphabeta(
                copie,
                profondeur - 1,
                alpha,
                beta,
                joueur_max,
                eval_fn
            )

            if score > meilleur_score:
                meilleur_score = score
                meilleure_action = action

            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return meilleur_score, meilleure_action

    # =========================
    # MINIMISANT
    # =========================
    else:
        meilleur_score = float("inf")
        meilleure_action = None

        for action in etat.actions_possibles():
            copie = etat.copier()
            copie.appliquer_action(action)

            score, _ = alphabeta(
                copie,
                profondeur - 1,
                alpha,
                beta,
                joueur_max,
                eval_fn
            )

            if score < meilleur_score:
                meilleur_score = score
                meilleure_action = action

            beta = min(beta, score)

            if beta <= alpha:
                break

        return meilleur_score, meilleure_action
