# chess_game/pieces/bishop.py
from .piece import Piece


class Bishop(Piece):
    """
    Represents a bishop in the chess game. Inherits from Piece.

    The Bishop moves any number of squares diagonally.
    """

    def __init__(self, color: str, position: tuple, board: list):
        super().__init__(color, "Bishop", position, board)

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Checks if a move is valid for the bishop.

        Args:
            new_position (tuple): The proposed new position for the bishop.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not self.is_move_within_bounds(new_position):
            return False

        # Check if the move is valid
        return self._is_bishop_move_valid(new_position)
