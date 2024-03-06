# chess_game/pieces/pawn.py
from .piece import Piece


class King(Piece):
    """
    Represents a king in the chess game. Inherits from Piece.

    The King moves one square in any direction, horizontally, vertically,
    or diagonally.
    """

    def __init__(self, colour: str, position: tuple, board: list):
        super().__init__(colour, "King", position, board)

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Checks if a move is valid for the king.

        Args:
            new_position (tuple): The proposed new position for the king.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not self.is_move_within_bounds(new_position):
            return False

        # Check if the move is valid
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])
        return (row_diff == 1 or col_diff == 1) and \
               (self._is_empty(new_position) or
                self._is_opposite_colour(new_position))
