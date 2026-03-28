import tempCard
class tempDeck:
    def __init__(self):
        self.deck = [tempCard.tempCard()]
    
    def get_card(self, index):
        return self.deck[index]
    
    