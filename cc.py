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

# Player labels
class PlayerLbl(Enum):
    DARK = 'Dark',
    LIGHT = 'Light'

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

class Piece:
    def __init__(self, name, desc, pos, img_path, art_path):
        '''
        Initializes a Piece object.

        Args:
        - name: The name of the piece.
        - desc: The description of the piece.
        - pos: The position of the piece on the board.
        - img_path: The file path to the image of the piece.
        - art_path: The file path to the artwork of the piece.
        '''
        self.name = name
        self.desc = desc
        self.pos = pos
        self.img = pygame.transform.scale(pygame.image.load(img_path), CELL_SIZE)
        self.art = pygame.transform.scale(pygame.image.load(art_path), CELL_SIZE)
        self.atk = self.set_atk()

    def set_atk(self):
        # Should be overridden by subclass
        return 0

class Elephant(Piece):
    def set_atk(self):
        return 8

class Lion(Piece):
    def set_atk(self):
        return 7

class Tiger(Piece):
    def set_atk(self):
        return 6

class Leopard(Piece):
    def set_atk(self):
        return 5

class Wolf(Piece):
    def set_atk(self):
        return 4

class Dog(Piece):
    def set_atk(self):
        return 3

class Cat(Piece):
    def set_atk(self):
        return 2

class Rat(Piece):
    def set_atk(self):
        return 1

class Player:
    def __init__(self, name, lbl):
        self.name = name
        self.lbl = lbl
        self.pieces = {}

    def add_piece(self, piece):
        self.pieces[piece.name] = piece

class Step:
    def __init__(self, player_lbl_name, piece_name, des_pos):
        self.player_lbl_name = player_lbl_name
        self.piece_name = piece_name
        self.des_pos = des_pos

