import pygame

def draw_screen(game_state, screen, end_game=False):
    screen.blit(_cover_scaled, (0, 0))

    # Draw the game title
    txt_tit = _font_tit.render(NAME, True, Color.WHITE.value)
    screen.blit(txt_tit, txt_tit.get_rect(center=(SIZE[0] / 2, 25)))

    # Draw the game over screen with the game result if applicable
    if end_game:
        for i, line in enumerate(_game_result.split('\n')):
            txt_game_over = _font_res.render(line, True, Color.YELLOW.value)
            screen.blit(txt_game_over, txt_game_over.get_rect(center=(SIZE[0] / 2, SIZE[1] / 2 + 90 + i * (txt_game_over.get_height() + 5))))

    # Draw the start button
    screen.blit(_start_btn_scaled, _start_btn_rect.topleft)

    txt_color = Color.WHITE.value
    waiting_for_input = True

    # Enter the loop while waiting for user input
    while waiting_for_input:
        mouse_pos = pygame.mouse.get_pos()

        # Change text color based on mouse hover
        if _start_btn_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            txt_color = Color.YELLOW.value
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            txt_color = Color.WHITE.value

        # Render and draw the text on the start button
        txt_surf = _font_btn.render('New Game', True, txt_color)
        screen.blit(_start_btn_scaled, _start_btn_rect.topleft)
        screen.blit(txt_surf, txt_surf.get_rect(center=_start_btn_rect.center))

        # Update the display
        pygame.display.flip()

        # Handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN and _start_btn_rect.collidepoint(mouse_pos):
                if end_game:
                    initialize_game()
                waiting_for_input = False

    # Reset the mouse cursor
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def draw_game(game_state, screen):
    # Draw the game board, pieces, possible moves, etc.
    pass

def draw_start_button(screen):
    # Draw the start button
    pass
