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

# Piece labels
class PieceLbl(Enum):
    ELEPHANT = 'Elephant'
    LION = 'Lion'
    TIGER = 'Tiger'
    LEOPARD = 'Leopard'
    WOLF = 'Wolf'
    DOG = 'Dog'
    CAT = 'Cat'
    RAT = 'Rat'

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
    def __init__(self, name, lbl, desc, pos, atk, img_path, art_path):
        '''
        Initializes a Piece object.

        Args:
        - name: The name of the piece.
        - lbl: The label of the piece.
        - desc: The description of the piece.
        - pos: The position of the piece on the board.
        - atk: The attack power of the piece.
        - img_path: The file path to the image of the piece.
        - art_path: The file path to the artwork of the piece.

        Example:
        >>> piece = Piece('Mammoth', PieceLbl.ELEPHANT, 'Elephant of the Challenger', (4, 2), 8, 'assets/pieces/dark/elephant.png', 'assets/artworks/dark/elephant.png')
        '''
        self.name = name
        self.lbl = lbl
        self.desc = desc
        self.pos = pos
        self.atk = atk
        self.img = pygame.transform.scale(pygame.image.load(img_path), CELL_SIZE)
        self.art = pygame.transform.scale(pygame.image.load(art_path), CELL_SIZE)

class Player:
    def __init__(self, name, lbl):
        '''
        Represents a player in the game.

        Args:
        - name: The name of the player.
        - lbl: The label of the player.

        Example:
        >>> player = Player('Player', PlayerLbl.LIGHT)
        '''
        self.name = name
        self.lbl = lbl
        self.pieces = {}

    def add_piece(self, piece):
        '''
        Add a piece to the player's pieces.

        Args:
        - piece: An instance of the Piece class

        Example:
        >>> player.add_piece(piece)
        '''
        self.pieces[piece.lbl] = piece

class Step:
    def __init__(self, player_lbl_name, piece_lbl_name, des_pos):
        '''
        Represents a step taken by a player in the game.

        Args:
        - player_lbl_name: The name of the player label making the move.
        - piece_lbl_name: The name of the piece label being moved.
        - des_pos: The position to which the piece is being moved.

        Example:
        >>> step = Step('Player', PieceLbl.Lion.value, (3, 4))
        '''
        self.player_lbl_name = player_lbl_name
        self.piece_lbl_name = piece_lbl_name
        self.des_pos = des_pos

