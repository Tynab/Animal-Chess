import pygame
from pygame import display, time

pygame.init()

import scripts.common as common
import scripts.manager as manager
import scripts.rendering as rendering
from scripts.common import Size, GameState

_screen = display.set_mode(Size.BOARD, pygame.SRCALPHA, 32)

display.set_caption(common.TIT)

_clock = time.Clock()

_game_manager = manager.GameManager()

rendering.draw_game(_screen, _game_manager)

# Main game loop
_carry_on = True
while _carry_on:
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            _carry_on = False
        elif _game_manager.game_state == GameState.OVER:
            rendering.draw_screen(_screen, _game_manager)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if not _game_manager.selected_piece or not _game_manager.handle_piece_move(mouse_position):
                _game_manager.handle_piece_selection(mouse_position)

    #
    rendering.draw_game(_screen, _game_manager)

    # Update the display
    pygame.display.flip()
    _clock.tick(60)

pygame.quit()
