# chess_game/pieces/pawn.py
from .piece import Piece


class Pawn(Piece):
    """
    Represents a pawn in the chess game. Inherits from Piece.

    The Pawn moves straight forward one square, or optionally, two squares
    from its starting position, but it captures diagonally. Pawns can also
    perform a special move known as "en passant."
    """

    def __init__(self, color: str, position: tuple, board: list):
        super().__init__(color, "Pawn", position, board)

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
        if self._is_initial_move(new_position):
            # Check if the move is a forward move and the path is clear
            # or if the move is a diagonal capture
            return self._is_forward_move(new_position) and \
                   (self._is_empty(new_position) or
                    self._is_diagonal_capture(new_position))

        # Check if the move is a forward move and the path is clear
        elif self._is_forward_move(new_position):
            return self._is_empty(new_position)

        # Check if the move is a diagonal capture move and the piece at
        # the new position is the opposite color
        elif self._is_diagonal_capture(new_position):
            return self._is_opposite_color(new_position)
        return False

    def _is_forward_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a forward move.

        Args:
            new_position (tuple): The proposed new position for the pawn.

        Returns:
            bool: True if the move is a forward move, False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        if self.color == "White":
            return new_col == col and new_row == row - 1
        elif self.color == "Black":
            return new_col == col and new_row == row + 1
        return False

    def _is_diagonal_capture(self, new_position: tuple) -> bool:
        """
        Checks if the move is a diagonal capture move.

        Args:
            new_position (tuple): The proposed new position for the pawn.

        Returns:
            bool: True if the move is a diagonal capture move, False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        if self.color == "White":
            return new_row == row - 1 and \
                   (new_col == col - 1 or new_col == col + 1)
        elif self.color == "Black":
            return new_row == row + 1 and \
                   (new_col == col - 1 or new_col == col + 1)
        return False
