import pygame
from pieces import Piece
from game_logger import setup_logging
import logging

setup_logging()




class UI:

    WHITE = (255, 242, 227)
    GREEN = (175, 183, 170)
    IMAGES = {
        "WhitePawn": pygame.image.load("src/main/images/wP.png"),
        "BlackPawn": pygame.image.load("src/main/images/bP.png"),
        "BlackBishop": pygame.image.load("src/main/images/bB.png"),
        "WhiteBishop": pygame.image.load("src/main/images/wB.png"),
        "WhiteKnight": pygame.image.load("src/main/images/wKn.png"),
        "BlackKnight": pygame.image.load("src/main/images/bKn.png"),
        "BlackKing": pygame.image.load("src/main/images/bK.png"),
        "WhiteKing": pygame.image.load("src/main/images/wK.png"),
        "WhiteRook": pygame.image.load("src/main/images/wR.png"),
        "BlackRook": pygame.image.load("src/main/images/bR.png"),
        "BlackQueen": pygame.image.load("src/main/images/bQ.png"),
        "WhiteQueen": pygame.image.load("src/main/images/wQ.png")
    }

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.SIZE = self.WIDTH // 8
        self.window = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setup_window()

    def setup_window(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("ChessAI")

    def display_board(self, board):
        for i in range(8):
            for j in range(8):
                piece = board[j][i]
                colour = self.WHITE if (i + j) % 2 == 0 else self.GREEN
                # Draw the square
                pygame.draw.rect(self.window, colour, (i * self.SIZE, j * self.SIZE, self.SIZE, self.SIZE))
                if isinstance(piece, Piece):
                    piece_key = f'{piece.colour}{type(piece).__name__}'
                    image = self.IMAGES[piece_key]
                    # Scale the image to fit the square size
                    image = pygame.transform.scale(image, (self.SIZE, self.SIZE))
                    # Calculate the position to center the image in the square
                    image_pos = (i * self.SIZE + (self.SIZE - image.get_width()) // 2, 
                                j * self.SIZE + (self.SIZE - image.get_height()) // 2)
                    self.window.blit(image, image_pos)

    def get_square_from_mouse(self, pos):
        x, y = pos
        row = y // self.SIZE
        col = x // self.SIZE
        return row, col

    def highlight_square(self, row, col, colour="YELLOW"):
        """
        Highlights a square on the board.

        Args:
            row (int): The row of the square to highlight.
            col (int): The column of the square to highlight.
            colour (str): The colour to use for the highlight ("BLUE", "GREEN", "RED", or "YELLOW").
        """
        self.logger.info(f"Highlighting square at {row, col}")
        colour_map = {
            "BLUE": (0, 0, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "YELLOW": (255, 255, 0)
        }

        highlight_colour = colour_map.get(colour, "RED")  # Default to yellow if colour not found
        pygame.draw.rect(self.window, highlight_colour, (col * self.SIZE, row * self.SIZE, self.SIZE, self.SIZE), 5)

    def highlight_available_moves(self, available_moves):
        for move in available_moves:
            row, col = move
            self.highlight_square(row, col, "GREEN")  # Use "GREEN" key for available moves
