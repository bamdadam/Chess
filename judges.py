import copy
from abc import ABC, abstractmethod

from board import ChessBoard
from pieces import Piece


class Judge(ABC):
    @abstractmethod
    def process_move(self, piece, board, move):
        pass

    @abstractmethod
    def is_game_over(self, board):
        pass


class ChessJudge(Judge):
    def __init__(self):
        pass

    def process_move(self, piece: Piece, board: ChessBoard, move):
        if move in self.movable_moves(piece, board):
            return True
        else:
            return False

    def is_game_over(self, board: ChessBoard):
        if self.is_king_check(board.get_king("BLACK"), board):
            if not self.can_any_piece_move("BLACK", board):
                return True, "WHITE"
        elif self.is_king_check(board.get_king("WHITE"), board):
            if not self.can_any_piece_move("WHITE", board):
                return True, "BLACK"
        else:
            return False, None

    def can_any_piece_move(self, color, board: ChessBoard):
        for piece in board.pieces:
            if piece.color == color:
                if len(self.movable_moves(piece, board)) != 0:
                    return True
        return False

    def threaten_moves(self, piece: Piece, board: ChessBoard):
        threaten_moves = piece.find_moves(board)
        return threaten_moves

    def movable_moves(self, piece: Piece, board: ChessBoard):
        threaten_moves = self.threaten_moves(piece, board)
        movable_moves = []
        for move in threaten_moves:
            c_board = copy.deepcopy(board)
            c_piece = c_board.get_piece(piece.get_position())
            c_piece.move_piece(move)
            c_king = c_board.get_king(c_piece.color)
            if not self.is_king_check(c_king, c_board):
                movable_moves.append(move)
        return movable_moves

    def is_king_check(self, king: Piece, board: ChessBoard):
        for piece in board.pieces:
            if piece.color != king.color and \
                    king.get_position() in self.threaten_moves(piece, board):
                return True
        return False
