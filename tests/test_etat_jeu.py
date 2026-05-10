import unittest

from jeu.joueur import Joueur
from jeu.etatJeu import EtatJeu
from jeu.action import Action


class TestEtatJeu(unittest.TestCase):

    def setUp(self):
        self.j1 = Joueur("J1")
        self.j2 = Joueur("J2")
        self.etat = EtatJeu(self.j1, self.j2)

    def test_changement_joueur(self):
        joueur_depart = self.etat.get_joueur_courant()

        self.etat.changer_joueur()

        self.assertNotEqual(
            joueur_depart,
            self.etat.get_joueur_courant()
        )

    def test_actions_possibles(self):
        actions = self.etat.actions_possibles()

        self.assertEqual(
            len(actions),
            len(self.j1.main) + 1
        )

    def test_appliquer_action_jouer(self):
        score_depart = self.j1.score_manche

        action = Action("jouer", 0)
        self.etat.appliquer_action(action)

        self.assertGreater(
            self.j1.score_manche,
            score_depart
        )

    def test_appliquer_action_pass(self):
        action = Action("passer")
        self.etat.appliquer_action(action)

        self.assertTrue(self.j1.a_passe)

    def test_manche_terminee(self):
        self.j1.a_passe = True
        self.j2.a_passe = True

        self.assertTrue(self.etat.manche_terminee())


    def test_copie_independante(self):
        copie = self.etat.copier()
        copie.joueurs[0].score_manche = 999

        self.assertNotEqual(
            self.etat.joueurs[0].score_manche,
            copie.joueurs[0].score_manche
        )

    def test_copie_main(self):
        copie = self.etat.copier()

        self.assertEqual(
            len(self.etat.joueurs[0].main),
            len(copie.joueurs[0].main)
        )

        self.assertIsNot(
            self.etat.joueurs[0].main[0],
            copie.joueurs[0].main[0]
        )

    def test_copie_cartes_jouees(self):
        self.j1.jouer_carte(0)
        copie = self.etat.copier()

        self.assertEqual(
            len(self.j1.cartes_jouees),
            len(copie.joueurs[0].cartes_jouees)
        )

        self.assertIsNot(
            self.j1.cartes_jouees[0],
            copie.joueurs[0].cartes_jouees[0]
        )

    def test_modifier_copie_ne_change_pas_original(self):
        copie = self.etat.copier()

        taille_originale = len(self.etat.joueurs[0].main)

        copie.joueurs[0].jouer_carte(0)

        self.assertEqual(
            len(self.etat.joueurs[0].main),
            taille_originale
        )

    def test_copie_joueur_courant(self):
        self.etat.joueur_courant = 1

        copie = self.etat.copier()

        self.assertEqual(
            copie.joueur_courant,
            1
        )

    def test_copie_numero_manche(self):
        self.etat.numero_manche = 3

        copie = self.etat.copier()

        self.assertEqual(
            copie.numero_manche,
            3
        )

    def test_simulation_action_sur_copie(self):
        copie = self.etat.copier()

        action = Action("jouer", 0)

        copie.appliquer_action(action)

        self.assertEqual(
            self.etat.joueurs[0].score_manche,
            0
        )

if __name__ == "__main__":
    unittest.main()