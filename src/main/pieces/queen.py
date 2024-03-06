# chess_game/pieces/queen.py
from .piece import Piece


class Queen(Piece):
    """
    Represents a queen in the chess game. Inherits from Piece.

    The Queen moves any number of squares horizontally, vertically, or
    diagonally.

    """

    def __init__(self, colour: str, position: tuple, board: list):
        super().__init__(colour, "Queen", position, board)

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Checks if a move is valid for the pawn.

        Args:
            new_position (tuple): The proposed new position for the pawn.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not self.is_move_within_bounds(new_position):
            return False

        # Check if the move is valid
        return self._is_queen_move_valid(new_position)
