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
                        self.update_ui()
                if self.current_player == self.ai_player:
                    self.logger.info("AI's Turn ")
                        # AI player's turn logic
                    self.handle_ai_player_turn()
                    pygame.display.update()

                elif self.board.is_game_over():
                    self.logger.info("Game over!")
                    self.game_running = False

            self.logger.info(f"Current player's turn: {id(self.current_player)}")
            self.logger.info(f"AI player definition: {id(self.ai_player)}")
            self.update_ui()
            pygame.display.update()

    def handle_user_player_click(self, clicked_square):
        piece = self.board.get_piece_at_position(*clicked_square)
        # self.logger.info(f"Piece: {piece}")
        # self.logger.info (f"Stored {self.user_player.chosen_piece}")
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
            if not self.current_player.chosen_piece:
                self.ui.highlight_square(*clicked_square, colour="RED")
            self.logger.info(f"Player {self.current_player} clicked on empty square {clicked_square}")


        if self.user_player.chosen_piece != None and isinstance(self.user_player.chosen_piece, Piece):
            possible_moves = self.user_player.chosen_piece.get_possible_moves(self.board)
            self.logger.info (f"Stored {self.user_player.chosen_piece}")
            self.logger.info(f"Clicked piece is {clicked_square}")
            self.logger.info(f"Possible moves are {possible_moves}" )
            if clicked_square in (possible_moves):
                self.logger.info("Move is valid")

                # Move the piece to the new position
                self.board.move_piece(self.user_player.chosen_square, clicked_square)
                # Log the move
                self.logger.info(f"Moved {piece} to {clicked_square}")
                self.switch_turns()
                
                

            else:
                self.logger.info("Move is invalid")
        
        self.user_player.chosen_piece = piece
        self.user_player.chosen_square = clicked_square
                

    def update_ui(self):
        self.ui.display_board(self.board.get_board())
        pygame.display.update()

    def handle_ai_player_turn(self):
        self.ai_player.make_move(self.board)