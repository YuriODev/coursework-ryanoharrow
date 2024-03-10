# chess_game/pieces/knight.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class Knight(Piece):
    """
    Represents a knight in the chess game. Inherits from Piece.

    The Knight moves in an L-shape, two squares in one direction and one
    square in a perpendicular direction.
    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new Knight. Inherits from Piece.

        Args:
            colour (str): The colour of the knight.
            position (tuple): The starting position of the knight.
        """
        super().__init__(colour, "Knight", position)

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the knight.

        Args:
            new_position (tuple): The proposed new position for the knight.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_knight_move_valid(self.position, new_position,
                                                  chess_board)
