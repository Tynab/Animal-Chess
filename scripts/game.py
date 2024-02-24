from enum import Enum, auto

class GameConstant(Enum):
    '''
    The constant of the game.
    
    Attributes:
        WIDTH (int): The width of the game.
        HEIGHT (int): The height of the game.
        FPS (int): The frame per second of the game.
        TITLE (str): The title of the game.
        SPAN (int): The span of the game.
        SIZE (tuple): The size of the game.
        CELL_SIZE (tuple): The size of the cell.
        ARTWORK_SIZE (tuple): The size of the artwork.
        START_BTN_SIZE (tuple): The size of the start button.
    '''
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
    '''
    The status of the game.
    
    Attributes:
        NEW (auto): The game is new.
        RUNNING (auto): The game is running.
        OVER (auto): The game is over.
    '''
    NEW = auto
    RUNNING = auto
    OVER = auto
