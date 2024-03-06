from board import ChessBoard
from ui import UI
from ai import AI
import pygame as pg


def handle_pygame_events(chess_board: ChessBoard, ui: UI) -> bool:
    """
    Handles pygame events such as quitting the game and processing player
    moves.

    Args:
        chess_board (ChessBoard): The chess board object.
        ui (UI): The user interface object.

    Returns:
        bool: True if the game should continue running, False otherwise.
    """

    global selected_piece, player_go
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False  # Signal to stop the game loop

        if event.type == pg.MOUSEBUTTONDOWN and player_go:
            process_player_move(chess_board, ui)

    return True  # Continue running the game loop


def process_player_move(chess_board: ChessBoard, ui: UI) -> None:
    """
    Processes the player's move by getting the clicked square and moving the
    piece if it is a valid move.

    Args:
        chess_board (ChessBoard): The chess board object.
        ui (UI): The user interface object.
    """

    global selected_piece, player_go
    clicked_row, clicked_col = ui.get_square_from_mouse(pg.mouse.get_pos())
    if selected_piece:
        if chess_board.move_piece(selected_piece[0], selected_piece[1],
                                  clicked_row, clicked_col):
            selected_piece = None
            player_go = False  # AI's turn
    else:
        if chess_board.get_board()[clicked_row][clicked_col] != '-':
            selected_piece = (clicked_row, clicked_col)


def process_ai_move(chess_board: ChessBoard, ui: UI) -> None:
    """
    Processes the AI's move by getting the best move from the minimax
    algorithm and moving the piece.

    Args:
        chess_board (ChessBoard): The chess board object.
        ui (UI): The user interface object.
    """

    global player_go
    ai_move = ai.minimax(1, False)[1]
    if ai_move:
        from_row, from_col, to_row, to_col = ai_move
        if chess_board.move_piece(from_row, from_col, to_row, to_col):
            player_go = True  # Player's turn


def update_game_state(chess_board: ChessBoard, ui: UI) -> bool:
    """
    Updates the game state by checking if the game is over and updating the
    display.

    Args:
        chess_board (ChessBoard): The chess board object.
        ui (UI): The user interface object.

    Returns:
        bool: True if the game should continue running, False otherwise.
    """

    game_over = chess_board.is_game_over()
    if game_over != 2:  # Assuming 2 means the game is still ongoing
        print("Game over!")
        return False
    return True


def main_game_loop():
    """
    This function is the main game loop that runs the game.
    """

    global run, selected_piece, player_go
    while run:  # Main game loop

        # Handle pygame events and update the run flag
        run = handle_pygame_events(chess_board, ui)

        if not player_go:  # If it's not the player's turn
            process_ai_move(chess_board, ai)  # Process AI's move

        # Display the chess board
        run = update_game_state(chess_board, ui) and run
        ui.display_board(chess_board.get_board())

        if selected_piece:  # If a piece is selected
            # Highlight the selected square
            ui.highlight_square(selected_piece[0], selected_piece[1])
        pg.display.update()  # Update the display


# Initialization code
pg.init()
ui = UI(400, 400)
ui.setup_window()
chess_board = ChessBoard()
ai = AI(chess_board)

# Global state variables
run = True
selected_piece = None
player_go = True

# Start the game loop
if __name__ == "__main__":
    main_game_loop()
