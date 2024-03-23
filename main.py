import pygame
from pygame import display, time, mouse, event, Color

# Initialize Pygame
pygame.init()

import scripts.common as common
import scripts.rendering as rendering
from scripts.common import Size, GameState, GameMode, PlayerSide, Color
from scripts.manager import GameManager

# Set the loop counter
LOOP = 1000

# Set the global variables
_counter = LOOP
_game_mode = GameMode.PvC

# Set the screen and clock
_clock = time.Clock()
_screen = display.set_mode(Size.TOTAL, pygame.SRCALPHA, 32)

# Set the window caption
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
    # Iterate over all the events
    for e in event.get():
        if e.type == pygame.QUIT:
            return False
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
                        # Set the global variables
                        global _counter

                        # Reset the counter
                        _counter = LOOP

    # Return True if the game should continue running
    return True

def main():
    '''
    The main function.
    '''
    # Initialize the game manager
    game_manager = GameManager(_game_mode)
    running = True

    # Set the global variables
    global _counter

    # Main loop
    while running:
        # Fill the screen with white color
        _screen.fill(Color.WHITE)

        # Check if the game is running
        if GameState.is_running(game_manager.game_state):
            if GameMode.is_cvc(game_manager.game_mode):
                game_manager.computer_move()
            else:
                # Get the mouse position
                mouse_position = mouse.get_pos()
                game_manager.handle_piece_focus(mouse_position)

                # Check if it is the computer's turn
                if GameMode.is_pvc(game_manager.game_mode) and PlayerSide.is_dark(game_manager.current_side):
                    game_manager.computer_move()
                else:
                    running = handle_events(game_manager, mouse_position)

                # Draw the game
                rendering.draw_game(_screen, game_manager)
        else:
            if GameMode.is_cvc(game_manager.game_mode) and _counter > 0:
                game_manager.reset_game()
                _counter -= 1
            else:
                running = handle_events(game_manager, mouse.get_pos())
                rendering.draw_screen(_screen, game_manager)

        # Update the display and limit the frame rate to 60 FPS
        display.flip()
        _clock.tick(60)

    # Quit the game
    pygame.quit()

# Run the main function
if __name__ == '__main__':
    main()
