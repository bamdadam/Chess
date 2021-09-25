from abc import ABC, abstractmethod
from constants import BISHOP_MOVES, ROOK_MOVES, KNIGHT_MOVES, PAWN_MOVES, KING_MOVES


class Piece(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.moves = []

    def get_position(self):
        return self.x, self.y

    @abstractmethod
    def get_name(self):
        pass

    def find_moves_incremental(self, board):
        moves = []
        for move_type in self.moves:
            # print(move_type)
            for move in move_type:
                # print(type(move[0]))
                # print(self.x)
                # print(self.y)
                new_x = move[0] + self.x
                new_y = move[1] + self.y
                new_move = (new_x, new_y)
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board.get_piece(new_move) is None:
                        moves.append(new_move)
                        new_x += move[0]
                        new_y += move[1]
                        new_move = (new_x, new_y)
                    elif board.get_piece(new_move).color != self.color:
                        moves.append(new_move)
                        break
                    else:
                        break
        return moves

    def find_moves_spot(self, board):
        moves = []
        for move_type in self.moves:
            # print(move_type)
            for move in move_type:
                # print(move)
                new_x = move[0] + self.x
                new_y = move[1] + self.y
                new_move = (new_x, new_y)
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board.get_piece(new_move) is None:
                        moves.append(new_move)
                    elif board.get_piece(new_move).color != self.color:
                        moves.append(new_move)
        return moves

    def find_moves(self, board):
        if KNIGHT_MOVES in self.moves \
                or PAWN_MOVES in self.moves \
                or KING_MOVES in self.moves:
            return self.find_moves_spot(board)
        else:
            return self.find_moves_incremental(board)

    def move_piece(self, move):
        self.x = move[0]
        self.y = move[1]


class PieceFactory:
    @staticmethod
    def build_piece(piece_type: str, x, y, color):
        if piece_type == "PAWN":
            return Pawn(x=x, y=y, color=color)
        if piece_type == "ROOK":
            return Rook(x=x, y=y, color=color)
        if piece_type == "BISHOP":
            return Bishop(x=x, y=y, color=color)
        if piece_type == "KNIGHT":
            return Knight(x=x, y=y, color=color)
        if piece_type == "KING":
            return King(x=x, y=y, color=color)
        if piece_type == "QUEEN":
            return Queen(x=x, y=y, color=color)


class Pawn(Piece):
    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x=x, y=y, color=color)
        self.moves = []

    def get_name(self):
        return self.color[0] + "PA"


class Rook(Piece):
    def __init__(self, x, y, color):
        super(Rook, self).__init__(x=x, y=y, color=color)
        self.moves = [ROOK_MOVES]

    def get_name(self):
        return self.color[0] + "RO"


class Bishop(Piece):
    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x=x, y=y, color=color)
        self.moves = [BISHOP_MOVES]

    def get_name(self):
        return self.color[0] + "BI"


class Knight(Piece):
    def __init__(self, x, y, color):
        super(Knight, self).__init__(x=x, y=y, color=color)
        self.moves = [KNIGHT_MOVES]

    def get_name(self):
        return self.color[0] + "KN"


class Queen(Piece):
    def __init__(self, x, y, color):
        super(Queen, self).__init__(x=x, y=y, color=color)
        self.moves = []

    def get_name(self):
        return self.color[0] + "QU"


class King(Piece):
    def __init__(self, x, y, color):
        super(King, self).__init__(x=x, y=y, color=color)
        self.moves = []

    def get_name(self):
        return self.color[0] + "KI"
