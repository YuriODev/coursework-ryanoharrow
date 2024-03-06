# chess_game/pieces/piece.py

class Piece:
    """
    Base class for all chess pieces.

    Attributes:
        color (str): The color of the piece ('White' for white, 'Black'
                     for black).
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

    def _is_initial_move(self, new_position: tuple, direction: int) -> bool:
        """
        Checks if the move is the piece's initial move.

        Args:
            new_position (tuple): The proposed new position for the piece.
            direction (int): The direction the piece is moving.

        Returns:
            bool: True if the move is the piece's initial move, False
                  otherwise.
        """
        pass

    def _is_forward_move(self, new_position: tuple, direction: int) -> bool:
        """
        Checks if the move is a forward move.

        Args:
            new_position (tuple): The proposed new position for the piece.
            direction (int): The direction the piece is moving.

        Returns:
            bool: True if the move is a forward move, False otherwise.
        """
        pass

    def _is_diagonal_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a diagonal move.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a diagonal move, False otherwise.
        """
        pass

    def _is_diagonal_capture(self, new_position: tuple, direction: int) -> bool:
        """
        Checks if the move is a diagonal capture move.

        Args:
            new_position (tuple): The proposed new position for the piece.
            direction (int): The direction the piece is moving.

        Returns:
            bool: True if the move is a diagonal capture move, False otherwise.
        """
        pass

    def _is_vertical_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a vertical move.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a vertical move, False otherwise.
        """
        pass

    def _is_horizontal_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a horizontal move.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a horizontal move, False otherwise.
        """
        pass

    def _is_opposite_color(self, new_position: tuple) -> bool:
        """
        Checks if the piece at the new position is the opposite color.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the piece at the new position is the opposite
                  color, False otherwise.
        """
        pass

    def _is_same_color(self, new_position: tuple) -> bool:
        """
        Checks if the piece at the new position is the same color.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the piece at the new position is the same color,
                  False otherwise.
        """
        pass

    def __str__(self) -> str:
        """
        Returns the string representation of the piece.

        Returns:
            str: The string representation of the piece.
        """
        return f"{self.color[0]}{self.name[0]}"

    def __repr__(self) -> str:
        """
        Returns the string representation of the piece.

        Returns:
            str: The string representation of the piece.
        """

        return self.__class__.__name__
