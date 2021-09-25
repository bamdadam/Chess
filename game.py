from board import ChessBoard
from judges import ChessJudge


class Chess:
    def __init__(self, judge: ChessJudge, board: ChessBoard):
        self.board = board
        self.judge = judge

    def do_a_move(self, piece, move):
        piece.move_piece(move)

    def show_board(self):
        for j_index, row in enumerate(self.board.board):
            for i_index, column in enumerate(row):
                piece = self.board.get_piece((i_index, self.board.size - 1 - j_index))
                if piece:
                    print(piece.get_name() + ' ', end='')
                else:
                    print("EMP ", end='')
            print()

