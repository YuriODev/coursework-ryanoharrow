import logging
from game_logger import setup_logging
import pygame
from players import UserPlayer, AIPlayer
from pieces import Piece

setup_logging()


class Game:
    def __init__(self, ui, user_player, ai_player, board):
        self.ui = ui
        self.user_player = user_player
        self.ai_player = ai_player
        self.board = board
        self.game_running = True
        self.current_player = user_player
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("A new game has been created.")

    def get_square_from_mouse(pos, cell_size=100):
        """
        Translates a mouse click position into chessboard coordinates.
        
        Args:
            pos (tuple): The position of the mouse click (x, y).
            cell_size (int): The size of each square cell in pixels. Default is 100 for an 800x800 board.

        Returns:
            tuple: The (row, column) of the clicked cell.
        """
        x, y = pos  # Mouse click position in pixels.
        column = x // cell_size  # Integer division to find the column index.
        row = y // cell_size  # Integer division to find the row index.
        return (row, column)

    def switch_turns(self):
        self.current_player = self.user_player if self.current_player == self.ai_player else self.ai_player

    def play(self):
        while not self.board.is_game_over() and self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_square = self.ui.get_square_from_mouse(event.pos)
                    if self.current_player == self.user_player:
                        self.handle_user_player_click(clicked_square)
                    elif self.current_player == self.ai_player:
                        # AI player's turn logic
                        self.handle_ai_player_turn()

                    elif self.board.is_game_over():
                        self.logger.info("Game over!")
                        self.game_running = False

            self.update_ui()

    def handle_user_player_click(self, clicked_square):
        piece = self.board.get_piece_at_position(*clicked_square)
        if isinstance(piece, Piece):  # Ensure piece is actually a Piece object
            possible_moves = piece.get_possible_moves(self.board)
            if possible_moves:
                self.ui.highlight_square(*clicked_square, colour="BLUE")  # Highlight the selected piece
                self.ui.highlight_available_moves(possible_moves)
            else:
                # No possible moves, highlight in red
                self.ui.highlight_square(*clicked_square, colour="RED")
            self.logger.info(f"Player {self.current_player} clicked on square {clicked_square} with piece {piece}")
        else:
            # Handle empty cell click, possibly highlight in red if no piece is selected
            if not self.current_player.choosen_piece:
                self.ui.highlight_square(*clicked_square, colour="RED")
            self.logger.info(f"Player {self.current_player} clicked on empty square {clicked_square}")

    def update_ui(self):
        self.ui.display_board(self.board.get_board())
        pygame.display.update()