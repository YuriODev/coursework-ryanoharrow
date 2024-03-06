from board import ChessBoard
from ui import UI
from ai import AI
import pygame as pg

pg.init()
ui = UI(400, 400)  
ui.setup_window()
chess_board = ChessBoard()
ai = AI(chess_board)

"""Change here"""

run = True
selected_piece = None 
player_go = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            clicked_row, clicked_col = ui.get_square_from_mouse(pg.mouse.get_pos())
            if player_go:
                if selected_piece:
                    chess_board.move_piece(selected_piece[0], selected_piece[1], clicked_row, clicked_col)
                    selected_piece = None
                    player_go = False
        
                else:
                    if chess_board.get_board()[clicked_row][clicked_col] != '-':
                        selected_piece = (clicked_row, clicked_col)

            if not player_go:
                cc = ai.minimax(1, False)[1]
                if cc is not None:
                    from_row, from_col, to_row, to_col = cc
                    valid_move = chess_board.move_piece(from_row, from_col, to_row, to_col)
                    if valid_move:
                        player_go = True
                    else:
                        print (cc)
                        print("Invalid move")
                        player_go = True

            if chess_board.is_game_over() != 2:
                print ("Game over! ")


    ui.display_board(chess_board.get_board())

    if selected_piece:
        ui.highlight_square(selected_piece[0], selected_piece[1])

    pg.display.update()