from jeu.action import Action
from jeu.etatJeu import EtatJeu
from jeu.joueur import Joueur


def alphabeta(etat: EtatJeu,
              profondeur: int,
              alpha: float,
              beta: float,
              joueur_max: Joueur,
              eval_fn):
    """
    Implémentation de l'algorithme Minimax avec élagage Alpha-Bêta.

    Objectif :
    - explorer l'arbre des coups possibles
    - éliminer les branches inutiles (alpha-bêta)
    - retourner le meilleur coup selon une fonction d'évaluation

    Args:
        etat (EtatJeu): état actuel du jeu
        profondeur (int): profondeur de recherche restante
        alpha (float): meilleure valeur garantie pour le joueur MAX
        beta (float): meilleure valeur garantie pour le joueur MIN
        joueur_max (Joueur): joueur pour lequel on optimise le score
        eval_fn: fonction d'évaluation heuristique
    """

    # =========================
    # CAS TERMINAL
    # =========================
    # On arrête la recherche si :
    # - profondeur atteinte
    # - partie terminée
    # - manche terminée
    if profondeur == 0 or etat.partie_terminee() or etat.manche_terminee():
        return eval_fn(etat, joueur_max), None

    # =========================
    # DÉTERMINER LE RÔLE ACTUEL
    # =========================
    # MAX = joueur qu'on cherche à optimiser
    # MIN = adversaire
    maximisant = etat.get_joueur_courant().nom == joueur_max.nom

    # =========================
    # CAS MAX (IA)
    # =========================
    if maximisant:
        meilleur_score = float("-inf")
        meilleure_action = None

        for action in etat.actions_possibles():
            # Simulation du coup
            copie = etat.copier()
            copie.appliquer_action(action)

            # Appel récursif
            score, _ = alphabeta(
                copie,
                profondeur - 1,
                alpha,
                beta,
                joueur_max,
                eval_fn
            )

            # Mise à jour du meilleur choix
            if score > meilleur_score:
                meilleur_score = score
                meilleure_action = action

            # Mise à jour de alpha (meilleur garanti pour MAX)
            alpha = max(alpha, score)

            # =========================
            # ELAGAGE
            # =========================
            # Si beta <= alpha, inutile d'explorer davantage
            # car MIN ne laissera jamais arriver cette branche
            if beta <= alpha:
                break

        return meilleur_score, meilleure_action

    # =========================
    # CAS MIN (ADVERSAIRE)
    # =========================
    else:
        meilleur_score = float("inf")
        meilleure_action = None

        for action in etat.actions_possibles():
            # Simulation du coup adverse
            copie = etat.copier()
            copie.appliquer_action(action)

            # Appel récursif
            score, _ = alphabeta(
                copie,
                profondeur - 1,
                alpha,
                beta,
                joueur_max,
                eval_fn
            )

            # Mise à jour du pire cas pour MAX (donc meilleur pour MIN)
            if score < meilleur_score:
                meilleur_score = score
                meilleure_action = action

            # Mise à jour de beta (meilleur garanti pour MIN)
            beta = min(beta, score)

            # =========================
            # ELAGAGE
            # =========================
            if beta <= alpha:
                break

        return meilleur_score, meilleure_action