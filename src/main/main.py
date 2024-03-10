from Game import Game
from board import ChessBoard
import pygame as pg
from ui import UI
from players import UserPlayer, AIPlayer
from ai import AI


if __name__ == "__main__":
    pg.init()
    board = ChessBoard()
    # ui = UI(400, 400)
    ui = UI(800, 800)
    algorithm = AI(board)
    user_player = UserPlayer("White")
    ai_player = AIPlayer("Black", algorithm, depth=3)
    # game = Game(board, ui, user_player, ai_player)
    # game = Game(board, ui)
    game = Game(ui, user_player, ai_player, board)
    game.play()
