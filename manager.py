from game import Chess
from user import Player


class Manager:
    def __init__(self, user1, user2, game: Chess):
        self.player1 = Player(user1, 1)
        self.player1.turn = True
        self.player2 = Player(user2, 2)
        self.player2.turn = False
        self.game = game

    def play_game(self):
        self.game.show_board()
        while True:
            # player 1 make a move
            self.do_a_move(player=self.player1)
            self.game.show_board()
            # check game end
            if self.check_game_end():
                break
            # player 2 make a move
            self.do_a_move(player=self.player2)
            self.game.show_board()
            # check game end
            if self.check_game_end():
                break

    def do_a_move(self, player):
        while True:
            piece_position, move = player.make_move()
            piece = self.game.board.get_piece(piece_position)
            if piece:
                if self.game.judge.process_move(piece=piece, board=self.game.board, move=move):
                    self.game.do_a_move(piece=piece, move=move)
                    break

    def check_game_end(self):
        game_over, winner = self.game.judge.is_game_over(self.game.board)
        if game_over:
            print(f"game is over {winner} won!!")
            return True

        # close clients and stuff
