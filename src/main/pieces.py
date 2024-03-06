from pprint import pprint

class Piece:
    def __init__(self, colour, name, board):
        self.colour = colour
        self.name = name
        self.__board = board
        
    def is_valid_move(self):
        pass

    def check_friendly_collision(self, to_row, to_col):
        if isinstance(self.__board[to_row][to_col], Piece):
            if self.colour == self.__board[to_row][to_col].colour:
                print (self.colour,self.name, "collision with", self.colour, self.__board[to_row][to_col].name, "at", to_row, to_col)
                return True
        return False

    def check_collision(self, to_row, to_col):
        pprint(self.__board)

        if self.__board[to_row][to_col] != "-":
            return True
        
    def __repr__(self):
        return self.__class__.__name__

class Pawn(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            return False
        if self.colour == "w":
            if (self.check_collision(to_row, to_col)\
            and ((from_row - 1 == to_row) and (abs(from_col - to_col) == 1))):
                return True
            if from_row == 6 and from_col == to_col and from_row - 2 == to_row and board[from_row - 1][from_col] == "-":
                return True
            if from_row - 1 == to_row and from_col == to_col\
            and not self.check_collision(to_row, to_col):
                return True
        
        elif self.colour == "b":
            if (self.check_collision(to_row, to_col)\
            and ((from_row + 1 == to_row) and (abs(from_col - to_col) == 1))):
                return True
            if from_row == 1 and from_col == to_col\
            and from_row + 2 == to_row and board[from_row+1][from_col] == "-":
                return True
            if from_row + 1 == to_row and from_col == to_col\
            and not self.check_collision(to_row, to_col):
                return True
        
        return False
    
class Rook(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            return False
        if from_row == to_row and from_col != to_col:
            min_col = min(from_col, to_col)
            max_col = max(from_col, to_col)
            for col in range(min_col + 1, max_col):  
                if board[from_row][col] != '-':
                    return False
            return True
            
        elif from_col == to_col and from_row != to_row:
            min_row = min(from_row, to_row)
            max_row = max(from_row, to_row)
            for row in range(min_row + 1, max_row):  
                if board[row][from_col] != '-':
                    return False
            return True
            
        return False
  
class Bishop(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            return False
        if (to_row - from_row) == (to_col - from_col)\
        or (to_row - from_row) == -(to_col - from_col):
            if to_row > from_row:
                j = 1
            else:
                j=-1
            if to_col > from_col:
                i=1
            else:
                i=-1
        
            cur_row = from_row + j
            cur_col = from_col + i
      
            while cur_row != to_row and cur_col != to_col:
                if board[cur_row][cur_col] != '-':
                    return False
                cur_row += j
                cur_col += i
  
            return True

class Knight(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            return False
        if ((from_row + 2 == to_row or from_row - 2 == to_row) and
        (from_col + 1 == to_col or from_col - 1 == to_col)) or\
        ((from_col + 2 == to_col or from_col - 2 == to_col) and
        (from_row + 1 == to_row or from_row - 1 == to_row)):
            return True
        return False 

class King(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            print(f"Cant move here {(to_row, to_col)}")
            return False
        
        if (from_row - to_row == 1 or from_row - to_row == -1) and from_col == to_col:
            return True
        elif (from_col - to_col == 1 or from_col - to_col == -1) and from_row == to_row:
            return True
        elif from_row - to_row == 1 or from_row - to_row == -1\
        and (from_col - to_col == 1 or from_col - to_col == -1):
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, colour, name, board):
        super().__init__(colour, name, board)

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        if self.check_friendly_collision(to_row, to_col):
            return False
        if Bishop.is_valid_move(self, board, from_row, from_col, to_row, to_col)\
        or Rook.is_valid_move(self, board, from_row, from_col, to_row, to_col):
                return True
        return False