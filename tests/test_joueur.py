import unittest
from jeu.joueur import Joueur


class TestJoueur(unittest.TestCase):

    def test_jouer_carte(self):
        joueur = Joueur("Test")

        taille_main_depart = len(joueur.main)

        carte = joueur.main[0]
        valeur = carte.valeur

        joueur.jouer_carte(0)

        self.assertEqual(len(joueur.main), taille_main_depart - 1)
        self.assertEqual(joueur.score_manche, valeur)
        self.assertEqual(len(joueur.cartes_jouees), 1)

    def test_passer_manche(self):
        joueur = Joueur("Test")

        joueur.passer_manche()

        self.assertTrue(joueur.a_passe)

    def test_manche_suivante(self):
        joueur = Joueur("Test")

        joueur.score_manche = 15
        joueur.a_passe = True

        joueur.manche_suivante(True)

        self.assertEqual(joueur.score_manche, 0)
        self.assertFalse(joueur.a_passe)
        self.assertEqual(joueur.manches_gagnees, 1)


if __name__ == "__main__":
    unittest.main()