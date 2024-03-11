from pieces import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from pprint import pprint
from game_logger import setup_logging
import logging
setup_logging()


class ChessBoard:
    """
    Represents the chess board, responsible for setting up the board and moving pieces.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.__board = [["-" for _ in range(8)] for _ in range(8)]
        self.__setup_pieces()
        self.__is_game_over = False
        self.logger.info("A new chess board has been created.")
        self.logger.info(f"Initial board state: \n{self}")

    def __setup_pieces_for_colour(self, colour, back_row):

        front_row = back_row + 1 if colour == "Black" else back_row - 1

        for col, piece_cls in enumerate([Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], start=0):
            self.logger.info(f"Setting up {colour} piece {piece_cls.__name__} at {(back_row, col)}")
            # Set up the main pieces on the back row
            self.__board[back_row][col] = piece_cls(colour, (back_row, col))
            # Set up pawns on the front row
            self.logger.info(f"Setting up {colour} Pawn at {(front_row, col)}")
            self.__board[front_row][col] = Pawn(colour, (front_row, col))

    def __setup_pieces(self):
        """
        Sets up the pieces on the board in their initial positions.
        """

        self.__setup_pieces_for_colour("Black", 0)
        self.__setup_pieces_for_colour("White", 7)

        # Ensure that your ChessBoard class has the necessary methods (get_piece_at_position and move_piece) implemented to support these operations. The move_piece method in ChessBoard should handle the logistics of updating the board's internal representation, such as setting the new position to the piece and the old position to a default empty state (like "-").

    def move_piece(self, from_piece, to_piece) -> bool:
        """
        Moves a piece from one position to another if the move is valid.

        Args:
            from_row: The row of the piece to be moved.
            from_col: The column of the piece to be moved.
            to_row: The row of the target position.
            to_col: The column of the target position.

        Returns:
            True if the move is valid and completed, False otherwise.
        """

        from_row, from_col = from_piece
        to_row, to_col = to_piece
        
        from_piece = self.get_piece_at_position(from_row, from_col)
        to_piece = self.get_piece_at_position(to_row, to_col)

        if isinstance(from_piece, Piece):
            if not isinstance(to_piece, Piece) or to_piece.colour != from_piece.colour:
                self.__board[to_row][to_col] = from_piece
                self.__board[from_row][from_col] = "-"
                from_piece.position = (to_row, to_col)  # Update piece's position
                self.logger.info(f"Current board state: \n{self}")
                return True
        return False
    
    def get_piece_at_position(self, row: int, col: int) -> Piece:
        """
        Returns the piece at the specified position.

        Args:
            row (int): The row of the piece.
            col (int): The column of the piece.

        Returns:
            Piece: The piece at the specified position.
        """
        return self.__board[row][col]

    def get_board(self) -> list:
        """
        Returns the current state of the board.

        Returns:
            The board state as a list of lists.
        """
        return self.__board

    def display(self) -> None:
        """
        Prints the board to the console.
        """
        print(str(self))

    def set_board(self, board: list) -> None:
        """
        Sets the board to a new state.

        Args:
            board (list): The new board state.
        """
        self.__board = board

    def move_puts_in_check(self, position, i, j, colour) -> bool:
        """
        Checks if a move puts the king in check.

        Args:
            position (tuple): The position of the piece to move.
            i (int): The row index of the target position.
            j (int): The column index of the target position.
            colour (str): The colour of the piece to move.

        Returns:
            bool: True if the move puts the king in check, False otherwise.
        """

        # Create a copy of the board
        board_copy = [row[:] for row in self.__board]
        # Move the piece to the target position
        board_copy[i][j] = board_copy[position[0]][position[1]]
        board_copy[position[0]][position[1]] = "-"
        # Check if the move puts the king in check
        return self.is_king_in_check(colour, board_copy)
    
    def is_king_in_check(self, colour: str, board: list) -> bool:
        """
        Checks if the king of the specified colour is in check.

        Args:
            colour (str): The colour of the king to check.
            board (list): The current state of the board.

        Returns:
            bool: True if the king is in check, False otherwise.
        """
        king_position = None
        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if isinstance(piece, King) and piece.colour == colour:
                    king_position = (i, j)
                    break
            if king_position:
                break
        if not king_position:
            raise ValueError(f"No {colour} king found on the board")
        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if isinstance(piece, Piece) and piece.colour != colour:
                    if piece.is_valid_move(king_position, self):
                        return True
        return False

    def has_legal_moves(self, colour: str, in_check: bool) -> bool:
        for row in self.__board:
            for piece in row:
                if isinstance(piece, Piece) and piece.colour == colour:
                    for i in range(8):
                        for j in range(8):
                            if piece.is_valid_move((i, j), self) and not self.move_puts_in_check(piece.position, *(i, j), colour):
                                return True
        return False

    def is_game_over(self) -> bool:
        """
        Checks if the game is over by checking if either side has no legal moves.

        Returns:
            bool: True if the game is over, False otherwise.
        """

        for colour in ["White", "Black"]:
            in_check = self.is_king_in_check(colour, self.__board)
            if not self.has_legal_moves(colour, in_check):
                return True
        return False

    def __str__(self) -> str:
        """
        Returns a string representation of the board with grid coordinates.
        Pieces are represented by their first letter and color (e.g., WR for White Rook),
        and all characters are uppercase for uniformity. Each board slot is 4 characters wide.

        Returns:
            str: The board state as a string with visual enhancements.
        """
        # Initial top border and column labels for clarity
        board_str = "\n"
        space = 29 * " "
        board_str += space + "    0    1    2    3    4    5    6    7\n" + space +  "  -----------------------------------------\n"
        
        # Generating each row with row numbers, making slots 4 chars wide
        for i, row in enumerate(self.__board, start=0):  # Reversed for correct orientation
            row_str = f"{i} |"
            for piece in row:
                if isinstance(piece, Piece):
                    # Construct symbol string from piece properties, keeping all uppercase
                    symbol = f"{piece.colour[0]}{piece.name[0]}".upper()
                    row_str += f" {symbol} |"
                else:
                    row_str += " -- |"
            board_str += space + row_str + f" {i}\n" + space +  "  -----------------------------------------\n"        
        # Adding bottom column labels for completeness
        board_str += space +  "    0    1    2    3    4    5    6    7\n"

        return board_str

    def __repr__(self) -> str:
        """
        Returns a string representation of the board.

        Returns:
            str: The board state as a string.
        """
        return self.__str__()