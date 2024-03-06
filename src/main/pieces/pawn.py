# chess_game/pieces/pawn.py
from .piece import Piece


class Pawn(Piece):
    """
    Represents a pawn in the chess game. Inherits from Piece.

    The Pawn moves straight forward one square, or optionally, two squares
    from its starting position, but it captures diagonally. Pawns can also
    perform a special move known as "en passant."
    """

    def __init__(self, color, position, board):
        super().__init__(color, "Pawn", position, board)

    def is_valid_move(self, new_position):
        """
        Determines if a move is valid for the pawn, taking into account its
        unique movement and capture rules.

        Args:
            new_position (tuple): The proposed new position for the pawn.

        Returns:
            bool: True if the move is valid according to pawn rules, False otherwise.
        """
        current_row, current_col = self.position
        new_row, new_col = new_position
        # Pawns move up for 'w' and down for 'b'
        direction = 1 if self.color == 'b' else -1
        start_row = 1 if self.color == 'b' else 6

        # Move forward one square
        if (new_col == current_col and
                new_row == current_row + direction and
                self.board[new_row][new_col] == "-"):
            return True

        # Initial move: move forward two squares
        if (current_row == start_row and
                new_col == current_col and
                new_row == current_row + 2 * direction and
                self.board[current_row + direction][current_col] == "-" and
                self.board[new_row][new_col] == "-"):
            return True

        # Capture diagonally
        if (new_row == current_row + direction and
                abs(new_col - current_col) == 1):
            target = self.board[new_row][new_col]
            if isinstance(target, Piece) and target.color != self.color:
                return True

        return False
