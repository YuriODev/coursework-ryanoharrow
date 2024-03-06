from pieces import Piece

class Utilities:
    def all_moves(self, board):
        self.moves = [[], []]
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if isinstance(piece, Piece):
                    for x in range(8):
                        for y in range(8):
                            if piece.is_valid_move(board, i, j, x, y) and not piece.check_friendly_collision(x, y):
                                if piece.colour == "w":
                                    self.moves[0].append((i, j, x, y))
                                elif piece.colour == "b":
                                    # print(f"Black piece {piece} at {i},{j} can move to {x},{y}")
                                    self.moves[1].append((i, j, x, y))
        return self.moves


