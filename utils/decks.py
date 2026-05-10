import json
from typing import List
from random import sample

from jeu.carte import Carte


def charger_cartes(fichier_json: str):
    """
    Charge les cartes depuis un fichier JSON.

    Args:
        fichier_json (str):
            Chemin vers le fichier JSON contenant les cartes.

    Returns:
        list[Carte]:
            Liste des cartes chargées.
    """

    with open(fichier_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    cartes = [
        Carte(c["nom"], c["valeur"], c["type"])
        for c in data
    ]

    return cartes


def creer_deck_joueur():
    """
    Crée un deck complet pour un joueur.

    Les cartes sont chargées depuis le fichier JSON
    puis copiées afin que chaque joueur possède
    son propre deck indépendant.

    Returns:
        list[Carte]:
            Liste des cartes du deck du joueur.
    """

    cartes = charger_cartes("utils/cartes.json")

    return [
        Carte(c.nom, c.valeur, c.type_carte)
        for c in cartes
    ]


def distribuer_cartes(deck: List[Carte]):
    """
    Distribue une main de départ aléatoire au joueur.

    Les cartes distribuées sont retirées du deck.

    Args:
        deck (list[Carte]):
            Deck du joueur.

    Returns:
        list[Carte]:
            Main de départ contenant 10 cartes.
    """

    main = sample(deck, 10)

    for carte in main:
        deck.remove(carte)

    return main