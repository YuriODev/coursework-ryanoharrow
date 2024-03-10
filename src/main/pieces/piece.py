# chess_game/pieces/piece.py
from __future__ import annotations
import logging
from game_logger import setup_logging
from .validator import MoveValidator

setup_logging()


class Piece:
    """
    Base class for all chess pieces.

    Attributes:
        name (str): The name of the piece (e.g., 'Pawn', 'Rook').
        colour (str): The colour of the piece ('White' for white, 'Black'
                     for black).
        position (tuple): The current position of the piece on the board.

    """

    def __init__(self, colour: str, name: str, position: tuple):
        """
        Initializes a new Piece.

        Args:
            colour (str): The colour of the piece.
            name (str): The name of the piece.
            position (tuple): The starting position of the piece.
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.__colour = colour
        self.__name = name
        self.__position = position
        self.__is_initial_position = True
        self.__posible_moves = []
        self.logger.info(f"Creating a new {colour} {name} at {position}")

    @property
    def colour(self):
        """
        Gets the colour of the piece.
        """
        return self.__colour

    @property
    def name(self):
        """
        Gets the name of the piece.
        """
        return self.__name

    @property
    def position(self):
        """
        Gets the position of the piece.
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
        Sets the position of the piece.
        """
        self.__position = value

    @property
    def is_initial_position(self):
        """
        Gets the initial position of the piece.
        """
        return self.__is_initial_position

    @is_initial_position.setter
    def is_initial_position(self, value: bool):
        """
        Sets the initial position of the piece.
        """
        self.__is_initial_position = value

    def is_valid_move(self, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if a move is valid for the piece.

        Args:
            new_position (tuple): The proposed new position for the piece.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        self.logger.info(f"Checking if move of {self} to {new_position} is"
                         "valid")

        return MoveValidator.is_basically_valid_move(self.position,
                                                     new_position,
                                                     chess_board)

    def get_possible_moves(self, chess_board: ChessBoard) -> list:
        """
        Returns a list of possible moves for the piece.

        Args:
            chess_board (ChessBoard): The current state of the board.

        Returns:
            list: A list of possible moves for the piece.
        """
        self.__posible_moves = MoveValidator.get_possible_moves(self, chess_board)
        self.logger.info(f"Possible moves for {self} at {self.position}: {self.__posible_moves}")

        return self.__posible_moves


    def __str__(self):
        """
        Returns a string representation of the piece.
        """
        
        return f"{self.colour}{self.name}"

    def __repr__(self):
        """
        Returns a string representation of the piece.
        """
        return str(self)

    def __contains__(self, item: tuple):
        """
        Checks if a move is valid for the piece.
        """
        return item in self.__posible_moves
