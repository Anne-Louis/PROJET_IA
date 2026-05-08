from ia.minimax import alphabeta
from ia.evaluation import evaluation_facile


PROFONDEUR = 1


def choisir_action(etat):
    joueur_max = etat.get_joueur_courant()

    _, action = alphabeta(
        etat,
        PROFONDEUR,
        float("-inf"),
        float("inf"),
        joueur_max,
        evaluation_facile
    )

    return action


def choisir_action_debug(etat):

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
            evaluation_facile
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