from enum import Enum

class Color(Enum):
    '''
    The color of the pieces.
    
    Attributes:
        BLACK (tuple): The color black.
        WHITE (tuple): The color white.
        RED (tuple): The color red.
        ORANGE (tuple): The color orange.
        YELLOW (tuple): The color yellow.
        GREEN (tuple): The color green.
        BLUE (tuple): The color blue.
        PINK (tuple): The color pink.
        PURPLE (tuple): The color purple.
        CYAN (tuple): The color cyan.
        GRAY (tuple): The color gray.
    '''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PINK = (255, 192, 203)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    GRAY = (128, 128, 128)
