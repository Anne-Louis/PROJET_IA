import time
from collections import defaultdict
from statistics import mean

from jeu.joueur import Joueur
from jeu.etatJeu import EtatJeu

import ia.ia_facile as ia_facile
import ia.ia_moyenne as ia_moyenne
import ia.ia_difficile as ia_difficile


# =========================================================
# CONFIGURATION
# =========================================================

NB_PARTIES = 200


# =========================================================
# REGISTRE DES IA
# =========================================================

IA_REGISTRY = {
    "IA Facile": ia_facile,
    "IA Moyenne": ia_moyenne,
    "IA Difficile": ia_difficile,
}


# =========================================================
# STATISTIQUES
# =========================================================

stats_victoires = defaultdict(int)

# victoires détaillées par matchup
stats_matchups = defaultdict(int)

stats_temps = {
    "IA Facile": [],
    "IA Moyenne": [],
    "IA Difficile": []
}

stats_scores = {
    "IA Facile": {
        "min": [],
        "moy": [],
        "choisi": []
    },
    "IA Moyenne": {
        "min": [],
        "moy": [],
        "choisi": []
    },
    "IA Difficile": {
        "min": [],
        "moy": [],
        "choisi": []
    }
}


# =========================================================
# OUTILS
# =========================================================


def enregistrer_stats_ia(nom_ia, infos_debug, temps_execution):
    """
    infos_debug doit être un dictionnaire contenant :

    {
        "scores_possibles": [...],
        "score_choisi": float
    }
    """

    stats_temps[nom_ia].append(temps_execution)

    scores = infos_debug["scores_possibles"]

    if len(scores) > 0:
        stats_scores[nom_ia]["min"].append(min(scores))
        stats_scores[nom_ia]["moy"].append(mean(scores))

    stats_scores[nom_ia]["choisi"].append(
        infos_debug["score_choisi"]
    )


# =========================================================
# PARTIE IA VS IA
# =========================================================


def jouer_partie(ia1_nom, ia2_nom):

    joueur1 = Joueur(f"{ia1_nom} (J1)")
    joueur2 = Joueur(f"{ia2_nom} (J2)")

    etat = EtatJeu(joueur1, joueur2)

    ia1_module = IA_REGISTRY[ia1_nom]
    ia2_module = IA_REGISTRY[ia2_nom]

    while not etat.partie_terminee():

        while not etat.manche_terminee():

            joueur = etat.get_joueur_courant()

            # =====================================
            # JOUEUR 1
            # =====================================

            if joueur == joueur1:
                debut = time.perf_counter()

                action, infos_debug = ia1_module.choisir_action_debug(etat)

                fin = time.perf_counter()

                enregistrer_stats_ia(
                    ia1_nom,
                    infos_debug,
                    fin - debut
                )

            # =====================================
            # JOUEUR 2
            # =====================================

            else:
                debut = time.perf_counter()

                action, infos_debug = ia2_module.choisir_action_debug(etat)

                fin = time.perf_counter()

                enregistrer_stats_ia(
                    ia2_nom,
                    infos_debug,
                    fin - debut
                )

            etat.appliquer_action(action)

        etat.terminer_manche()

    # =====================================
    # ENREGISTREMENT VICTOIRE
    # =====================================

    if joueur1.manches_gagnees > joueur2.manches_gagnees:
        stats_victoires[f"{ia1_nom} (J1)"] += 1

        stats_matchups[
            f"{ia1_nom} (J1) vs {ia2_nom} (J2)"
        ] += 1

    elif joueur2.manches_gagnees > joueur1.manches_gagnees:
        stats_victoires[f"{ia2_nom} (J2)"] += 1

        stats_matchups[
            f"{ia2_nom} (J2) vs {ia1_nom} (J1)"
        ] += 1


# =========================================================
# TOURNOI COMPLET
# =========================================================


def lancer_tournoi():

    liste_ias = list(IA_REGISTRY.keys())

    for ia1 in liste_ias:
        for ia2 in liste_ias:

            print("\n====================================")
            print(f"{ia1} (J1) VS {ia2} (J2)")
            print("====================================")

            for partie in range(NB_PARTIES):
                print(f"Partie {partie + 1}/{NB_PARTIES}")
                jouer_partie(ia1, ia2)

    afficher_resultats()


# =========================================================
# AFFICHAGE RESULTATS
# =========================================================


def afficher_resultats():

    print("\n\n============================")
    print("RESULTATS TOURNOI")
    print("============================")

    # =====================================
    # VICTOIRES TOTALES
    # =====================================

    print("--- Victoires totales ---")

    for ia, nb in stats_victoires.items():
        print(f"{ia} : {nb} victoires")

    # =====================================
    # DETAILS PAR AFFRONTEMENT
    # =====================================

    print("--- Victoires par affrontement ---")

    for ia1 in IA_REGISTRY.keys():
        for ia2 in IA_REGISTRY.keys():

            cle_j1 = f"{ia1} (J1) vs {ia2} (J2)"
            cle_j2 = f"{ia2} (J2) vs {ia1} (J1)"

            v1 = stats_matchups.get(cle_j1, 0)
            v2 = stats_matchups.get(cle_j2, 0)

            print(f"{ia1} (J1) VS {ia2} (J2)")
            print(f"{ia1} : {v1} victoires")
            print(f"{ia2} : {v2} victoires")

    # =====================================
    # TEMPS MOYENS
    # =====================================

    print("\n--- Temps moyens par coup ---")

    for ia, temps in stats_temps.items():

        if len(temps) > 0:
            print(
                f"{ia} : {mean(temps):.6f} sec"
            )

    # =====================================
    # SCORES
    # =====================================

    print("\n--- Scores moyens observes ---")

    for ia, data in stats_scores.items():

        min_moy = mean(data["min"]) if data["min"] else 0
        moy_moy = mean(data["moy"]) if data["moy"] else 0
        choisi_moy = mean(data["choisi"]) if data["choisi"] else 0

        print(f"\n{ia}")
        print(f"Pire score moyen : {min_moy:.3f}")
        print(f"Score moyen des actions : {moy_moy:.3f}")
        print(f"Score choisi moyen : {choisi_moy:.3f}")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    lancer_tournoi()