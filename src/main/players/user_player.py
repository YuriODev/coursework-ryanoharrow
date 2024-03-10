from .player import Player


class UserPlayer(Player):
    def __init__(self, colour):
        super().__init__(colour)
    
    def make_move(self, board):
        # Get user input to make a move.
        # Update the board state.
        pass
