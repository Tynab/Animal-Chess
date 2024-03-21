import math
import pygame
import scripts.common as common
from pygame import Surface, Rect, draw, transform, image, font, mouse
from scripts.common import Color, ImagePath, Size, FontName, GameState

COVER_SCALED = transform.scale(image.load(ImagePath.COVER), Size.BOARD)
START_BTN_SCALED = transform.scale(image.load(ImagePath.START_BTN), Size.START_BTN)
START_BTN_RECT = Rect((Size.BOARD[0] - Size.START_BTN[0]) / 2, Size.BOARD[1] - Size.START_BTN[1] - 25, Size.START_BTN[0], Size.START_BTN[1])

FONT_TIT = font.SysFont(FontName.TIT, 45, bold=True)
FONT_BTN = font.SysFont(FontName.BTN, 23, bold=True)
FONT_RES = font.SysFont(FontName.TXT, 57, bold=True)

@staticmethod
def draw_screen(screen, game_manager):
    '''
    Draws the game screen based on the current state of the game.

    Parameters:
        screen (pygame.Surface): The surface on which to draw the game.
        game_manager (GameManager): The game manager that holds the state of the game.
    '''
    # Draw the game title
    screen.blit(COVER_SCALED, (0, 0))
    x, y = Size.BOARD[0] / 2, Size.BOARD[1] / 2 + 90
    txt_tit = FONT_TIT.render(common.TIT, True, Color.WHITE)
    screen.blit(txt_tit, txt_tit.get_rect(center=(x, 25)))

    # Draw the game over screen with the game result if applicable
    if GameState.is_over(game_manager.game_state):
        for i, line in enumerate(game_manager.game_result.split('\n')):
            txt_game_over = FONT_RES.render(line, True, Color.YELLOW)
            screen.blit(txt_game_over, txt_game_over.get_rect(center=(x, y + i * (txt_game_over.get_height() + 5))))

    # Draw the start button
    screen.blit(START_BTN_SCALED, START_BTN_RECT.topleft)
    txt_color = Color.WHITE
    
    # Check if the mouse is hovering over the start button
    if START_BTN_RECT.collidepoint(mouse.get_pos()):
        mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        txt_color = Color.YELLOW
    else:
        mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        txt_color = Color.WHITE

    # Render and draw the "New Game" text on the start button
    txt_surf = FONT_BTN.render('New Game', True, txt_color)
    screen.blit(START_BTN_SCALED, START_BTN_RECT.topleft)
    screen.blit(txt_surf, txt_surf.get_rect(center=START_BTN_RECT.center))

