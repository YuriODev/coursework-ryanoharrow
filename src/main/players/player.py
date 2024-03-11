from abc import ABC, abstractmethod
import logging
from game_logger import setup_logging

setup_logging()


class Player(ABC):
    def __init__(self, colour):
        self.__colour = colour
        self.__taken_pieces = []
        self.__chosen_piece = None
        self.__chosen_square = None
        self.__last_move = None
        self.__all_moves = []
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(f"Player {colour} created")

    @property
    def colour(self):
        return self.__colour
    
    @property
    def taken_pieces(self):
        return self.__taken_pieces
    
    @property
    def chosen_piece(self):
        return self.__chosen_piece
    
    @property
    def chosen_square(self):
        return self.__chosen_square
    
    @chosen_square.setter
    def chosen_square(self, value):
        self.__chosen_square = value

    
    @property
    def last_move(self):
        return self.__last_move
    
    @property
    def all_moves(self):
        return self.__all_moves
    
    @chosen_piece.setter
    def chosen_piece(self, value):
        self.__chosen_piece = value

    @last_move.setter
    def last_move(self, value):
        self.__last_move = value

    @all_moves.setter
    def all_moves(self, value):
        self.__all_moves = value

    @abstractmethod
    def make_move(self, board: list):
        self.logger.info(f"Player {self.__colour} made a move")
    
    def move_piece(self, from_pos, to_pos):
        """
        Moves a piece on the board and updates the game state.

        Args:
            from_pos (tuple): The current position of the piece to move.
            to_pos (tuple): The destination position for the piece.
        """
        # Retrieve the piece object from the board
        piece = self.__board.get_piece_at_position(*from_pos)
        if piece and to_pos in piece:
            # Move the piece on the board
            self.__board.move_piece(*from_pos, *to_pos)
            self.logger.info(f"Moved {piece} from {from_pos} to {to_pos}")
            
            # Reset selected piece and possible moves
            self.selected_piece = None
            self.possible_moves = []
        else:
            self.logger.warning(f"Invalid move attempted from {from_pos} to {to_pos}")

    def take_piece(self, piece):
        self.__taken_pieces.append(piece)

    def __str__(self):
        return f"Player {self.__colour}"

    def __repr__(self):
        return f"Player {self.__colour}"
