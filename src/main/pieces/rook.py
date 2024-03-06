# chess_game/pieces/rook.py
from .piece import Piece


class Rook(Piece):
    """
    Represents a rook in the chess game. Inherits from Piece.

    The Rook moves straight forward one square, or optionally, two squares
    from its starting position, but it captures diagonally. Rooks can also
    perform a special move known as "en passant."
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

        # Check if the move is valid
        if self._is_vertical_move(new_position) or \
                self._is_horizontal_move(new_position):
            return self._is_empty(new_position) or \
                self._is_opposite_color(new_position)

        return False

    def _is_vertical_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a vertical move.

        Args:
            new_position (tuple): The proposed new position for the rook.

        Returns:
            bool: True if the move is a vertical move, False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        return new_col == col and new_row != row

    def _is_horizontal_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a horizontal move.

        Args:
            new_position (tuple): The proposed new position for the rook.

        Returns:
            bool: True if the move is a horizontal move, False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        return new_row == row and new_col != col
