import jeu.row as row
class board: 
    """Classe permettant de représenter le plateau de jeu"""
    
    """Initialise le plateau """
    def __init__(self):
        self.player1_row1 = row.row()
        self.player1_row2 = row.row()
        self.player1_row3 = row.row()
        self.player2_row1 = row.row()
        self.player2_row2 = row.row()
        self.player2_row3 = row.row()
        self.player1_total_score = [0,0,0] #Le score du joueur 1 par ligne
        self.player2_total_score = [0,0,0] #Le score du joueur 2 par ligne

    def update_score(self):
        self.player1_total_score = [self.player1_row1.get_Score(), self.player1_row2.get_Score(), self.player1_row3.get_Score()]
        self.player2_total_score = [self.player2_row1.get_Score(), self.player2_row2.get_Score(), self.player2_row3.get_Score()]
    
    def add_card(self, row, card):
        row.add_card(card)

    def clear_row(self, row):
        row.clear_row()
        self.update_score()