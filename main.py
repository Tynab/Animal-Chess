import pygame
from pygame import display, time, mouse, event

pygame.init()

import scripts.common as common
import scripts.manager as manager
import scripts.rendering as rendering
from scripts.common import Size, GameState

_clock = time.Clock()
_screen = display.set_mode(Size.BOARD, pygame.SRCALPHA, 32)
display.set_caption(common.TIT)

def main():
    game_manager = manager.GameManager()
    running = True
    while running:
        # 
        mouse_position = mouse.get_pos()
        if game_manager.game_state == GameState.RUNNING:
            rendering.draw_game(_screen, game_manager)
            for e in event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if not game_manager.selected_piece or not game_manager.handle_piece_move(mouse_position):
                        game_manager.handle_piece_selection(mouse_position)
        else:
            rendering.draw_screen(_screen, game_manager)
            for e in event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if rendering.START_BTN_RECT.collidepoint(mouse_position):
                        game_manager = manager.GameManager()
                        game_manager.set_game_state(GameState.RUNNING)


        # Update the display
        display.flip()
        _clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
