# chess_game/pieces/piece.py

class Piece:
    """
    Base class for all chess pieces.

    Attributes:
        color (str): The color of the piece ('w' for white, 'b' for black).
        name (str): The name of the piece (e.g., 'Pawn', 'Rook').
        position (tuple): The current position of the piece on the board.
        board (list): A reference to the board's current state.
    """

    def __init__(self, color: str, name: str, position: tuple, board: list):
        """
        Initializes a new Piece.

        Args:
            color (str): The color of the piece.
            name (str): The name of the piece.
            position (tuple): The starting position of the piece.
            board (list): A reference to the board's current state.
        """
        self.color = color
        self.name = name
        self.position = position
        self.board = board

    def is_move_within_bounds(self, position: tuple) -> bool:
        """
        Checks if a given position is within the bounds of the chess board.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if the position is within bounds, False otherwise.
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def is_valid_move(self, new_position: tuple) -> bool:
        """
        Placeholder method to be overridden by subclasses to check if a move
        is valid.

        Args:
            new_position (tuple): The proposed new position of the piece.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        pass
