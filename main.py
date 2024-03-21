import pygame
from pygame import display, time, mouse, event

# Initialize Pygame
pygame.init()

import scripts.common as common
import scripts.rendering as rendering
from scripts.common import Size, GameState, GameMode, PlayerSide
from scripts.manager import GameManager

# Set the loop counter
LOOP = 1000
counter = LOOP

# Initialize the clock, screen, and set the window caption
_clock = time.Clock()
_screen = display.set_mode(Size.TOTAL, pygame.SRCALPHA, 32)
display.set_caption(common.TIT)

def handle_events(game_manager, mouse_position):
    '''
    Handle events such as mouse clicks and window close.

    Args:
        game_manager (GameManager): The game manager object.
        mouse_position (tuple): The current mouse position.

    Returns:
        bool: True if the game should continue running, False otherwise.
    '''
    # Set the initial value of running to True
    running = True

    # Iterate over all the events
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if GameState.is_running(game_manager.game_state):
                if not game_manager.selected_piece or not game_manager.handle_piece_move(mouse_position):
                    game_manager.handle_piece_selection(mouse_position)
            else:
                if rendering.START_BTN_RECT.collidepoint(mouse_position):
                    # Reset game
                    game_manager.reset_game()

                    # Set the game state to running
                    if GameMode.is_cvc(game_manager.game_mode):
                        global counter
                        counter = LOOP
    return running

def main():
    '''
    The main function.
    '''
    # Initialize the game manager, running
    global counter
    game_manager = GameManager(GameMode.PvC)
    running = True

    # Main loop
    while running:
        # Get the mouse position and handle the piece focus
        mouse_position = mouse.get_pos()
        game_manager.handle_piece_focus(mouse_position)

        # Check if the game is running and it's player vs computer mode with the computer's turn
        if GameState.is_running(game_manager.game_state):
            if GameMode.is_cvc(game_manager.game_mode) or GameMode.is_pvc(game_manager.game_mode) and PlayerSide.is_dark(game_manager.current_side):
                game_manager.computer_move()
                
        # Check if the game mode is CvC and the counter is greater than 0
        if GameMode.is_cvc(game_manager.game_mode) and counter > 0:
            if GameState.is_running(game_manager.game_state):
                # rendering.draw_game(_screen, game_manager)
                pass
            else:
                game_manager.reset_game()
                counter -= 1
        else:
            # Handle events and get the value of running
            running = handle_events(game_manager, mouse_position)

            # Draw the game or the screen based on the game state
            if GameState.is_running(game_manager.game_state):
                rendering.draw_game(_screen, game_manager)
            else:
                rendering.draw_screen(_screen, game_manager)

        # Update the display and limit the frame rate to 60 FPS
        display.flip()
        _clock.tick(60)

    # Quit the game
    pygame.quit()

# Run the main function
if __name__ == '__main__':
    main()
