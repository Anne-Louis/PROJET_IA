import json
from typing import List
from jeu.carte import Carte
from random import sample

def charger_cartes(fichier_json: str):
    with open(fichier_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    cartes = [Carte(c["nom"], c["valeur"], c["type"]) for c in data]
    return cartes

def creer_deck_joueur():
    cartes = charger_cartes("utils/cartes.json")
    return [Carte(c.nom, c.valeur, c.type_carte) for c in cartes]
    
def distribuer_cartes(deck: List[Carte]):
    main = sample(deck, 10) 
    for carte in main :
        deck.remove(carte)
    return main
