# chess_game/pieces/bishop.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class Bishop(Piece):
    """
    Represents a bishop in the chess game. Inherits from Piece.

    The Bishop moves any number of squares diagonally.
    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new Bishop. Inherits from Piece.

        Args:
            colour (str): The colour of the bishop.
            position (tuple): The starting position of the bishop.
        """
        super().__init__(colour, "Bishop", position)

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the bishop.

        Args:
            new_position (tuple): The proposed new position for the bishop.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_bishop_move_valid(self.position, new_position,
                                                  chess_board)