@staticmethod
def draw_game(screen, game_manager):
    '''
    Draw the game on the screen.
    
    Args:
        screen (pygame.Surface): The surface to draw on.
        game_manager (GameManager): The game manager.
    '''
    # Check if the mouse is hovering over a cell and set the cursor accordingly
    cursor_hand = False
    mouse_pos = mouse.get_pos()

    # Draw the cells and the pieces on the board
    for col in game_manager.board.cells:
        for cell in col:
            # Calculate the position of the cell
            x, y = cell.position[0] * common.SPAN, cell.position[1] * common.SPAN
            cell_rect = Rect(x, y, common.SPAN, common.SPAN)
            draw.rect(screen, Color.WHITE, cell_rect, 0)

            # Draw the cell image if it exists
            if cell.image:
                screen.blit(cell.image, (x, y))
            
            # Draw the cell border
            draw.rect(screen, Color.GREY, cell_rect, 1)

            # Check if the mouse is hovering over a cell with a piece of the current side
            if cell.piece:
                # Check if the mouse is hovering over a cell with a piece of the current side
                cursor_hand |= cell_rect.collidepoint(mouse_pos) and cell.piece.side == game_manager.current_side
                draw_star(screen, Color.star_color(cell.piece.side), (x + 50, y + 50), 40, 20, 192, 20)

                # Flip the piece image horizontally if cell.position > 3
                if cell.position[0] > 3:
                    screen.blit(transform.flip(cell.piece.image, True, False), (x, y))
                else:
                    screen.blit(cell.piece.image, (x, y))
    
    # Highlight the available cells for the selected piece
    if game_manager.selected_piece:
        # Create a surface to draw the highlighted cells
        highlight_surface = Surface((common.SPAN, common.SPAN), pygame.SRCALPHA)

        # Iterate through the available cells of the selected piece
        for cell in game_manager.selected_piece.available_cells(game_manager.board):
            x, y = cell.position[0] * common.SPAN, cell.position[1] * common.SPAN
            cell_rect = Rect(x, y, common.SPAN, common.SPAN)
            cursor_hand |= cell_rect.collidepoint(mouse_pos)
            draw.circle(
                highlight_surface,
                (*Color.RED, 192) if cell.piece else (*Color.GREEN, 192) if cell.is_river or abs(cell.position[0] - game_manager.selected_piece.position[0]) > 1 or abs(cell.position[1] - game_manager.selected_piece.position[1]) > 1 else (*Color.YELLOW, 192),
                (common.SPAN // 2, common.SPAN // 2),
                common.SPAN // 4
            )
            screen.blit(highlight_surface, (x, y))
    
    # Set the cursor based on whether the mouse is hovering over a cell or not
    mouse.set_cursor(cursor_hand and pygame.SYSTEM_CURSOR_HAND or pygame.SYSTEM_CURSOR_ARROW)

    # Draw the subscreen
    if game_manager.focused_piece:
        draw_subscreen(screen, game_manager)

@staticmethod
def draw_subscreen(screen, game_manager):
    '''
    Draw the subscreen on the screen.
    
    Args:
        screen (pygame.Surface): The surface to draw on.
        game_manager (GameManager): The game manager.
    '''
    # Create a subscreen surface and fill it with a grey color
    subscreen = Surface((Size.SUBSCREEN[0], Size.SUBSCREEN[1]))
    subscreen.fill(Color.GREY)
    subscreen.blit(transform.scale(game_manager.focused_piece.artwork, Size.ARTWORK), (0, 0))
    y_position = Size.ARTWORK[1] + Size.PADDING[1]
    desciption_text = f'''Name: {game_manager.focused_piece.name}
Type: {game_manager.focused_piece.__class__.__name__}
ATK: {game_manager.focused_piece.atk}
{game_manager.focused_piece.detail}'''
    
    # Wrap the description text and render it on the subscreen
    for line in wrap_text(desciption_text, FONT_BTN, Size.SUBSCREEN[0] - Size.PADDING[0] * 3):
        detail_text = FONT_BTN.render(line, True, Color.WHITE)
        subscreen.blit(detail_text, (Size.PADDING[0] * 2, y_position))
        y_position += detail_text.get_height() + Size.PADDING[1] / 2
    
    # Draw the subscreen on the screen
    screen.blit(subscreen, (Size.BOARD[0], 0))

@staticmethod
def draw_star(surface, color, center, outer_radius, inner_radius, opacity=255, points=5):
    '''
    Draw a semi-transparent star on the specified surface.

    Args:
        surface (pygame.Surface): The surface to draw on.
        color (tuple): The color of the star (R, G, B).
        center (tuple): The center of the star (x, y).
        outer_radius (int): The radius from the center to the outer point of the star.
        inner_radius (int): The radius from the center to the inner corner of the star.
        opacity (int): The opacity level of the star (0 to 255).
        points (int): The number of points the star has.
    '''
    star_surface = Surface((2 * outer_radius, 2 * outer_radius), pygame.SRCALPHA)
    angle_between_points = (2 * math.pi) / points
    start_angle = math.pi / 2
    star_center = (outer_radius, outer_radius)
    draw.polygon(star_surface, color + (opacity,), [point for pair in [
        (
            (star_center[0] + math.cos(start_angle - i * angle_between_points) * outer_radius, star_center[1] - math.sin(start_angle - i * angle_between_points) * outer_radius),
            (star_center[0] + math.cos(start_angle - (i + 0.5) * angle_between_points) * inner_radius, star_center[1] - math.sin(start_angle - (i + 0.5) * angle_between_points) * inner_radius)
        )
        for i in range(points)
    ] for point in pair])
    surface.blit(star_surface, (center[0] - outer_radius, center[1] - outer_radius))

@staticmethod
def wrap_text(text, font, max_width):
    '''
    Wrap the text to fit within the specified width.
    
    Args:
        text (str): The text to wrap.
        font (pygame.font.Font): The font to use for rendering the text.
        max_width (int): The maximum width of the wrapped text.
    
    Returns:
        list: The list of wrapped lines.
    '''
    # Create a list to hold the wrapped lines
    wrapped_lines = []

    # Iterate over the lines of the text
    for line in text.split('\n'):
        # Create a list to hold the words of the current line
        current_line = []

        # Split the line into words and iterate over them
        for word in line.split(' '):
            # Get the width of the current line with the new word
            width, _ = font.size(' '.join(current_line + [word]))

            # Append the word to the current line if the width is less than the max width
            if width <= max_width:
                current_line.append(word)
            else:
                wrapped_lines.append(' '.join(current_line))
                current_line = [word]

        # Append the current line if it's not empty
        if current_line:
            wrapped_lines.append(' '.join(current_line))

    # Return the wrapped lines
    return wrapped_lines