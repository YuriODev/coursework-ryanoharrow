# chess_game/pieces/pawn.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class King(Piece):
    """
    Represents a king in the chess game. Inherits from Piece.

    The King moves one square in any direction, horizontally, vertically,
    or diagonally.
    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new King. Inherits from Piece.

        Args:
            colour (str): The colour of the king.
            position (tuple): The starting position of the king.
        """
        super().__init__(colour, "King", position)

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the king.

        Args:
            new_position (tuple): The proposed new position for the king.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_king_move_valid(self.position, new_position,
                                                chess_board)
