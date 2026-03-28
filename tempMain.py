import board
import tempCard
import player
def tempMain():
    game_board = board.board()
    game_board.update_score()
    print("Player 1 total score:", game_board.player1_total_score)
    print("Player 2 total score:", game_board.player2_total_score)
    card = tempCard.tempCard()
    game_board.add_card(game_board.player1_row1, card)
    game_board.update_score()
    print("Player 1 total score:", game_board.player1_total_score)
    print("Player 2 total score:", game_board.player2_total_score)
    game_board.clear_row(game_board.player1_row1)
    print("Player 1 total score:", game_board.player1_total_score)
    print("Player 2 total score:", game_board.player2_total_score)
    player1 = player.player()
    player1.play_card(player1.hand, game_board.player1_row1, game_board)
    print("Player 1 total score:", game_board.player1_total_score)
    print("Player 2 total score:", game_board.player2_total_score)
    print(player1.hand)

tempMain()