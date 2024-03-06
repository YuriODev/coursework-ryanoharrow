import pygame as pg
from pieces import Piece

class UI:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.SIZE = self.WIDTH // 8
        self.WHITE = (255, 242, 227)
        self.GREEN = (175, 183, 170)
        self.IMAGES = {
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

    def setup_window(self):
        self.window = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("ChessAI")

    def display_board(self, board):
        for i in range(8):
            for j in range(8):
                piece = board[j][i]
                color = self.WHITE if (i + j) % 2 == 0 else self.GREEN
                pg.draw.rect(self.window, color, (i * self.SIZE, j * self.SIZE, self.SIZE, self.SIZE))
                if isinstance(piece, Piece):
                    piece_key = f'{piece.colour}{type(piece).__name__}'
                    image = self.IMAGES[piece_key]
                    self.window.blit(image, ((i * self.SIZE)-5, (j * self.SIZE)-4))

    def get_square_from_mouse(self, pos):
        x, y = pos
        row = y // self.SIZE
        col = x // self.SIZE
        return row, col

    def highlight_square(self, row, col):
        highlight_color = (255, 255, 0) 
        pg.draw.rect(self.window, highlight_color, (col * self.SIZE, row * self.SIZE, self.SIZE, self.SIZE), 5)