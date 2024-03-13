import pygame
from pygame import display, time, mouse, event

pygame.init()

import scripts.common as common
import scripts.rendering as rendering
from scripts.common import Size, GameState, GameMode, PlayerSide
from scripts.manager import GameManager

# Initialize the clock, screen, and set the window caption
_clock = time.Clock()
_screen = display.set_mode(Size.BOARD, pygame.SRCALPHA, 32)
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
        # Check if the event is a window close event
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # Check if the game is currently running
            if GameState.is_running(game_manager.game_state):
                # If there is no selected piece or the piece move is not handled, handle piece selection
                if not game_manager.selected_piece or not game_manager.handle_piece_move(mouse_position):
                    game_manager.handle_piece_selection(mouse_position)
            else:
                # If the start button is clicked, reset the game
                if rendering.START_BTN_RECT.collidepoint(mouse_position):
                    game_manager.reset_game()

    # Return the value of running
    return running

def main():
    '''
    The main function.
    '''
    # Initialize the game manager and set the running variable to True
    game_manager = GameManager()
    running = True

    # Main loop
    while running:
        # Get the current mouse position
        mouse_position = mouse.get_pos()

        # Check if the game is running and it's player vs computer mode with the computer's turn
        if GameState.is_running(game_manager.game_state):
            # If it's the computer's turn, make the computer move
            if GameMode.is_pvc(game_manager.game_mode) and PlayerSide.is_dark(game_manager.current_side):
                game_manager.computer_move()
                
        # Handle events and update the running variable
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
