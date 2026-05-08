from jeu.etatJeu import EtatJeu
from jeu.joueur import Joueur


def evaluation_facile(etat, joueur_max: Joueur):
    joueur = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    adversaire = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    return joueur.score_manche - adversaire.score_manche



def evaluation_moyenne(etat, joueur_max):
    j = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    a = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    ecart = j.score_manche - a.score_manche

    score = 0

    # tempo
    score += 2 * ecart

    # ressources
    score += 1.0 * (len(j.main) - len(a.main))

    # coût modéré des cartes utilisées
    cout = sum(c.valeur for c in j.cartes_jouees)
    score -= 0.2 * cout

    # réaction au pass
    if a.a_passe:
        if ecart > 0:
            score += 15
        else:
            score += 5 * len(j.main)

    return score


"""def evaluation_difficile(etat, joueur_max: Joueur):
    joueur = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    adversaire = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    score = 0
    ecart = joueur.score_manche - adversaire.score_manche

    # score principal
    score += 2 * ecart

    # cartes restantes (tempo) - plus important que dans la moyenne
    score += 1.0 * (len(joueur.main) - len(adversaire.main))

    # gestion du passage adverse
    if adversaire.a_passe:
        if ecart > 0:
            score += 20
            score += 15 * len(joueur.main)
            score -= ecart * 2
        else:
            # coût minimal pour gagner
            cout_min = min((c.valeur for c in joueur.main), default=999)
            deficit = abs(ecart)
            # si gagner est rentable
            if cout_min <= deficit:
                score += 15
            else:
                # mieux vaut préserver les cartes
                score += 10 * len(joueur.main)

    # sacrifice de manche : si on a déjà gagné une manche et qu'on est
    # très en retard avec peu de cartes, mieux vaut passer et économiser
    if joueur.manches_gagnees == 1 and ecart < -10 and len(joueur.main) > len(adversaire.main):
        score += 15  # inciter à passer pour garder l'avantage en cartes

    # avantage manches - penser long terme
    score += 10 * (joueur.manches_gagnees - adversaire.manches_gagnees)

    return score"""

def evaluation_difficile(etat, joueur_max):

    joueur = next(j for j in etat.joueurs if j.nom == joueur_max.nom)
    adversaire = next(j for j in etat.joueurs if j.nom != joueur_max.nom)

    score = 0

    # =====================================================
    # 1. TEMPO (AVANTAGE DE SCORE IMMÉDIAT)
    # =====================================================
    ecart = joueur.score_manche - adversaire.score_manche
    score += 2.0 * ecart

    # =====================================================
    # 2. RESSOURCES (CARDS = PUISSANCE FUTURE)
    # =====================================================
    diff_cartes = len(joueur.main) - len(adversaire.main)
    score += 1.2 * diff_cartes

    # =====================================================
    # 3. VALUE DES CARTES (EFFICIENCE)
    # =====================================================

    # coût total déjà investi dans la manche
    cout_joueur = sum(c.valeur for c in joueur.cartes_jouees)

    # on favorise la victoire avec peu de coût
    score -= 0.3 * cout_joueur

    # =====================================================
    # 4. GESTION DU PASS ADVERSAIRE (MOMENT CRITIQUE)
    # =====================================================
    if adversaire.a_passe:

        # CAS 1 : on gagne déjà
        if ecart > 0:

            # on veut arrêter immédiatement de dépenser
            score += 30  # victoire quasi assurée
            score += 5 * len(joueur.main)  # garder les cartes est crucial

            # pénalité de sur-investissement
            score -= 1.0 * ecart

        # CAS 2 : on perd malgré le pass adverse
        else:
            deficit = abs(ecart)
            # meilleure carte disponible
            meilleure_carte = min((c.valeur for c in joueur.main), default=999)

            # si on peut encore rattraper facilement
            if meilleure_carte <= deficit + 1:
                score += 10  # tenter de gagner la manche
            else:
                score += 15 * len(joueur.main)  # abandonner proprement

    # =====================================================
    # 5. LOGIQUE DE SACRIFICE DE MANCHE
    # =====================================================

    # si on a déjà gagné une manche (pression long terme)
    if joueur.manches_gagnees > adversaire.manches_gagnees:

        # si situation mauvaise dans cette manche
        if ecart < -8:
            score += 10  # incite à perdre proprement et économiser

        # si situation correcte
        elif ecart > 0:
            score += 5  # stabilisation

    # =====================================================
    # 6. AVANTAGE GLOBAL MATCH (LONG TERME)
    # =====================================================
    score += 15 * (joueur.manches_gagnees - adversaire.manches_gagnees)

    # =====================================================
    # 7. PETITE STABILISATION (évite égalités parfaites)
    # =====================================================
    score += 0.01 * len(joueur.main)

    return score