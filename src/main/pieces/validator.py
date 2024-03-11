from __future__ import annotations
from board import ChessBoard


class MoveValidator:
    """
    Validates moves for different chess pieces.
    """

    @staticmethod
    def is_move_within_bounds(position: tuple) -> bool:
        """
        Checks if a given position is within the bounds of the chess board.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if the position is within bounds, False otherwise.
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    @staticmethod
    def is_new_cell_empty(new_position: tuple,
                          chess_board: ChessBoard) -> bool:
        """
        Checks if the new position is empty.

        Args:
            new_position (tuple): The proposed new position for the piece.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the new position is empty, False otherwise.
        """
        board = chess_board
        row, col = new_position
        return board[row][col] == "-"

    @staticmethod
    def is_opposite_colour(position: tuple, new_position: tuple,
                           chess_board: ChessBoard) -> bool:
        """
        Checks if the piece at the new position is the opposite colour.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the piece at the new position is the opposite
                  colour, False otherwise.
        """
        row, col = new_position
        board = chess_board
        current_piece = board[position[0]][position[1]]
        target_piece = board[row][col]

        # Ensure there is a piece at the new position and it's of the 
        # opposite colour

        if isinstance(target_piece, str):
            return False

        return target_piece.colour != current_piece.colour

    @staticmethod
    def is_basically_valid_move(position: tuple, new_position: tuple,
                                chess_board: ChessBoard) -> bool:
        """
        Checks if a move is basically valid.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is basically valid, False otherwise.
        """

        return MoveValidator.is_move_within_bounds(new_position) and \
            MoveValidator.is_new_cell_empty(new_position, chess_board) or \
            MoveValidator.is_opposite_colour(position,
                                             new_position,
                                             chess_board)

    @staticmethod
    def is_vertical_move(position: tuple, new_position: tuple) -> bool:
        """
        Checks if the move is a vertical move.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a vertical move, False otherwise.
        """
        _, col = position
        _, new_col = new_position
        return new_col == col

    @staticmethod
    def is_horizontal_move(position: tuple, new_position: tuple) -> bool:
        """
        Checks if the move is a horizontal move.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a horizontal move, False otherwise.
        """
        row, _ = position
        new_row, _ = new_position
        return new_row == row

    @staticmethod
    def is_diagonal_move(position: tuple, new_position: tuple) -> bool:
        """
        Checks if the move is a diagonal move.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is a diagonal move, False otherwise.
        """
        row, col = position
        new_row, new_col = new_position
        return abs(new_row - row) == abs(new_col - col)

    @staticmethod
    def is_path_clear(position: tuple, new_position: tuple,
                      chess_board: ChessBoard) -> bool:
        """
        Checks if the path to the new position is empty.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the path to the new position is empty, False
                  otherwise.
        """
        row, col = position
        new_row, new_col = new_position
        row_diff = new_row - row
        col_diff = new_col - col
        
        # Determine direction of movement

        # Horizontal step
        row_step = (row_diff // abs(row_diff)) if row_diff != 0 else 0
        
        # Vertical step
        col_step = (col_diff // abs(col_diff)) if col_diff != 0 else 0

        steps = max(abs(row_diff), abs(col_diff)) - 1  # Exclude the final cell

        for step in range(1, steps + 1):
            current_row = row + step * row_step
            current_col = col + step * col_step
            if chess_board.get_board()[current_row][current_col] != "-": 
                return False  # Path is blocked

        return True  # Path is clear

    @staticmethod
    def is_L_shape_move(position: tuple, new_position: tuple) -> bool:
        """
        Checks if the move is an L-shaped move.

        Args:
            position (tuple): The current position of the piece.
            new_position (tuple): The proposed new position for the piece.

        Returns:
            bool: True if the move is an L-shaped move, False otherwise.
        """
        row_diff = abs(new_position[0] - position[0])
        col_diff = abs(new_position[1] - position[1])

        return (row_diff == 2 and col_diff == 1) or \
            (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_knight_move_valid(position: tuple, new_position: tuple,
                             chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the knight.

        Args:
            position (tuple): The current position of the knight.
            new_position (tuple): The proposed new position for the knight.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_basically_valid_move(position, new_position,
                                                     chess_board) and \
            MoveValidator.is_L_shape_move(position, new_position)

    @staticmethod
    def is_bishop_move_valid(position: tuple, new_position: tuple,
                             chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the bishop.

        Args:
            position (tuple): The current position of the bishop.
            new_position (tuple): The proposed new position for the bishop.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_basically_valid_move(position, new_position,
                                                     chess_board) and \
            MoveValidator.is_diagonal_move(position, new_position) and \
            MoveValidator.is_path_clear(position, new_position, chess_board)

    @staticmethod
    def is_rook_move_valid(position: tuple, new_position: tuple,
                           chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the rook.

        Args:
            position (tuple): The current position of the rook.
            new_position (tuple): The proposed new position for the rook.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return MoveValidator.is_basically_valid_move(position, new_position,
                                                     chess_board) and \
            (MoveValidator.is_vertical_move(position, new_position) or \
                MoveValidator.is_horizontal_move(position, new_position)) and \
            MoveValidator.is_path_clear(position, new_position, chess_board)

    @staticmethod
    def is_queen_move_valid(position: tuple, new_position: tuple,
                            chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the queen.

        Args:
            position (tuple): The current position of the queen.
            new_position (tuple): The proposed new position for the queen.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (MoveValidator.is_bishop_move_valid(position, new_position,
                                                   chess_board) or \
                MoveValidator.is_rook_move_valid(position, new_position,
                                                 chess_board))

    @staticmethod
    def is_forward_pawn_move_valid(position: tuple, new_position: tuple,
                                   chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for a forward pawn move.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        row, col = position
        new_row, new_col = new_position
        board = chess_board

        # Check if the new cell is empty
        if not MoveValidator.is_new_cell_empty(new_position, chess_board):
            return False

        # Check if the move is within the bounds of the board
        if not MoveValidator.is_move_within_bounds(new_position):
            return False
        
        # Check for the pawn's initial two-square move
        if MoveValidator.is_initial_pawn_move_valid(position, new_position, 
                                                    chess_board):
            return True

        # Check if the move is a one-square forward move
        if board[row][col].colour == "White":
            return new_col == col and new_row == row - 1
        else:
            return new_col == col and new_row == row + 1

    @staticmethod
    def is_pawn_capture_valid(position: tuple, new_position: tuple,
                              chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for a pawn capture.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        row, col = position
        new_row, new_col = new_position
        board = chess_board

        # Check if the move is within the bounds of the board
        if not MoveValidator.is_move_within_bounds(new_position):
            return False

        # Check if the new cell is occupied by an opponent's piece
        if MoveValidator.is_new_cell_empty(new_position, chess_board):
            return False

        # Check if the pawn is capturing diagonally
        if board[row][col].colour == "White":
            return abs(new_col - col) == 1 and new_row == row - 1
        else:
            return abs(new_col - col) == 1 and new_row == row + 1

    @staticmethod
    def is_pawn_en_passant_valid(position: tuple, new_position: tuple,
                                 chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for a pawn en passant capture.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Implementation details go here
        pass

    @staticmethod
    def is_pawn_promotion_valid(position: tuple, new_position: tuple) -> bool:
        """
        Checks if the move is valid for a pawn promotion.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Implementation details go here
        pass

    @staticmethod
    def is_initial_pawn_move_valid(position: tuple, new_position: tuple,
                                   chess_board: ChessBoard) -> bool:
        """
        Checks if the pawn's initial two-square forward move is valid.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the initial two-square move is valid, False
            otherwise.
        """
        row, col = position
        new_row, new_col = new_position
        board = chess_board

        if col != new_col:
            return False  # The move must be in the same column

        if board[row][col].colour == "White" and \
           row == 6 and new_row == row - 2:
            # White pawn initial two-square move
            return MoveValidator.is_new_cell_empty((row-1, col),
                                                   chess_board) and \
                MoveValidator.is_new_cell_empty(new_position, chess_board)
        
        if board[row][col].colour == "Black" and \
           row == 1 and new_row == row + 2:
            # Black pawn initial two-square move
            return MoveValidator.is_new_cell_empty((row+1, col),
                                                   chess_board) and \
                MoveValidator.is_new_cell_empty(new_position, chess_board)

        return False

    @staticmethod
    def is_pawn_move_valid(position: tuple, new_position: tuple,
                           chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the pawn.

        Args:
            position (tuple): The current position of the pawn.
            new_position (tuple): The proposed new position for the pawn.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (MoveValidator.is_forward_pawn_move_valid(position, new_position,
                                                         chess_board) or \
                MoveValidator.is_pawn_capture_valid(position, new_position,
                                                   chess_board))

    @staticmethod
    def is_king_move_valid(position: tuple, new_position: tuple,
                           chess_board: ChessBoard) -> bool:
        """
        Checks if the move is valid for the king.

        Args:
            position (tuple): The current position of the king.
            new_position (tuple): The proposed new position for the king.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """

        row, col = position
        new_row, new_col = new_position
        row_diff = abs(new_row - row)
        col_diff = abs(new_col - col)

        # The king can move exactly one square horizontally, vertically, or
        # diagonally.
        if row_diff > 1 or col_diff > 1:
            return False
        
        return MoveValidator.is_basically_valid_move(position, new_position,
                                                     chess_board)

    @staticmethod
    def get_possible_moves(piece: Piece, chess_board: ChessBoard) -> list:
        """
        Returns a list of possible moves for a piece.

        Args:
            piece (Piece): The piece for which to calculate possible moves.
            chess_board (ChessBoard): The current state of the board.

        Returns:
            list: A list of possible moves for the piece.
        """
        possible_moves = []
        for row in range(8):
            for col in range(8):
                new_position = (row, col)
                if piece.is_valid_move(new_position, chess_board):
                    possible_moves.append(new_position)
        return possible_moves
