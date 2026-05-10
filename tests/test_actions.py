import unittest
from jeu.action import Action

class TestAction(unittest.TestCase):

    def test_action_jouer(self):
        action = Action("jouer", 2)

        self.assertTrue(action.est_jouer())
        self.assertFalse(action.est_pass())
        self.assertEqual(action.index_carte, 2)

    def test_action_passer(self):
        action = Action("passer")

        self.assertTrue(action.est_pass())
        self.assertFalse(action.est_jouer())


if __name__ == "__main__":
    unittest.main()