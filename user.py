class User:
    def __init__(self, username):
        self.username = username
        self.rank = 0


class Player:
    def __init__(self, username, player_number):
        self.username = username
        self.turn = False
        self.number = player_number

    def make_move(self):
        print(f"player {self.number} make a move:")
        piece_position, dest_position = input().split('-')
        piece_position_x, piece_position_y = piece_position.strip().split(',')
        dest_position_x, dest_position_y = dest_position.strip().split(',')
        return (int(piece_position_x), int(piece_position_y)), (int(dest_position_x), int(dest_position_y))
