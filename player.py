import tempDeck
import tempCard
HAND_SIZE = 5
class player:
    """Classe représentant le joueur"""
    def __init__(self):
        self.deck = tempDeck.tempDeck()
        self.hand = tempCard.tempCard() #temporaire le temps d'avoir les vrais deck
        self.is_playing = True

    def play_card(self, card, row, game_board):
        game_board.add_card(row, card)
        game_board.update_score()
        self.hand = None

    def get_card(self, index):
        self.hand.get_card(index)
    
    def pass_turn(self):
        self.is_playing = False