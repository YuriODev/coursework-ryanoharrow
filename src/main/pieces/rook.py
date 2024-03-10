# chess_game/pieces/rook.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class Rook(Piece):
    """
    Represents a rooke in the chess game. Inherits from Piece.

    The Rooke moves any number of squares horizontally or vertically.
    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new Rooke. Inherits from Piece.

        Args:
            colour (str): The colour of the rooke.
            position (tuple): The starting position of the rooke.
        """
        super().__init__(colour, "Rook", position)

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the rooke.

        Args:
            new_position (tuple): The proposed new position for the rooke.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_rook_move_valid(self.position, new_position,
                                                chess_board)
