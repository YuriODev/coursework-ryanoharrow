from pieces import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from pprint import pprint


class ChessBoard:
    """
    Represents the chess board, responsible for setting up the board and moving pieces.
    """

    def __init__(self):
        self.__board = [["-" for _ in range(8)] for _ in range(8)]
        self.__setup_pieces()

    def __setup_pieces_for_colour(self, colour, row):
        for col, piece_cls in enumerate([Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], start=0):
            self.__board[row][col] = piece_cls(colour, (row, col), self.__board)
            self.__board[row + 1][col] = Pawn(colour, (row + 1, col), self.__board)

    def __setup_pieces(self):
        """
        Sets up the pieces on the board in their initial positions.
        """

        self.__setup_pieces_for_colour("Black", 0)
        self.__setup_pieces_for_colour("White", 6)

    def move_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
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
        piece = self.__board[from_row][from_col]
        if isinstance(piece, Piece) and piece.is_valid_move((to_row, to_col)):
            target_piece = self.__board[to_row][to_col]
            if not isinstance(target_piece, Piece) or target_piece.colour != piece.colour:
                self.__board[to_row][to_col] = piece
                self.__board[from_row][from_col] = "-"
                piece.position = (to_row, to_col)  # Update piece's position
                return True
        return False

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
        for row in self.__board:
            print(' '.join([piece.name[0] if isinstance(piece, Piece) else "-" for piece in row]))
    
    def is_game_over(self) -> bool:
        """
        Checks if the game is over (if one or both kings are missing).

        Returns:
            True if the game is over, False otherwise.
        """
        self.display()
        kings_count = sum(1 for row in self.__board for piece in row if isinstance(piece, King))
        return kings_count < 2
