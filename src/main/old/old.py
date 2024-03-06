import pygame as pg
import sys
import time
import copy

board = [
    ["bRook", "bKnight", "bBishop", "bQueen", "bKing", "bBishop", "bKnight", "bRook"] if i == 0 else
    ["bPawn"] * 8 if i == 1 else
    ["wPawn"] * 8 if i == 6 else
    ["wRook", "wKnight", "wBishop", "wQueen", "wKing", "wBishop", "wKnight", "wRook"] if i == 7 else
    ["-"] * 8
    for i in range(8)
]

# This creates the constant that is the board.
# This board is used to represent the current chess state in the entirety of the code

go = "White"          
move_count = 0
w_moves = []
b_moves = []

# Variables to store crucical information about the chess game.
# "go" alternates between "White" and "Black" to indicate which player must play next.
# 

def convert_cc(cc):
  column = ord(cc[0].lower()) - ord('a')
  row = 7 - (int(cc[1]) - 1)
  return row, column

def cc_to_chess(row, col):
  column = chr(col + ord('a'))
  column = column.upper()
  row = 8 - row
  return f"{column}{row}"


def move(from_row,from_col,to_row,to_col):
  piece = board[from_row][from_col]
  board[to_row][to_col] = piece
  board[from_row][from_col] = '-'

def check_collision(to_row,to_col):
  if board[to_row][to_col] != "-":
    return True

def check_moves(from_row,from_col,to_row,to_col,piece):
    if piece[1:] == "Pawn":
      return check_pawn(from_row,from_col,to_row,to_col,piece)
  
    if piece[1:] == "Rook":
      return check_rook(from_row,from_col,to_row,to_col,piece)
  
    if piece[1:] == "Knight":
      return check_knight(from_row,from_col,to_row,to_col)
  
    if piece[1:] == "Bishop":
      return check_bishop(from_row,from_col,to_row,to_col,piece)
  
    if piece[1:] == "King":
      return check_king(from_row,from_col,to_row,to_col)
  
    if piece[1:] == "Queen":
      if check_rook(from_row,from_col,to_row,to_col,piece) == True\
      or check_bishop(from_row,from_col,to_row,to_col,piece) == True:
        return True
    return False

def check_pawn(from_row, from_col, to_row, to_col, piece):
  if board[from_row][from_col][0] != board[to_row][to_col][0]:
    if piece[0] == "w":
      if (check_collision(to_row, to_col)\
      and ((from_row - 1 == to_row) and (abs(from_col - to_col) == 1))):
        return True
      if from_row == 6 and from_col == to_col and from_row - 2 == to_row and not check_collision(to_row, to_col) and board[from_row - 1][from_col] == "-":
        return True
      if from_row - 1 == to_row and from_col == to_col\
      and not check_collision(to_row, to_col):
        return True
    elif piece[0] == "b":
      if (check_collision(to_row, to_col)\
      and ((from_row + 1 == to_row) and (abs(from_col - to_col) == 1))):
        return True
      if from_row == 1 and from_col == to_col\
      and from_row + 2 == to_row and not check_collision(to_row, to_col) and board[from_row+1][from_col] == "-":
        return True
      if from_row + 1 == to_row and from_col == to_col\
      and not check_collision(to_row, to_col):
        return True
  return False



def check_rook(from_row, from_col, to_row, to_col, piece):
  if board[from_row][from_col][0] != board[to_row][to_col][0]:
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
  

def check_bishop(from_row, from_col, to_row, to_col, piece):
  if board[from_row][from_col][0] != board[to_row][to_col][0]:
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

def check_king(from_row, from_col, to_row, to_col):
  if board[from_row][from_col][0] != board[to_row][to_col][0]:
    if (from_row - to_row == 1 or from_row - to_row == -1) and from_col == to_col:
      return True
    elif (from_col - to_col == 1 or from_col - to_col == -1) and from_row == to_row:
      return True
    elif from_row - to_row == 1 or from_row - to_row == -1\
    and (from_col - to_col == 1 or from_col - to_col == -1):
      return True
    else:
      return False

def check_knight(from_row, from_col, to_row, to_col):
  if board[from_row][from_col][0] != board[to_row][to_col][0]:
    if ((from_row + 2 == to_row or from_row - 2 == to_row) and
      (from_col + 1 == to_col or from_col - 1 == to_col)) or\
      ((from_col + 2 == to_col or from_col - 2 == to_col) and
      (from_row + 1 == to_row or from_row - 1 == to_row)):
      return True
  return False 
  

def all_moves():
  white_moves = []
  black_moves = []
  white_all_moves = []
  black_all_moves = []

  for i in range (8):
    for j in range (8):
      if board[i][j] != "-":
        piece = board[i][j]
        for x in range (8):
          for y in range (8):
            if check_moves(i,j,x,y,piece):
              if piece[0] == "w":
                white_moves.append((x,y))
                white_all_moves.append((i,j,x,y))
              elif piece[0] == "b":
                black_moves.append((x,y))
                black_all_moves.append((i,j,x,y))
  try:
    black_all_moves.remove((0,0,0,1))
    black_all_moves.remove((0,7,0,6))
  except ValueError:
    pass
  return [white_moves,black_moves,white_all_moves,black_all_moves]

def get_king_pos(go):
  for i in range (8):
    for j in range (8):
      if board[i][j] == go[0].lower()+"King":
        return (i,j)


# pieceScore = {"King": 1000, "Queen": 10, "Rook": 5, "Bishop": 3, "Knight": 3,"Pawn":1}


