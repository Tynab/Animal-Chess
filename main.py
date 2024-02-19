import pygame
from enum import Enum

pygame.init()

class Game(Enum):
    WIDTH = 7
    HEIGHT = 9
    FPS = 60
    TITLE = 'Animal Chess'
    SPAN = 100
    SIZE = (WIDTH * SPAN, HEIGHT * SPAN)
    CELL_SIZE = (SPAN, SPAN)
    START_BTN_SIZE = (190, 50)

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

class PlayerLabel(Enum):
    DARK = 'Dark'
    LIGHT = 'Light'

class CellLabel(Enum):
    EMPTY = 'Empty'
    RIVER = 'River'
    DARK_TRAP = 'DarkTrap'
    LIGHT_TRAP = 'LightTrap'
    DARK_DEN = 'DarkDen'
    LIGHT_DEN = 'LightDen'

class PieceLabel(Enum):
    DARK_RAT = 'DarkRat'
    DARK_CAT = 'DarkCat'
    DARK_DOG = 'DarkDog'
    DARK_WOLF = 'DarkWolf'
    DARK_LEOPARD = 'DarkLeopard'
    DARK_TIGER = 'DarkTiger'
    DARK_LION = 'DarkLion'
    DARK_ELEPHANT = 'DarkElephant'
    LIGHT_RAT = 'LightRat'
    LIGHT_CAT = 'LightCat'
    LIGHT_DOG = 'LightDog'
    LIGHT_WOLF = 'LightWolf'
    LIGHT_LEOPARD = 'LightLeopard'
    LIGHT_TIGER = 'LightTiger'
    LIGHT_LION = 'LightLion'
    LIGHT_ELEPHANT = 'LightElephant'

class Position(Enum):
    RIVER_1_1 = (1, 3)
    RIVER_1_2 = (2, 3)
    RIVER_1_3 = (1, 4)
    RIVER_1_4 = (2, 4)
    RIVER_1_5 = (1, 5)
    RIVER_1_6 = (2, 5)
    RIVER_2_1 = (4, 3)
    RIVER_2_2 = (5, 3)
    RIVER_2_3 = (4, 4)
    RIVER_2_4 = (5, 4)
    RIVER_2_5 = (4, 5)
    RIVER_2_6 = (5, 5)
    DARK_TRAP_1 = (3, 1)
    DARK_TRAP_2 = (2, 0)
    DARK_TRAP_3 = (4, 0)
    LIGHT_TRAP_1 = (3, 7)
    LIGHT_TRAP_2 = (2, 8)
    LIGHT_TRAP_3 = (4, 8)
    DARK_DEN = (3, 0)
    LIGHT_DEN = (3, 8)
    DARK_RAT = (0, 2)
    DARK_CAT = (1, 5)
    DARK_DOG = (1, 1)
    DARK_WOLF = (4, 2)
    DARK_LEOPARD = (2, 2)
    DARK_TIGER = (0, 6)
    DARK_LION = (0, 0)
    DARK_ELEPHANT = (6, 2)
    LIGHT_RAT = (6, 6)
    LIGHT_CAT = (1, 7)
    LIGHT_DOG = (5, 7)
    LIGHT_WOLF = (2, 6)
    LIGHT_LEOPARD = (4, 6)
    LIGHT_TIGER = (0, 8)
    LIGHT_LION = (6, 8)
    LIGHT_ELEPHANT = (0, 6)

_screen = pygame.display.set_mode(Game.SIZE.value)

pygame.display.set_caption(Game.TITLE.value)

_clock = pygame.time.Clock()