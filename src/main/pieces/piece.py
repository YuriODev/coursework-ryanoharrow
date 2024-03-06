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
        self.is_initial_position = True

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

    def _is_initial_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is the piece's initial move.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is the piece's initial move, False
                  otherwise.
        """
        return self.is_initial_position

    def _is_forward_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a forward move.

        Args:
            new_position (tuple): The proposed new position for the piece.

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

        row, col = self.position
        new_row, new_col = new_position
        return abs(new_row - row) == abs(new_col - col)

    def _is_diagonal_capture(self, new_position: tuple) -> bool:
        """
        Checks if the move is a diagonal capture move.

        Args:
            new_position (tuple): The proposed new position for the piece.

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
        
        _, col = self.position
        _, new_col = new_position
        return new_col == col

    def _is_horizontal_move(self, new_position: tuple) -> bool:
        """
        Checks if the move is a horizontal move.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a horizontal move, False otherwise.
        """
        
        row, _ = self.position
        new_row, _ = new_position
        return new_row == row

    def _is_opposite_color(self, new_position: tuple) -> bool:
        """
        Checks if the piece at the new position is the opposite color.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the piece at the new position is the opposite
                  color, False otherwise.
        """
        row, col = new_position
        return isinstance(self.board[row][col], Piece) and \
            self.board[row][col].color != self.color

    def _is_empty(self, new_position: tuple) -> bool:
        """
        Checks if the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the rook.

        Returns:
            bool: True if the new position is empty, False otherwise.
        """
        row, col = new_position
        return not isinstance(self.board[row][col], Piece)

    def _is_enemy_king(self, new_position: tuple) -> bool:
        """
        Checks if the piece at the new position is the enemy king.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the piece at the new position is the enemy king,
                  False otherwise.
        """
        pass

    def _is_empty_diagonal_path(self, new_position: tuple) -> bool:
        """
        Checks if the diagonal path to the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the _.

        Returns:
            bool: True if the diagonal path to the new position is empty,
                  False otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        row_diff = new_row - row
        col_diff = new_col - col
        row_dir = 1 if row_diff > 0 else -1
        col_dir = 1 if col_diff > 0 else -1

        # Check if the path is empty
        for i in range(1, abs(row_diff)):
            if not self._is_empty((row + i * row_dir, col + i * col_dir)):
                return False
        return True

    def _is_empty_horizontal_path(self, new_position: tuple) -> bool:
        """
        Checks if the horizontal path to the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the piecce.

        Returns:
            bool: True if the horizontal path to the new position is empty,
                  False otherwise.
        """
        row, col = self.position
        _, new_col = new_position
        col_diff = new_col - col
        col_dir = 1 if col_diff > 0 else -1

        # Check if the path is empty
        for i in range(1, abs(col_diff)):
            if not self._is_empty((row, col + i * col_dir)):
                return False
        return True

    def _is_empty_vertical_path(self, new_position: tuple) -> bool:
        """
        Checks if the vertical path to the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the vertical path to the new position is empty,
                  False otherwise.
        """
        row, col = self.position
        new_row, __dict__ = new_position
        row_diff = new_row - row
        row_dir = 1 if row_diff > 0 else -1

        # Check if the path is empty
        for i in range(1, abs(row_diff)):
            if not self._is_empty((row + i * row_dir, col)):
                return False
        return True

    def _is_empty_path(self, new_position: tuple) -> bool:
        """
        Checks if the path to the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the queen.

        Returns:
            bool: True if the path to the new position is empty, False
                  otherwise.
        """
        row, col = self.position
        new_row, new_col = new_position
        row_diff = new_row - row
        col_diff = new_col - col

        # Check if the move is a diagonal move
        if abs(row_diff) == abs(col_diff):
            return self._is_empty_diagonal_path(new_position)
        # Check if the move is a horizontal move
        elif row_diff == 0:
            return self._is_empty_horizontal_path(new_position)
        # Check if the move is a vertical move
        elif col_diff == 0:
            return self._is_empty_vertical_path(new_position)
        return False

    def _is_rook_move_valid(self, new_position: tuple) -> bool:
        """
        Checks if the move is valid for the rook.

        Args:
            new_position (tuple): The proposed new position for the rook.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return self._is_horizontal_move(new_position) or \
            self._is_vertical_move(new_position)

    def _is_bishop_move_valid(self, new_position: tuple) -> bool:
        """
        Checks if the move is valid for the bishop.

        Args:
            new_position (tuple): The proposed new position for the bishop.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return self._is_diagonal_move(new_position)

    def _is_queen_move_valid(self, new_position: tuple) -> bool:
        """
        Checks if the move is valid for the queen.

        Args:
            new_position (tuple): The proposed new position for the queen.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return self._is_rook_move_valid(new_position) or \
            self._is_bishop_move_valid(new_position)

    def move(self, new_position: tuple) -> None:
        """
        Moves the piece to the new position.

        Args:
            new_position (tuple): The new position of the piece.
        """
        self.position = new_position
        self.is_initial_position = False

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
