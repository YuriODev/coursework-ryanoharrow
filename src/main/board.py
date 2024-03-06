from pieces import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from pprint import pprint


class ChessBoard:
    """
    This class represents the chess board. It is responsible for setting up the board and moving pieces.

    """
    


    def __init__(self):
        self.__board = [["-" for _ in range(8)] for _ in range(8)]
        for col in range(8):
            self.__board[1][col] = Pawn("b", "Pawn", self.__board)
        self.__board[0][0] = Rook("b", "Rook", self.__board)
        self.__board[0][7] = Rook("b", "Rook", self.__board)
        self.__board[0][2] = Bishop("b", "Bishop", self.__board)
        self.__board[0][5] = Bishop("b", "Bishop", self.__board)
        self.__board[0][1] = Knight("b", "Knight", self.__board)
        self.__board[0][6] = Knight("b", "Knight", self.__board)
        self.__board[0][4] = King("b", "King", self.__board)
        self.__board[0][3] = Queen("b", "Queen", self.__board)
        
        for col in range(8):
            self.__board[6][col] = Pawn("w", "Pawn", self.__board)
        self.__board[7][7] = Rook("w", "Rook", self.__board)
        self.__board[7][0] = Rook("w", "Rook", self.__board)
        self.__board[7][5] = Bishop("w", "Bishop", self.__board)
        self.__board[7][2] = Bishop("w", "Bishop", self.__board)
        self.__board[7][1] = Knight("w", "Knight", self.__board)
        self.__board[7][6] = Knight("w", "Knight", self.__board)
        self.__board[7][4] = King("w", "King", self.__board)
        self.__board[7][3] = Queen("w", "Queen", self.__board)

    def move_piece(self, from_row, from_col, to_row, to_col):
        """
        This method moves a piece from one position to another. It checks if the move is valid and if it is, it moves the piece to the new position.

        :param from_row: The row of the piece to be moved.
        :param
        :param to_row: The row of the position to move the piece to.
        :param to_col: The column of the position to move the piece to.
        :return: True if the move is valid and the piece is moved, False otherwise.
        
        """
        

        piece = self.__board[from_row][from_col]
        target_piece = self.__board[to_row][to_col]
        if isinstance(piece, Piece) and piece.is_valid_move(self.__board, from_row, from_col, to_row, to_col):
            if not (isinstance(target_piece, Piece) and target_piece.colour == piece.colour):
                self.__board[to_row][to_col] = piece
                self.__board[from_row][from_col] = "-"
                return True
        return False

    
    def get_board(self):
        return self.__board
    
    def check_collision(self, to_row, to_col):  
        pprint(self.__board)
        if self.__board[to_row][to_col] != "-":
            return True
    
    def set_board(self, new_board_state):
        for i in range(8):
            for j in range(8):
                self.__board[i][j] = new_board_state[i][j] 
        # self.display()

    def display(self):
        for i in range (8):
            for j in range (8):
                piece = self.__board[i][j]
                if isinstance(piece,Piece):
                    print (piece.name,end=" ")
                else:
                    print ("-", end=" ")
            print("")
    
    def is_game_over(self):
        count = 0
        for i in range(8):
            for j in range(8):
                try:
                    piece = self.__board[i][j]
                    if piece.name == "King":
                        count+=1
                except AttributeError:
                    pass
                
        return count