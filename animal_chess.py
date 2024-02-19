import math
import pygame
import sys
from enum import Enum

# Initialize pygame
pygame.init()

# Font names
class FontName(Enum):
    TXT = 'Arial'
    BTN = 'Lato'
    TIT = 'Garamond'

# Colors
class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    ORANGE = (255, 165, 0)
    GRAY = (128, 128, 128)

# Game constants
NAME = 'Animal Chess'
W, H = 7, 9
SPAN = 100
SIZE = (W * SPAN, H * SPAN)
CELL_SIZE = (SPAN, SPAN)
START_BTN_SIZE = (190, 50)

# Display setup
_screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(NAME)

# Fonts
_font_tit = pygame.font.SysFont(FontName.TIT.value, 45, bold=True)
_font_res = pygame.font.SysFont(FontName.TXT.value, 57, bold=True)
_font_btn = pygame.font.SysFont(FontName.BTN.value, 23, bold=True)

# Load images
_cover_scaled = pygame.transform.scale(pygame.image.load('assets/images/cover.png'), SIZE)
_start_btn_scaled = pygame.transform.scale(pygame.image.load('assets/images/button.png'), START_BTN_SIZE)
_start_btn_rect = pygame.Rect((SIZE[0] - START_BTN_SIZE[0]) / 2, SIZE[1] - START_BTN_SIZE[1] - 25, START_BTN_SIZE[0], START_BTN_SIZE[1])

# Clock setup
_clock = pygame.time.Clock()

# Game variables
RIVERS = [(x, y) for x in range(1, 6) for y in range(3, 6) if x != 3]
DENS = {
    'Dark': (3, 0),
    'Light': (3, 8)
}
TRAPS = {
    'Dark': [(2, 0), (3, 1), (4, 0)],
    'Light': [(2, 8), (3, 7), (4, 8)]
}

# Game state variables
_current_player = 'Light'
_selected_piece = None
_game_over = False
_game_result = None
_river_images = []
_pieces = {}


def initialize_game():
    '''
    Initialize the game state variables and the pieces on the board.
    '''
    global _current_player, _selected_piece, _game_over, _game_result, _river_images, _pieces
    _current_player = 'Light'
    _selected_piece = None
    _game_over = False
    _game_result = None
    _river_images = [pygame.transform.scale(pygame.image.load(f'assets/images/river_{x}_{y}.png'), CELL_SIZE) for y in range(2) for x in range(3)]
    _pieces = {}
    poss = {
        'Dark': [(0, 0), (6, 0), (1, 1), (5, 1), (0, 2), (2, 2), (4, 2), (6, 2)],
        'Light': [(6, 8), (0, 8), (5, 7), (1, 7), (6, 6), (4, 6), (2, 6), (0, 6)]
    }
    for side in ('Dark', 'Light'):
        _pieces[side] = {}
        for i, name in enumerate(('Lion', 'Tiger', 'Cat', 'Dog', 'Elephant', 'Wolf', 'Leopard', 'Rat')):
            _pieces[side][name] = {'pos': poss[side][i], 'img': pygame.transform.scale(pygame.image.load(f'assets/pieces/{side.lower()}/{name.lower()}.png'), CELL_SIZE)}


def can_defeat(attacker, defender):
    '''
    Determine if the attacker can defeat the defender based on the game's rules.

    Args:
        attacker (str): The name of the attacking piece.
        defender (str): The name of the defending piece.

    Returns:
        bool: Whether the attacker can defeat the defender.
    '''
    defeat_map = {
        'Rat': ['Rat', 'Elephant'],
        'Cat': ['Cat', 'Rat'],
        'Dog': ['Dog', 'Cat', 'Rat'],
        'Wolf': ['Wolf', 'Dog', 'Cat', 'Rat'],
        'Leopard': ['Leopard', 'Wolf', 'Dog', 'Cat', 'Rat'],
        'Lion': ['Lion', 'Leopard', 'Wolf', 'Dog', 'Cat', 'Rat'],
        'Tiger': ['Tiger', 'Lion', 'Leopard', 'Wolf', 'Dog', 'Cat', 'Rat'],
        'Elephant': ['Elephant', 'Tiger', 'Lion', 'Leopard', 'Wolf', 'Dog', 'Cat']
    }
    return defender in defeat_map.get(attacker, [])


