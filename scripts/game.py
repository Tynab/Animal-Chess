from enum import Enum, auto

class GameConstant(Enum):
    WIDTH = 7
    HEIGHT = 9
    FPS = 60
    TITLE = 'Animal Chess'
    SPAN = 100
    SIZE = (WIDTH * SPAN, HEIGHT * SPAN)
    CELL_SIZE = (SPAN, SPAN)
    ARTWORK_SIZE = (500, 500)
    START_BTN_SIZE = (190, 50)

class GameStatus(Enum):
    NEW = auto
    RUNNING = auto
    OVER = auto
