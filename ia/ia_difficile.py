from ia.minimax import alphabeta
from ia.evaluation import evaluation_difficile

PROFONDEUR = 5

def choisir_action(etat):
    """
    Fonction principale utilisée par l'IA.

    Elle appelle l'algorithme Alpha-Bêta pour :
    - explorer les coups possibles
    - choisir l'action optimale selon l'évaluation difficile
    """

    joueur_max = etat.get_joueur_courant()

    _, action = alphabeta(
        etat,
        PROFONDEUR,
        float("-inf"),
        float("inf"),
        joueur_max,
        evaluation_difficile
    )

    return action


def choisir_action_debug(etat):
    """
    Version debug de l'IA.

    Permet de :
    - tester toutes les actions possibles
    - récupérer les scores associés
    - observer le comportement de l'algorithme Alpha-Bêta

    Utile pour analyser :
    - pourquoi une action est choisie
    - la qualité de la fonction d'évaluation
    - la stabilité des décisions
    """

    joueur_max = etat.get_joueur_courant()

    scores_possibles = []

    meilleure_action = None
    meilleur_score = float("-inf")

    for action in etat.actions_possibles():
        copie = etat.copier()
        copie.appliquer_action(action)

        score, _ = alphabeta(
            copie,
            PROFONDEUR - 1,
            float("-inf"),
            float("inf"),
            joueur_max,
            evaluation_difficile
        )

        scores_possibles.append(score)

        if score > meilleur_score:
            meilleur_score = score
            meilleure_action = action

    infos_debug = {
        "scores_possibles": scores_possibles,
        "score_choisi": meilleur_score
    }

    return meilleure_action, infos_debug