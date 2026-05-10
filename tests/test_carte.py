import unittest
from jeu.carte import Carte


class TestCarte(unittest.TestCase):

    def test_creation_carte(self):
        carte = Carte("Geralt", 15, "melee")

        self.assertEqual(carte.nom, "Geralt")
        self.assertEqual(carte.valeur, 15)
        self.assertEqual(carte.type_carte, "melee")


if __name__ == "__main__":
    unittest.main()