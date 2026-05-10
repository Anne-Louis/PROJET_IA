import unittest

from jeu.joueur import Joueur
from jeu.etatJeu import EtatJeu

from ia.evaluation import (
    evaluation_facile,
    evaluation_moyenne,
    evaluation_difficile
)


class TestEvaluations(unittest.TestCase):

    def setUp(self):
        self.j1 = Joueur("IA")
        self.j2 = Joueur("ADV")

        self.etat = EtatJeu(self.j1, self.j2)

    def test_evaluation_facile_positive(self):
        self.j1.score_manche = 10
        self.j2.score_manche = 5

        score = evaluation_facile(self.etat, self.j1)

        self.assertGreater(score, 0)

    def test_evaluation_facile_negative(self):
        self.j1.score_manche = 2
        self.j2.score_manche = 10

        score = evaluation_facile(self.etat, self.j1)

        self.assertLess(score, 0)

    def test_evaluation_moyenne_bonus_cartes(self):
        self.j1.main = self.j1.main[:8]
        self.j2.main = self.j2.main[:4]

        score = evaluation_moyenne(self.etat, self.j1)

        self.assertGreater(score, 0)

    def test_evaluation_difficile_pass_adverse(self):
        self.j1.score_manche = 15
        self.j2.score_manche = 10
        self.j2.a_passe = True

        score = evaluation_difficile(self.etat, self.j1)

        self.assertGreater(score, 20)

if __name__ == "__main__":
    unittest.main()