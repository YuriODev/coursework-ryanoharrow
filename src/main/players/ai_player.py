from .player import Player


class AIPlayer(Player):
    def __init__(self, colour, algorithm, depth=3):
        super().__init__(colour)
        self.algorithm = algorithm  # AI algorithm, e.g., minimax
        self.depth = depth

    def make_move(self, board):
        _, best_move = self.algorithm.minimax(depth=self.depth, 
                                              is_maximizing_player=True)
        if best_move:
            from_pos = (best_move[0], best_move[1])
            to_pos = (best_move[2], best_move[3])
            # Now use from_pos and to_pos to make the move on the board
            board.move_piece(from_pos, to_pos)  # Assuming this method exists on the board
            return True  # Indicate that a move was made
        return False  # Indicate that no move was made
