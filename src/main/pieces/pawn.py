# chess_game/pieces/pawn.py
from __future__ import annotations
from .piece import Piece
from .validator import MoveValidator


class Pawn(Piece):
    """
    Represents a pawn in the chess game. Inherits from Piece.

    The Pawn moves forward exactly one square, or optionally, two squares
    when on its starting square. The Pawn captures diagonally to the left
    or right.

    """

    def __init__(self, colour: str, position: tuple):
        """
        Initializes a new Pawn. Inherits from Piece.

        Args:
            colour (str): The colour of the pawn.
            position (tuple): The starting position of the pawn.
        """
        super().__init__(colour, "Pawn", position)
        self.__is_initial_move = True

    @property
    def is_initial_move(self):
        """
        Gets the initial move of the pawn.
        """
        return self.__is_initial_move
    
    @is_initial_move.setter
    def is_initial_move(self, value: bool):
        """
        Sets the initial move of the pawn.
        """
        self.__is_initial_move = value

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the pawn.

        Args:
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """

        return MoveValidator.is_pawn_move_valid(self.position, new_position,
                                                chess_board)
