# chess_game/pieces/queen.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class Queen(Piece):
    """
    Represents a queen in the chess game. Inherits from Piece.

    The Queen moves any number of squares horizontally, vertically, or
    diagonally.
    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new Queen. Inherits from Piece.

        Args:
            colour (str): The colour of the queen.
            position (tuple): The starting position of the queen.
        """
        super().__init__(colour, "Queen", position)

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the queen.

        Args:
            new_position (tuple): The proposed new position for the queen.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_queen_move_valid(self.position, new_position,
                                                 chess_board)
