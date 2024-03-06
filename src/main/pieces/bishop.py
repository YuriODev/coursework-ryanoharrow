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
        if self._is_diagonal_move(new_position):
            return self._is_empty_path(new_position) or \
                self._is_opposite_color(new_position)
        return False

    def _is_diagonal_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a diagonal move.

        Args:
            new_position (tuple): The proposed new position for the bishop.

        Returns:
            bool: True if the move is a diagonal move, False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        return abs(new_row - row) == abs(new_col - col)

    def _is_empty_path(self, new_position: tuple) -> bool:
        """
        Checks if the path to the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the bishop.

        Returns:
            bool: True if the path to the new position is empty, False
                  otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position

        # Determine the direction of the move
        dx = 1 if new_row > row else -1

        # Determine the direction of the move
        dy = 1 if new_col > col else -1
        row, col = row + dx, col + dy

        # Check if the path to the new position is empty
        while (row, col) != new_position:
            # If the path is not empty, return False
            if not self._is_empty((row, col)):
                return False

            # Move to the next position
            row, col = row + dx, col + dy
        return True
