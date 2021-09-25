Initial_White_Piece_Setup = [
    ('ROOK', 0, 0),
    ('KNIGHT', 1, 0),
    ('BISHOP', 2, 0),
    ('QUEEN', 3, 0),
    ('KING', 4, 0),
    ('BISHOP', 5, 0),
    ('KNIGHT', 6, 0),
    ('ROOK', 7, 0),
    ('PAWN', 0, 1),
    ('PAWN', 1, 1),
    ('PAWN', 2, 1),
    ('PAWN', 3, 1),
    ('PAWN', 4, 1),
    ('PAWN', 5, 1),
    ('PAWN', 6, 1),
    ('PAWN', 7, 1)
]

chess_board_size = 8
white_color = "WHITE"
black_color = "BLACK"

BISHOP_MOVES = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ROOK_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
KNIGHT_MOVES = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
QUEEN_MOVES = []
KING_MOVES = []
PAWN_MOVES = []

