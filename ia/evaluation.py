from jeu.etatJeu import EtatJeu
from jeu.joueur import Joueur


def evaluation_facile(etat, joueur_max: Joueur):
    """
    Évaluation très simple basée uniquement sur l'écart de score.

    Objectif :
    - comparer directement les points de la manche
    - aucune notion de stratégie ou de ressources
    """

    joueur = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    adversaire = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    return joueur.score_manche - adversaire.score_manche


def evaluation_moyenne(etat, joueur_max):
    """
    Évaluation intermédiaire.

    Ajoute à l'écart de score :
    - la notion de tempo (différence de score)
    - la gestion des ressources (cartes restantes)
    - un coût approximatif des cartes jouées
    - une réaction simple au fait que l'adversaire ait passé
    """

    j = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    a = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    ecart = j.score_manche - a.score_manche

    score = 0
    score += 2 * ecart

    score += 1.0 * (len(j.main) - len(a.main))

    cout = sum(c.valeur for c in j.cartes_jouees)
    score -= 0.2 * cout

    if a.a_passe:
        if ecart > 0:
            score += 15 
        else:
            score += 5 * len(j.main)

    return score


def evaluation_difficile(etat, joueur_max):
    """
    Évaluation avancée type IA "forte".

    Combine plusieurs notions stratégiques :
    - tempo (écart de score)
    - gestion des ressources
    - coût des cartes jouées (efficacité)
    - gestion avancée du pass adverse
    - logique de sacrifice de manche
    - vision globale du match (manches gagnées)
    """

    joueur = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    adversaire = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    score = 0

    ecart = joueur.score_manche - adversaire.score_manche
    score += 2.0 * ecart

    diff_cartes = len(joueur.main) - len(adversaire.main)
    score += 1.2 * diff_cartes

    cout_joueur = sum(c.valeur for c in joueur.cartes_jouees)
    score -= 0.3 * cout_joueur

    if adversaire.a_passe:
        if ecart > 0:

            score += 30
            score += 5 * len(joueur.main)
            score -= 1.0 * ecart

        else:
            deficit = abs(ecart)

            meilleure_carte = min((c.valeur for c in joueur.main), default=999)

            if meilleure_carte <= deficit + 1:
                score += 10
            else:
                score += 15 * len(joueur.main)

    if joueur.manches_gagnees > adversaire.manches_gagnees:
        if ecart < -8:
            score += 10 

        elif ecart > 0:
            score += 5

    score += 15 * (joueur.manches_gagnees - adversaire.manches_gagnees)

    score += 0.01 * len(joueur.main)

    return score