class Manager:
    def __init__(self):
        self.players = {}
        self.steps = []
        self.current_player = None
        self.game_over = False
        self.game_result = None
        self.selected_piece = None
        self.RIVER_IMGS = [pygame.transform.scale(pygame.image.load(f'assets/images/river_{x}_{y}.png'), CELL_SIZE) for y in range(2) for x in range(3)]
        self.RIVERS = [(x, y) for x in range(1, 6) for y in range(3, 6) if x != 3]
        self.DENS = {
            PlayerLbl.DARK: (3, 0),
            PlayerLbl.LIGHT: (3, 8)
        }
        self.TRAPS = {
            PlayerLbl.DARK: [(2, 0), (3, 1), (4, 0)],
            PlayerLbl.LIGHT: [(2, 8), (3, 7), (4, 8)]
        }

    
    def add_player(self, player):
        '''
        Add a player to the game

        Args:
        - player: An instance of the Player class

        Example:
        >>> player_c = Player('Computer', PlayerLbl.DARK)
        >>> add_player(player_c)
        '''
        self.players[player.lbl] = player
        if not self.current_player:
            self.current_player = player.lbl.value

    def switch_player(self):
        '''
        Switch the current player
        '''
        self.current_player = self.current_player == PlayerLbl.DARK and PlayerLbl.LIGHT or PlayerLbl.DARK

    def initialize_game(self):
        player_dark = Player('Computer', PlayerLbl.DARK)
        player_light = Player('Player', PlayerLbl.LIGHT)
        pieces_dark = [
            Elephant('Mammoth', 'Elephant of the Challenger', (4, 2), 'assets/pieces/dark/elephant.png', 'assets/artworks/dark/elephant.png'),
            Lion('Smilodon', 'Lion of the Challenger', (6, 0), 'assets/pieces/dark/lion.png', 'assets/artworks/dark/lion.png'),
            Tiger('White Tiger', 'Tiger of the Challenger', (0, 0), 'assets/pieces/dark/tiger.png', 'assets/artworks/dark/tiger.png'),
            Leopard('Black Panther', 'Leopard of the Challenger', (2, 2), 'assets/pieces/dark/leopard.png', 'assets/artworks/dark/leopard.png'),
            Wolf('Grey Wolf', 'Wolf of the Challenger', (0, 2), 'assets/pieces/dark/wolf.png', 'assets/artworks/dark/wolf.png'),
            Dog('Saluki', 'Dog of the Challenger', (1, 1), 'assets/pieces/dark/dog.png', 'assets/artworks/dark/dog.png'),
            Cat('Sphynx', 'Cat of the Challenger', (5, 1), 'assets/pieces/dark/cat.png', 'assets/artworks/dark/cat.png'),
            Rat('Rat', 'Rat of the Challenger', (6, 2), 'assets/pieces/dark/rat.png', 'assets/artworks/dark/rat.png')
        ]
        pieces_light = [
            Elephant('Loxodonta', 'Elephant of the Protector', (4, 6), 'assets/pieces/light/elephant.png', 'assets/artworks/light/elephant.png'),
            Lion('Panthera Leo', 'Lion of the Protector', (6, 8), 'assets/pieces/light/lion.png', 'assets/artworks/light/lion.png'),
            Tiger('Bengal Tiger', 'Tiger of the Protector', (0, 8), 'assets/pieces/light/tiger.png', 'assets/artworks/light/tiger.png'),
            Leopard('Siberi Leopard', 'Leopard of the Protector', (2, 6), 'assets/pieces/light/leopard.png', 'assets/artworks/light/leopard.png'),
            Wolf('Silver Fang', 'Wolf of the Protector', (0, 6), 'assets/pieces/light/wolf.png', 'assets/artworks/light/wolf.png'),
            Dog('Pitbull', 'Dog of the Protector', (1, 7), 'assets/pieces/light/dog.png', 'assets/artworks/light/dog.png'),
            Cat('Wildcat', 'Cat of the Protector', (5, 7), 'assets/pieces/light/cat.png', 'assets/artworks/light/cat.png'),
            Rat('Rat', 'Rat of the Protector', (6, 6), 'assets/pieces/light/rat.png', 'assets/artworks/light/rat.png')
        ]

        for piece in pieces_dark:
            player_dark.add_piece(piece)
        for piece in pieces_light:
            player_light.add_piece(piece)

        self.add_player(player_dark)
        self.add_player(player_light)
        self.current_player = PlayerLbl.DARK
        self.selected_piece = None
        self.game_over = False
        self.game_result = None
        self.steps = []

    def handle_piece_selection(self, mouse_pos):
        c, r = mouse_pos[0] // SPAN, mouse_pos[1] // SPAN
        for piece in self.players[self.current_player].pieces.values():
            if piece.pos == (c, r):
                self.selected_piece = piece
                return True
        return False

    def handle_piece_move(self, mouse_pos):
        if not self.selected_piece:
            return False

        src_pos = self.selected_piece.pos
        des_pos = (mouse_pos[0] // SPAN, mouse_pos[1] // SPAN)

        if self.can_move(self.selected_piece, src_pos, des_pos):
            self.selected_piece.pos = des_pos
            self.steps.append(Step(self.current_player.value, self.selected_piece.name, des_pos))
            self.handle_captures(des_pos)
            self.switch_player()
            self.selected_piece = None
            return True
        return False

    def can_move(self, selected_piece, src_pos, des_pos):
        if not (0 <= des_pos[0] < W and 0 <= des_pos[1] < H):
            return False
        if abs(src_pos[0] - des_pos[0]) + abs(src_pos[1] - des_pos[1]) > 1:
            return False
        if src_pos == des_pos:
            return False
        if src_pos[0] != des_pos[0] and src_pos[1] != des_pos[1]:
            return False
        if des_pos in self.RIVERS and not isinstance(selected_piece, Rat):
            if isinstance(selected_piece, (Lion, Tiger)):
                return self.is_jumping_over_river(src_pos, des_pos)
            return False
        if des_pos in self.TRAPS[self.current_player] or des_pos == self.DENS[self.current_player]:
            return False
        if des_pos == self.DENS[self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT]:
            return True
        for piece in self.players[self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT].pieces.values():
            if piece.pos == des_pos:
                return True
        return True

    def is_jumping_over_river(self, src_pos, des_pos):
        jump_poss = []
        if src_pos[0] == des_pos[0]:
            jump_poss = [(src_pos[0], y) for y in range(min(src_pos[1], des_pos[1]) + 1, max(src_pos[1], des_pos[1]))]
        elif src_pos[1] == des_pos[1]:
            jump_poss = [(x, src_pos[1]) for x in range(min(src_pos[0], des_pos[0]) + 1, max(src_pos[0], des_pos[0]))]
        for pos in jump_poss:
            if pos in self.RIVERS:
                for piece in self.players.values():
                    if isinstance(piece, Rat) and piece.pos == pos:
                        return False
        return True

    def handle_captures(self, des_pos):
        opponent = self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT
        opponent_pieces = self.players[opponent].pieces
        for name, piece in list(opponent_pieces.items()):
            if piece.pos == des_pos:
                del opponent_pieces[name]
        if des_pos == self.DENS[opponent]:
            self.game_over = True
            self.game_result = f'{self.current_player.value} Wins!'

    def check_game_end(self):
        for lbl, player in self.players.items():
            if not self.players[PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT].pieces:
                self.game_over = True
                self.game_result = f"{lbl} Wins by capturing all opponent's pieces!"
                return
        if not self.game_over:
            self.game_result = "Game continues..."

    def draw_game(self):
        '''
        Draw game board, pieces, and other elements
        '''
        _screen.fill(Color.WHITE.value)

        # Draw rivers
        river_idx = 0
        river_img_count = len(self.RIVER_IMGS)
        for c in range(W):
            for r in range(H):
                if (c, r) in self.RIVERS:
                    _screen.blit(self.RIVER_IMGS[river_idx % river_img_count], (c * SPAN, r * SPAN))
                    river_idx += 1
                else:
                    pygame.draw.rect(_screen, Color.WHITE.value, [c * SPAN, r * SPAN, SPAN, SPAN], 0)
                pygame.draw.rect(_screen, Color.GRAY.value, pygame.Rect(c * SPAN, r * SPAN, SPAN, SPAN), 1)

        # Draw dens
        for den in self.DENS.values():
            _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/den.png'), CELL_SIZE), (den[0] * SPAN, den[1] * SPAN))

        # Draw traps
        for traps in self.TRAPS.values():
            for trap in traps:
                _screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images/trap.png'), CELL_SIZE), (trap[0] * SPAN, trap[1] * SPAN))

        # Draw pieces
        for player in self.players.values():
            for piece in player.pieces.values():
                self.draw_star(_screen, player.lbl == PlayerLbl.DARK and Color.ORANGE.value or Color.CYAN.value, (piece.pos[0] * SPAN + 50, piece.pos[1] * SPAN + 50), 40, 20, 192, 20)
                _screen.blit(piece.img, (piece.pos[0] * SPAN, piece.pos[1] * SPAN))

        # Highlight possible moves for the selected piece
        if self.selected_piece:
            for move in self.highlight_possible_moves(self.selected_piece, self.players[self.current_player].pieces[self.selected_piece].pos):
                highlight_surface = pygame.Surface((SPAN, SPAN), pygame.SRCALPHA)
                pygame.draw.circle(highlight_surface, (*Color.YELLOW.value, 192), (SPAN // 2, SPAN // 2), SPAN // 3)
                _screen.blit(highlight_surface, (move[0] * SPAN, move[1] * SPAN))

        # Update the display
        pygame.display.flip()

    def draw_star(self, surface, color, center, outer_radius, inner_radius, opacity=255, num_points=5):
        '''
        Draw a star on the game board
        
        Args:
        - surface: The game surface
        - color: The color of the star
        - center: The center position of the star
        - outer_radius: The outer radius of the star
        - inner_radius: The inner radius of the star
        - opacity: The opacity of the star
        - num_points: The number of points on the star
        
        Example:
        >>> draw_star(_screen, Color.ORANGE.value, (100, 100), 40, 20, 192, 20)
        '''
        star_points = []
        for i in range(num_points * 2):
            radius = outer_radius if i % 2 == 0 else inner_radius
            angle = i * math.pi / num_points
            star_points.append((center[0] + int(math.cos(angle) * radius), center[1] + int(math.sin(angle) * radius)))
        pygame.draw.polygon(surface, color + (opacity,), star_points)


    def highlight_possible_moves(self, piece_lbl, pos):
        '''
        Highlight possible moves on the game board

        Args:
        - piece_lbl: The label of the piece
        - pos: The position of the piece

        Example:
        >>> highlight_possible_moves(PieceLbl.LION.value, (3, 4))
        '''
        possible_moves = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            end_pos = (pos[0] + dx, pos[1] + dy)
            if self.can_move(piece_lbl, pos, end_pos):
                possible_moves.append(end_pos)
        return possible_moves

_game_manager = Manager()

# Other imports and initial setup code remain unchanged

def draw_screen(game_manager, end_game=False):
    _screen.blit(_cover_scaled, (0, 0))
    txt_tit = _font_tit.render(NAME, True, Color.WHITE.value)
    _screen.blit(txt_tit, txt_tit.get_rect(center=(SIZE[0] / 2, 25)))

    if game_manager.game_over:
        txt_game_over = _font_res.render(game_manager.game_result, True, Color.YELLOW.value)
        _screen.blit(txt_game_over, txt_game_over.get_rect(center=(SIZE[0] / 2, SIZE[1] / 2)))

    _screen.blit(_start_btn_scaled, _start_btn_rect.topleft)
    mouse_pos = pygame.mouse.get_pos()
    if _start_btn_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        txt_color = Color.YELLOW.value
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        txt_color = Color.WHITE.value
    txt_surf = _font_btn.render('New Game', True, txt_color)
    _screen.blit(txt_surf, txt_surf.get_rect(center=_start_btn_rect.center))
    pygame.display.flip()

def main():
    running = True
    _game_manager.initialize_game()

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if _start_btn_rect.collidepoint(mouse_pos):
                    _game_manager.initialize_game()  # Reset the game state here
                    continue  # Skip to the next iteration to avoid processing other mouse events
                if not _game_manager.game_over:
                    if _game_manager.handle_piece_selection(mouse_pos):
                        continue
                    else:
                        moved = _game_manager.handle_piece_move(mouse_pos)
                        if moved:
                            _game_manager.check_game_end()
                            if _game_manager.game_over:
                                # Optionally, display some end game information
                                continue
        draw_screen(_game_manager)
        _clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