def can_move(piece_name, start_pos, end_pos):
    '''
    Determine if a piece can move to a new position based on the game's rules.

    Args:
        piece_name (str): The name of the piece.
        start_pos (tuple): The starting position of the piece.
        end_pos (tuple): The ending position of the piece.

    Returns:
        bool: Whether the piece can move to the new position.
    '''

    # Check if the move is within the board
    if not (0 <= end_pos[0] < W and 0 <= end_pos[1] < H):
        return False

    # Check if the move is within the same row or column
    if abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1]) != 1:
        return False

    # Check if the piece is moving to a river square
    if piece_name not in ['Dog', 'Rat'] and end_pos in RIVERS:
        return False

    opp = 'Light' if _current_player == 'Dark' else 'Dark'

    # Check if the piece is moving to its own den
    if end_pos in TRAPS[opp]:
        for opp_piece_pos in _pieces[opp].values():
            if opp_piece_pos['pos'] == end_pos:
                return False

    # Check if the piece is moving to an opponent's den
    for opp_piece_name, opp_pos_info in _pieces[opp].items():
        if opp_pos_info['pos'] == end_pos:
            return can_defeat(piece_name, opp_piece_name)

    # Check if the piece is moving to a trap
    for piece_info in _pieces[_current_player].values():
        if piece_info['pos'] == end_pos:
            return False

    return True


def highlight_possible_moves(piece, start_pos):
    '''
    Highlight the possible moves for a piece based on the game's rules.
    
    Args:
        piece (str): The name of the piece.
        start_pos (tuple): The starting position of the piece.
        
    Returns:
        list: The list of possible moves for the piece.
    '''
    possible_moves = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        end_pos = (start_pos[0] + dx, start_pos[1] + dy)
        if can_move(piece, start_pos, end_pos):
            possible_moves.append(end_pos)
    return possible_moves


def draw_star(surface, color, center, outer_radius, inner_radius, opacity=255, points=5):
    """
    Draw a semi-transparent star on the specified surface.

    Args:
        surface (pygame.Surface): The surface to draw on.
        color (tuple): The color of the star (R, G, B).
        center (tuple): The center of the star (x, y).
        outer_radius (int): The radius from the center to the outer point of the star.
        inner_radius (int): The radius from the center to the inner corner of the star.
        points (int): The number of points the star has.
        opacity (int): The opacity level of the star (0 to 255).
    """
    star_surface = pygame.Surface((2*outer_radius, 2*outer_radius), pygame.SRCALPHA)
    star_surface.fill((0, 0, 0, 0))
    outer_points = []
    inner_points = []
    angle_between_points = (2 * math.pi) / points
    start_angle = math.pi / 2
    star_center = (outer_radius, outer_radius)

    # Calculate the outer and inner points
    for i in range(points):
        outer_angle = start_angle - (angle_between_points * i)
        inner_angle = outer_angle - (angle_between_points / 2)
        outer_points.append((star_center[0] + math.cos(outer_angle) * outer_radius, star_center[1] - math.sin(outer_angle) * outer_radius))
        inner_points.append((star_center[0] + math.cos(inner_angle) * inner_radius, star_center[1] - math.sin(inner_angle) * inner_radius))

    star_points = []

    # Create a list of points to draw the star
    for i in range(points):
        star_points.append(outer_points[i])
        star_points.append(inner_points[i])

    # Draw the star on the new surface
    pygame.draw.polygon(star_surface, color + (opacity,), star_points)

    # Blit this surface onto the main surface
    surface.blit(star_surface, (center[0] - outer_radius, center[1] - outer_radius))