class Manager:
    def __init__(self):
        '''
        Initialize the game manager

        Attributes:
        - players: A dictionary containing the players in the game
        - steps: A list containing the steps taken by the players
        - current_player: The current player
        - game_over: A boolean indicating whether the game is over
        - game_result: The result of the game
        - selected_piece: The piece selected by the current player
        - RIVERS: A list of positions representing the river squares
        - DENS: A dictionary containing the positions of the dens for each player
        - TRAPS: A dictionary containing the positions of the traps for each player

        Methods:
        - add_player: Add a player to the game
        - switch_player: Switch the current player
        - initialize_game: Initialize the game
        - handle_piece_selection: Handle piece selection
        - handle_piece_move: Handle piece movement
        - can_move: Check if a piece can move to a new position
        - is_jumping_over_river: Check if a piece is jumping over a river
        - handle_captures: Handle captures or special conditions when a piece moves to a new position
        - check_game_end: Check game end conditions
        - draw_game: Draw game board, pieces, and other elements
        - draw_star: Draw a star on the game board
        - highlight_possible_moves: Highlight possible moves

        Example:
        >>> game_manager = Manager()
        '''
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
        '''
        Initialize the game
        '''
        player_dark = Player('Computer', PlayerLbl.DARK)
        player_light = Player('Player', PlayerLbl.LIGHT)
        pieces_dark = [
            Piece('Mammoth', PieceLbl.ELEPHANT, 'Elephant of the Challenger', (0, 2), 8, 'assets/pieces/dark/elephant.png', 'assets/artworks/dark/elephant.png'),
            Piece('Smilodon', PieceLbl.LION, 'Lion of the Challenger', (6, 0), 7, 'assets/pieces/dark/lion.png', 'assets/artworks/dark/lion.png'),
            Piece('White Tiger', PieceLbl.TIGER, 'Tiger of the Challenger', (0, 0), 6, 'assets/pieces/dark/tiger.png', 'assets/artworks/dark/tiger.png'),
            Piece('Black Panther', PieceLbl.LEOPARD, 'Leopard of the Challenger', (4, 2), 5, 'assets/pieces/dark/leopard.png', 'assets/artworks/dark/leopard.png'),
            Piece('Grey Wolf', PieceLbl.WOLF, 'Wolf of the Challenger', (2, 2), 4, 'assets/pieces/dark/wolf.png', 'assets/artworks/dark/wolf.png'),
            Piece('Saluki', PieceLbl.DOG, 'Dog of the Challenger', (5, 1), 3, 'assets/pieces/dark/dog.png', 'assets/artworks/dark/dog.png'),
            Piece('Sphynx', PieceLbl.CAT, 'Cat of the Challenger', (1, 1), 2, 'assets/pieces/dark/cat.png', 'assets/artworks/dark/cat.png'),
            Piece('Rat', PieceLbl.RAT, 'Rat of the Challenger', (6, 2), 1, 'assets/pieces/dark/rat.png', 'assets/artworks/dark/rat.png')
        ]
        pieces_light = [
            Piece('Loxodonta', PieceLbl.ELEPHANT, 'Elephant of the Protector', (6, 6), 8, 'assets/pieces/light/elephant.png', 'assets/artworks/light/elephant.png'),
            Piece('Panthera Leo', PieceLbl.LION, 'Lion of the Protector', (0, 8), 7, 'assets/pieces/light/lion.png', 'assets/artworks/light/lion.png'),
            Piece('Bengal Tiger', PieceLbl.TIGER, 'Tiger of the Protector', (6, 8), 6, 'assets/pieces/light/tiger.png', 'assets/artworks/light/tiger.png'),
            Piece('Siberi Leopard', PieceLbl.LEOPARD, 'Leopard of the Protector', (2, 6), 5, 'assets/pieces/light/leopard.png', 'assets/artworks/light/leopard.png'),
            Piece('Silver Fang', PieceLbl.WOLF, 'Wolf of the Protector', (4, 6), 4, 'assets/pieces/light/wolf.png', 'assets/artworks/light/wolf.png'),
            Piece('Pitbull', PieceLbl.DOG, 'Dog of the Protector', (1, 7), 3, 'assets/pieces/light/dog.png', 'assets/artworks/light/dog.png'),
            Piece('Wildcat', PieceLbl.CAT, 'Cat of the Protector', (5, 7), 2, 'assets/pieces/light/cat.png', 'assets/artworks/light/cat.png'),
            Piece('Rat', PieceLbl.RAT, 'Rat of the Protector', (0, 6), 1, 'assets/pieces/light/rat.png', 'assets/artworks/light/rat.png')
        ]

        # Add pieces to players
        for piece in pieces_dark:
            player_dark.add_piece(piece)
        for piece in pieces_light:
            player_light.add_piece(piece)

        # Add players to the game
        self.add_player(player_dark)
        self.add_player(player_light)

        # Reset game state variables
        self.current_player = PlayerLbl.DARK
        self.selected_piece = None
        self.game_over = False
        self.game_result = None
        self.steps = []

    def handle_piece_selection(self, mouse_pos):
        '''
        Handle piece selection

        Args:
        - mouse_pos: The position of the mouse click

        Returns:
        - A boolean indicating whether a piece has been selected

        Example:
        >>> handle_piece_selection((100, 100))
        True
        '''
        c, r = mouse_pos[0] // SPAN, mouse_pos[1] // SPAN
        for piece_lbl, piece in self.players[self.current_player].pieces.items():
            if piece.pos == (c, r):
                self.selected_piece = piece_lbl
                return True
        return False

    def handle_piece_move(self, mouse_pos):
        '''
        Handle piece movement

        Args:
        - mouse_pos: The position of the mouse click

        Returns:
        - A boolean indicating whether the move was successful

        Example:
        >>> handle_piece_move((100, 100))
        True
        '''
        # Return False if no piece is selected
        if not self.selected_piece:
            return False

        selected_piece = self.players[self.current_player].pieces[self.selected_piece]
        src_pos = selected_piece.pos
        des_pos = (mouse_pos[0] // SPAN, mouse_pos[1] // SPAN)

        # Move the selected piece to the new position if possible
        if self.can_move(selected_piece.lbl, src_pos, des_pos):
            selected_piece.pos = des_pos
            self.steps.append(Step(self.current_player.value, selected_piece.lbl.value, des_pos))
            self.handle_captures(des_pos)
            self.switch_player()
            self.selected_piece = None
            return True
        return False

    def can_move(self, piece_lbl, src_pos, des_pos):
        '''
        Check if a piece can move to a new position

        Args:
        - piece_lbl: The label of the piece
        - src_pos: The source position of the piece
        - des_pos: The destination position of the piece

        Returns:
        - A boolean indicating whether the move is valid

        Example:
        >>> can_move(PieceLbl.LION.value, (3, 4), (3, 5))
        True
        '''
        # # Check if the move is within the board
        # if not (0 <= des_pos[0] < W and 0 <= des_pos[1] < H):
        #     return False

        # # Check if the move is within the same row or column
        # if abs(src_pos[0] - des_pos[0]) + abs(src_pos[1] - des_pos[1]) != 1:
        #     return False

        # # Check if the piece is moving to a river square
        # if piece_lbl not in [PieceLbl.DOG, PieceLbl.RAT] and des_pos in self.RIVERS:
        #     return False

        # # Check if the piece is moving to its own den
        # opp = self.current_player == PlayerLbl.DARK and PlayerLbl.LIGHT or PlayerLbl.DARK
        # if des_pos in self.TRAPS[opp]:
        #     for opp_piece in self.players[opp].pieces.values():
        #         if opp_piece.pos == des_pos:
        #             return False

        # # Check if the piece is moving to an opponent's den
        # for opp_piece_lbl, opp_piece in self.players[opp].pieces.items():
        #     if opp_piece.pos == des_pos:
        #         return self.can_defeat(piece_lbl, opp_piece_lbl)

        # # Check if the piece is moving to a trap
        # for piece in self.players[self.current_player].pieces.values():
        #     if piece.pos == des_pos:
        #         return False

        # return True
    
        # Check if the destination position is within the game board
        if not (0 <= des_pos[0] < W and 0 <= des_pos[1] < H):
            return False

        # Check if the destination position is within one square of the source position
        if abs(src_pos[0] - des_pos[0]) + abs(src_pos[1] - des_pos[1]) > 1:
            return False

        # Check if the destination position is not the same as the source position
        if src_pos == des_pos:
            return False

        # Restrict diagonal moves
        if src_pos[0] != des_pos[0] and src_pos[1] != des_pos[1]:
            return False

        # River rules
        if des_pos in self.RIVERS and piece_lbl != PieceLbl.RAT:
            if piece_lbl in [PieceLbl.LION, PieceLbl.TIGER]:
                return self.is_jumping_over_river(src_pos, des_pos)
            return False

        # Trap and Den rules
        if des_pos in self.TRAPS[self.current_player] or des_pos == self.DENS[self.current_player]:
            return False

        # Denying entry into own den
        if des_pos == self.DENS[self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT]:
            return True

        # Check for piece at destination
        for piece in self.players[self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT].pieces.values():
            if piece.pos == des_pos:
                return True

        return True

    def is_jumping_over_river(self, src_pos, des_pos):
        '''
        Check if a piece is jumping over a river

        Args:
        - src_pos: The source position of the piece
        - des_pos: The destination position of the piece

        Returns:
        - A boolean indicating whether the piece is jumping over a river

        Example:
        >>> is_jumping_over_river((3, 4), (3, 6))
        True
        '''
        jump_poss = []
        if src_pos[0] == des_pos[0]:
            jump_poss = [(src_pos[0], y) for y in range(
                min(src_pos[1], des_pos[1]) + 1, max(src_pos[1], des_pos[1]))]
        elif src_pos[1] == des_pos[1]:
            jump_poss = [(x, src_pos[1]) for x in range(
                min(src_pos[0], des_pos[0]) + 1, max(src_pos[0], des_pos[0]))]

        # Check if a rat is blocking the jump
        for pos in jump_poss:
            if pos in self.RIVERS:
                for player in self.players.values():
                    for piece in player.pieces.values():
                        if piece.pos == pos and piece.lbl == PieceLbl.RAT:
                            return False
        return True

    def handle_captures(self, des_pos):
        '''
        Handle captures or special conditions when a piece moves to a new position

        Args:
        - des_pos: The destination position of the piece

        Example:
        >>> handle_captures((3, 4))
        '''
        opp = self.current_player == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT
        opp_pieces = self.players[opp].pieces
        for lbl, piece in list(opp_pieces.items()):
            if piece.pos == des_pos:
                del opp_pieces[lbl]

        if des_pos == self.DENS[opp]:
            self.game_over = True
            self.game_result = f'{self.current_player.value} Wins!'

    def check_game_end(self):
        '''
        Check game end conditions
        '''
        # Check for win by moving into the opponent's den
        for lbl, player in self.players.items():
            for piece in player.pieces.values():
                if piece.pos == self.DENS[lbl == PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT]:
                    self.game_over = True
                    self.game_result = f"{lbl} Wins by entering the opponent's den!"
                    return

        # Check for win by capturing all opponent's pieces
        for lbl, player in self.players.items():
            if not self.players[PlayerLbl.LIGHT and PlayerLbl.DARK or PlayerLbl.LIGHT].pieces:
                self.game_over = True
                self.game_result = f"{lbl} Wins by capturing all opponent's pieces!"
                return

        # If no win condition met, game continues
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

def draw_screen(game_manager, end_game=False):
    '''
    Draw the game screen

    Args:
    - game_manager: An instance of the Manager class
    - end_game: A boolean indicating whether the game has ended

    Example:
    >>> draw_screen(game_manager)
    '''
    game_manager.draw_game()
    if end_game:
        txt_game_over = _font_res.render(game_manager.game_result, True, Color.YELLOW.value)
        _screen.blit(txt_game_over, txt_game_over.get_rect(center=(SIZE[0] / 2, SIZE[1] / 2)))
    pygame.display.flip()


def main():
    '''
    Main function to run the game
    '''
    running = True
    _game_manager.initialize_game()

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN and not _game_manager.game_over:
                mouse_pos = pygame.mouse.get_pos()
                if _game_manager.handle_piece_selection(mouse_pos):
                    pass
                else:
                    moved = _game_manager.handle_piece_move(mouse_pos)
                    if moved:
                        _game_manager.check_game_end()
                        if _game_manager.game_over:
                            draw_screen(_game_manager, end_game=True)
                            continue

        draw_screen(_game_manager)
        _clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
