# chess_game/pieces/knight.py
from .piece import Piece


class Knight(Piece):
    """
    Represents a knight in the chess game. Inherits from Piece.

    The Knight moves to any of the squares immediately adjacent to it that
    are not on the same rank, file, or diagonal. In other words, the knight
    moves two squares horizontally and one square vertically, or two squares
    vertically and one square horizontally.
    """

    def __init__(self, color: str, position: tuple, board: list):
        super().__init__(color, "Knight", position, board)

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Checks if a move is valid for the knight.

        Args:
            new_position (tuple): The proposed new position for the knight.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not self.is_move_within_bounds(new_position):
            return False

        # Check if the move is valid
        return self._is_L_shape_move(new_position) and \
            (self._is_empty(new_position) or
             self._is_opposite_color(new_position))

    def _is_L_shape_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is an L-shape move.

        Args:
            new_position (tuple): The proposed new position for the knight.

        Returns:
            bool: True if the move is an L-shape move, False otherwise.
        """
        row, col = self.position

        # All possible L-shape moves
        L_shape_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        return new_position in L_shape_moves
