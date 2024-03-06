from board import ChessBoard
from utilities import Utilities
from pieces import Piece
import copy
chess_board = ChessBoard()
util = Utilities()

class AI:
    def __init__(self, board):
        self.chess_board = board
        self.pieceScore = {
            "King": 1000,
            "Queen": 10,
            "Rook": 5,
            "Bishop": 3,
            "Knight": 3,
            "Pawn": 1
            }
    
    def evaluate(self, board):
        score = 0
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if isinstance(piece, Piece):
                    piece_value = self.pieceScore[piece.__class__.__name__]
                    if piece.colour == "w":
                        score -= piece_value
                    elif piece.colour == "b":
                        score += piece_value
                        
                if self.is_capture_move(i, j, piece, board):
                    capture_bonus = 5 
                    score += capture_bonus if piece.colour == "b" else -capture_bonus

        return score, None

    def is_capture_move(self, row, col, piece, board):
        if not isinstance(piece, Piece):
            return False

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board[new_row][new_col]
                    if isinstance(target_piece, Piece) and target_piece.colour != piece.colour:
                        return True
        return False




    def minimax(self, depth, isMaximisingPlayer, alpha=float('-inf'), beta=float('inf')):
        original_board = copy.deepcopy(self.chess_board.get_board())

        if depth == 0:
            eval_score = self.evaluate(original_board)
            return eval_score

        if isMaximisingPlayer:
            maxEval = float('-inf')
            best_move = None
            for potential in util.all_moves(original_board)[0]:
                self.chess_board.set_board(copy.deepcopy(original_board))
                self.chess_board.move_piece(potential[0], potential[1], potential[2], potential[3])
                eval, _ = self.minimax(depth - 1, False, alpha, beta)
            
                if eval > maxEval:
                    maxEval = eval
                    best_move = potential

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            self.chess_board.set_board(original_board) 
            return maxEval, best_move

        else:
            minEval = float('inf')
            best_move = None
            for potential in util.all_moves(original_board)[1]:  
                from_row, from_col, to_row, to_col = potential
                piece = original_board[to_row][to_col]
                if piece != '-' and piece.colour == "b":
                    continue 

                self.chess_board.set_board(copy.deepcopy(original_board)) 
                self.chess_board.move_piece(from_row, from_col, to_row, to_col)
                eval, _ = self.minimax(depth - 1, True, alpha, beta)
                
                if eval < minEval:
                    minEval = eval
                    best_move = potential

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            self.chess_board.set_board(original_board) 
            return minEval, best_move
