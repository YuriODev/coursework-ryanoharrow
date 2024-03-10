from board import ChessBoard
from utilities import Utilities
from pieces import Piece
# from pieces import Piece

import copy

util = Utilities()  # Utilities class instance


class AI:
    def __init__(self, chess_board: ChessBoard):
        self.chess_board = chess_board
        self.piece_score = {
            "King": 1000,
            "Queen": 10,
            "Rook": 5,
            "Bishop": 3,
            "Knight": 3,
            "Pawn": 1
        }
    
    def evaluate(self, board: list) -> tuple:
        """
        Evaluates the score of the current board state.

        Args:
            board (list): The chess board state.

        Returns:
            tuple: A tuple containing the score and the best move.
        """
        score = 0
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if isinstance(piece, Piece):
                    piece_value = self.piece_score[piece.__class__.__name__]
                    if piece.colour == "White":
                        score -= piece_value
                    elif piece.colour == "Black":
                        score += piece_value
                        
                if self.is_capture_move(i, j, piece, board):
                    capture_bonus = 5 
                    score += capture_bonus if piece.colour == "Black" else -capture_bonus

        return score, None

    def is_capture_move(self, row: int, col: int, piece: Piece, board: list) -> bool:
        """
        Checks if a move is a capture move.

        Args:
            row (int): The row index of the piece.
            col (int): The column index of the piece.
            piece (Piece): The piece object.
            board (list): The chess board state.

        Returns:
            bool: True if the move is a capture move, False otherwise.
        """
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

    def minimax(self, depth: int, is_maximizing_player: bool, alpha: float = float('-inf'), beta: float = float('inf')) -> tuple:
        """
        Implements the minimax algorithm to find the best move.

        Args:
            depth (int): The depth of the search tree.
            is_maximizing_player (bool): True if the current player is the maximizing player, False otherwise.
            alpha (float): The alpha value for alpha-beta pruning.
            beta (float): The beta value for alpha-beta pruning.

        Returns:
            tuple: A tuple containing the evaluation score and the best move.
        """
        original_board = copy.deepcopy(self.chess_board.get_board())

        if depth == 0:
            eval_score = self.evaluate(original_board)
            return eval_score

        if is_maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for potential in util.all_moves(original_board)[0]:
                self.chess_board.set_board(copy.deepcopy(original_board))
                self.chess_board.move_piece(potential[0], potential[1], potential[2], potential[3])
                eval, _ = self.minimax(depth - 1, False, alpha, beta)
            
                if eval > max_eval:
                    max_eval = eval
                    best_move = potential

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            self.chess_board.set_board(original_board) 
            return max_eval, best_move

        else:
            min_eval = float('inf')
            best_move = None
            for potential in util.all_moves(original_board)[1]:  
                from_row, from_col, to_row, to_col = potential
                piece = original_board[to_row][to_col]
                if piece != '-' and piece.colour == "b":
                    continue 

                self.chess_board.set_board(copy.deepcopy(original_board))
                self.chess_board.move_piece(from_row, from_col, to_row, to_col)
                eval, _ = self.minimax(depth - 1, True, alpha, beta)
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = potential

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            self.chess_board.set_board(original_board) 
            return min_eval, best_move
