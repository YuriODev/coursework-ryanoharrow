# chess_game/pieces/rook.py
from .piece import Piece


class Rook(Piece):
    """
    Represents a rook in the chess game. Inherits from Piece.

    The Rook moves any number of squares horizontally or vertically, forward
    or backward, through any number of unoccupied squares.
    """

    def __init__(self, color: str, position: tuple, board: list):
        super().__init__(color, "Rook", position, board)

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Checks if a move is valid for the rook.

        Args:
            new_position (tuple): The proposed new position for the rook.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not self.is_move_within_bounds(new_position):
            return False

        # Check if the move is horizontal or vertical and the path is clear
        return self._is_rook_move_valid(new_position)