def draw_game():
    '''
    Draw the game board with the pieces and the possible moves for the selected piece.
    '''
    river_idx = 0
    river_images_count = len(_river_images)

    # Draw the game board
    for c in range(W):
        for r in range(H):
            if (c, r) in RIVERS:
                _screen.blit(_river_images[river_idx % river_images_count], (c * SPAN, r * SPAN))
                river_idx += 1
            else:
                pygame.draw.rect(_screen, Color.WHITE.value, [c * SPAN, r * SPAN, SPAN, SPAN], 0)
            pygame.draw.rect(_screen, Color.GRAY.value, pygame.Rect(c * SPAN, r * SPAN, SPAN, SPAN), 1)

    # Draw dens
    _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/den.png'), CELL_SIZE), (DENS['Dark'][0] * SPAN, DENS['Dark'][1] * SPAN))
    _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/den.png'), CELL_SIZE), (DENS['Light'][0] * SPAN, DENS['Light'][1] * SPAN))

    # Draw traps
    for trap in TRAPS['Dark']:
        _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/trap.png'), CELL_SIZE), (trap[0] * SPAN, trap[1] * SPAN))
    for trap in TRAPS['Light']:
        _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/trap.png'), CELL_SIZE), (trap[0] * SPAN, trap[1] * SPAN))

    # Draw pieces
    for side in _pieces:
        for piece_info in _pieces[side].values():
            draw_star(_screen, side == 'Dark' and Color.ORANGE.value or Color.CYAN.value, (piece_info['pos'][0] * SPAN + 50, piece_info['pos'][1] * SPAN + 50), 40, 20, 192, 20)
            _screen.blit(piece_info['img'], (piece_info['pos'][0] * SPAN, piece_info['pos'][1] * SPAN))
        
    # Highlight possible moves for the selected piece with circles
    if _selected_piece:
        for move in highlight_possible_moves(_selected_piece, _pieces[_current_player][_selected_piece]['pos']):
            highlight_surface = pygame.Surface((SPAN, SPAN), pygame.SRCALPHA)
            pygame.draw.circle(highlight_surface, (*Color.YELLOW.value, 192), (SPAN // 2, SPAN // 2), SPAN // 3)
            _screen.blit(highlight_surface, (move[0] * SPAN, move[1] * SPAN))


def switch_player():
    '''
    Switch the current player to the other player.
    '''
    global _current_player
    _current_player = _current_player == 'Dark' and 'Light' or 'Dark'


def handle_piece_selection(mouse_pos):
    '''
    Handle the selection of a piece based on the current mouse position.

    Args:
        mouse_pos (tuple): The current mouse position.

    Returns:
        bool: Whether a piece has been selected.
    '''
    global _selected_piece
    c, r = mouse_pos[0] // SPAN, mouse_pos[1] // SPAN
    for piece_name, piece_info in _pieces[_current_player].items():
        if piece_info['pos'] == (c, r):
            _selected_piece = piece_name
            return True

    return False


def handle_piece_move(mouse_pos):
    '''
    Handle the movement of a piece based on the current mouse position.

    Args:
        mouse_pos (tuple): The current mouse position.

    Returns:
        bool: Whether the piece has been moved.
    '''
    global _selected_piece

    # Return False if no piece is selected
    if not _selected_piece:
        return False

    c, r = mouse_pos[0] // SPAN, mouse_pos[1] // SPAN

    # Move the selected piece to the new position if possible
    if can_move(_selected_piece, _pieces[_current_player][_selected_piece]['pos'], (c, r)):
        _pieces[_current_player][_selected_piece]['pos'] = (c, r)
        opp = _current_player == 'Dark' and 'Light' or 'Dark'
        for opp_piece_name, opp_piece_info in _pieces[opp].items():
            if opp_piece_info['pos'] == (c, r):
                del _pieces[opp][opp_piece_name]
                break
        _selected_piece = None
        switch_player()
        return True

    return False


def check_game_end():
    '''
    Check if the game has ended and display the game result.
    '''
    global _game_over, _game_result

    # Check if any of 'Dark's pieces has entered 'Light's den
    for piece_info in _pieces['Dark'].values():
        if piece_info['pos'] == DENS['Light']:
            _game_over = True
            _game_result = 'YOU\nLOSE!!!'
            return

    # Check if any of 'Light's pieces has entered 'Dark's den
    for piece_info in _pieces['Light'].values():
        if piece_info['pos'] == DENS['Dark']:
            _game_over = True
            _game_result = 'YOU\nWIN!!!'
            return


def draw_screen(end_game=False):
    '''
    Draw the game screen based on the game state.

    Args:
        end_game (bool): Whether the game has ended.
    '''
    _screen.blit(_cover_scaled, (0, 0))

    # Draw the game title
    txt_tit = _font_tit.render(NAME, True, Color.WHITE.value)
    _screen.blit(txt_tit, txt_tit.get_rect(center=(SIZE[0] / 2, 25)))

    # Draw the game over screen with the game result if applicable
    if end_game:
        for i, line in enumerate(_game_result.split('\n')):
            txt_game_over = _font_res.render(line, True, Color.YELLOW.value)
            _screen.blit(txt_game_over, txt_game_over.get_rect(center=(SIZE[0] / 2, SIZE[1] / 2 + 90 + i * (txt_game_over.get_height() + 5))))

    # Draw the start button
    _screen.blit(_start_btn_scaled, _start_btn_rect.topleft)

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
        _screen.blit(_start_btn_scaled, _start_btn_rect.topleft)
        _screen.blit(txt_surf, txt_surf.get_rect(center=_start_btn_rect.center))

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


initialize_game()
draw_screen()

carry_on = True

# Main game loop
while carry_on:
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            carry_on = False
        elif _game_over:
            draw_screen(True)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if not _selected_piece or not handle_piece_move(mouse_pos):
                handle_piece_selection(mouse_pos)

    # Draw the game board
    if not _game_over:
        draw_game()
        check_game_end()

    # Update the display
    pygame.display.flip()
    _clock.tick(60)

pygame.quit()