def minimax(depth, isMaximizingPlayer):
  global board
  if depth == 0:
      return evaluate()

  if isMaximizingPlayer: 
    maxEval = float('-inf')
    best_move = None
    for potential in all_moves()[3]:  
      copied_board = [row[:] for row in board]
      move(potential[0],potential[1],potential[2],potential[3])
      # captured_piece = board[potential[2]][potential[3]]
      eval, _ = minimax(depth - 1, False)
      board = copied_board
      if eval > maxEval:
        maxEval = eval
        best_move = potential
    return maxEval, best_move
  else:  
    minEval = float('inf')
    for potential in all_moves()[2]:  
      copied_board = [row[:] for row in board]
      move(potential[0],potential[1],potential[2],potential[3])
      # captured_piece = board[potential[2]][potential[3]]
      eval, _ = minimax(depth - 1, True)
      board = copied_board
      if eval < minEval:
        minEval = eval
    return minEval, None

def game_over():
  if w_king_missing():
    return True, "Black wins! "
  if b_king_missing():
    return True, "White wins! "
  return False, ""

def w_king_missing():
  for row in board:
    if "wKing" in row:
      return False
  return True

def b_king_missing():
  for row in board:
    if "bKing" in row:
      return False
  return True

def generate_moves(position,go):
  moves = []
  if go == "Black":
    player = 3
  else:
    player = 2
    
  for i in all_moves()[player]:
    if (i[0],i[1]) == position:
      moves.append((i[2],i[3]))

  return moves
    

def evaluate():
  score = 0

  for i in range(8):
    for j in range (8):
      if board[i][j][0] == "w":
        score -= pieceScore[board[i][j][1:]]
      elif board[i][j][0] == "b":
        score += pieceScore[board[i][j][1:]]

  return score, None


def eval_all_moves(depth,maxPlayer):
  for position in all_moves()[3]:
    return minimax((position[0],position[1]),depth,maxPlayer)

pg.init()

WIDTH = HEIGHT = 400
SIZE = WIDTH / 8
GREEN = (175,183,170)
WHITE = (255, 242, 227)

clock = pg.time.Clock()
max_fps = 15

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ChessAI")


import pygame as pg

# Load images only once, outside the display_board function
IMAGES = {
    "wPawn": pg.image.load("images/wP.png"),
    "bPawn": pg.image.load("images/bP.png"),
    "bBishop": pg.image.load("images/bB.png"),
    "wBishop": pg.image.load("images/wB.png"),
    "wKnight": pg.image.load("images/wKn.png"),
    "bKnight": pg.image.load("images/bKn.png"),
    "bKing": pg.image.load("images/bK.png"),
    "wKing": pg.image.load("images/wK.png"),
    "wRook": pg.image.load("images/wR.png"),
    "bRook": pg.image.load("images/bR.png"),
    "bQueen": pg.image.load("images/bQ.png"),
    "wQueen": pg.image.load("images/wQ.png")
}

def display_board(window, board, SIZE):
    for i in range(8):
        for j in range(8):
            piece = board[j][i]
            color = WHITE if (i + j) % 2 == 0 else GREEN
            pg.draw.rect(window, color, (i * SIZE, j * SIZE, SIZE, SIZE))

            if piece != '-':
                image = IMAGES[piece]
                window.blit(image, (i * SIZE, j * SIZE))


class Move:                #Allows move undoing.
  def __init__ (self):
    self.__stack = []

  def getStack(self):
    return self.__stack

  def addToStack(self, board):
    self.__stack.append(copy.deepcopy(board))

  def prevBoard(self):
    return self.__stack.pop(len(self.__stack) - 1)


print("")
print("Welcome to ChessAI, a chess game that gets more difficult as you play better!")
print("Please enter moves in the format <letter><number> i.e A2")
print("Take the king to win. ")
print("Good luck! ")
print("")

run = True
game_is_over, winner = game_over()
game = Move()
display_board(window, board, SIZE)
pg.display.update() 

while run and not game_is_over:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False

    if event.type == pg.MOUSEBUTTONDOWN:
      print("Test")
  
  ###run here
  if (go == "Black"):
    print("AI is thinking... ")
    
    
    if evaluate()[0] < -5:
      depth = 2
    elif evaluate()[0] < -10:
      depth = 3
    else:
      depth = 1

    
    score, ai_move = minimax(depth,True)
    if ai_move is not None:
      from_row, from_col, to_row, to_col = ai_move
      
      from_ai = cc_to_chess(from_row, from_col)
      to_ai = cc_to_chess(to_row, to_col)

    print("AI moves from",from_ai,"to",to_ai,)
    print("Difficulty set to:",depth)
    move(from_row,from_col,to_row,to_col)
    
    game_is_over, winner = game_over()
    if game_is_over:
        break

    go = "White"
    
  if (go == "White"):
    opos = str(input("Move: "))
    tpos = str(input("To: "))
    opos = "E2"
    tpos = "E4"
    from_row, from_col = convert_cc(opos)
    to_row, to_col = convert_cc(tpos)
    piecef = board[from_row][from_col]
    if check_moves(from_row, from_col, to_row, to_col, piecef) and piecef[0] == "w":
      game.addToStack(board)
      move(from_row, from_col, to_row, to_col)
      w_moves.append((from_row,from_col,to_row,to_col))
      
      undo = input("Undo move?(Y/N) ")
      
      if undo == "Y":
        prev_board = game.prevBoard()
        if prev_board is not None:
          board = prev_board
          go = "White"
      else:
        go = "Black"
      
      game_is_over, winner = game_over()
      if game_is_over:
          break
        
    display_board(window, board, SIZE)
    pg.display.update() 
    clock.tick(max_fps)
      
print (winner)
  

pg.quit()
sys.exit()