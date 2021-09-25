from constants import chess_board_size, Initial_White_Piece_Setup, white_color, black_color
from pieces import Piece, PieceFactory
from tile import Tile


class ChessBoard:
    def __init__(self):
        self.size = chess_board_size
        self.board = [
            [Tile(white_color) if i % 2 == 0 else Tile(black_color) for i in range(0, self.size)]
            for j in range(0, 8)
        ]
        self.pieces = []
        self.black_king = None
        self.white_king = None
        self.set_pieces()

    def set_pieces(self):
        for piece_setup in Initial_White_Piece_Setup:
            piece_type = piece_setup[0]
            piece_x_pos = piece_setup[1]
            piece_y_pos = piece_setup[2]
            print(piece_type)
            white_piece = PieceFactory.build_piece(piece_type=piece_type, x=piece_x_pos,
                                                   y=piece_y_pos, color=white_color)
            self.pieces.append(white_piece)
            black_piece = PieceFactory.build_piece(piece_type=piece_type, x=piece_x_pos,
                                                   y=self.size - 1 - piece_y_pos, color=black_color)
            self.pieces.append(black_piece)
            if piece_type == "KING":
                self.white_king = white_piece
                self.black_king = black_piece

    def get_piece(self, position):
        x_pos = position[0]
        y_pos = position[1]
        for piece in self.pieces:
            if x_pos == piece.x and y_pos == piece.y:
                return piece
        return None

    def get_king(self, color):
        if color == "WHITE":
            return self.white_king
        else:
            return self.black_king
