class row:
    """Classe représentant une ligne du plateau"""


    def __init__(self):
        self.score = 0
        self.cards = []


    def get_Score(self):
        return self.score
    

    def add_card(self, tempcard):
        self.cards.append(tempcard)
        self.score += tempcard.value
    
    def clear_row(self):
        self.score= 0
        self.cards = []