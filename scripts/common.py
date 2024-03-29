W = 7
H = 9
FPS = 60
TIT = 'Animal Chess'
SPAN = 100

class Size:
    '''
    A class that represents the sizes of various elements in the game.

    Attributes:
    - BOARD (tuple): The size of the game board.
    - SUBSCREEN (tuple): The size of the subscreen.
    - TOTAL (tuple): The total size of the game window.
    - CELL (tuple): The size of each cell on the game board.
    - ARTWORK (tuple): The size of the artwork images.
    - START_BTN (tuple): The size of the start button.
    - PADDING (tuple): The padding size for elements.
    '''
    BOARD = (W * SPAN, H * SPAN)
    SUBSCREEN = (500, BOARD[1])
    TOTAL = (BOARD[0] + SUBSCREEN[0], BOARD[1])
    CELL = (SPAN, SPAN)
    ARTWORK = (480, 480)
    START_BTN = (190, 50)
    PADDING = (10, 10)

class ImagePath:
    '''
    A class that represents the file paths to various images used in the game.

    Attributes:
    - COVER (str): The file path to the cover image.
    - START_BTN (str): The file path to the start button image.
    - GUIDE (str): The file path to the guide image.
    - CARD (str): The file path to the card image.
    '''
    COVER = 'assets/images/cover.png'
    START_BTN = 'assets/images/button.png'
    GUIDE = 'assets/images/guide.png'
    CARD = 'assets/images/card.png'

class FontName:
    '''
    A class that represents the names of various fonts used in the game.

    Attributes:
    - TIT (str): The name of the font used for titles, 'Garamond'.
    - BTN (str): The name of the font used for buttons, 'Lato'.
    - TXT (str): The name of the font used for general text, 'Arial'.
    '''
    TIT = 'Garamond'
    BTN = 'Lato'
    TXT = 'Arial'

class Color:
    '''
    The color of the pieces.
    
    Attributes:
    - BLACK (tuple): The color black.
    - WHITE (tuple): The color white.
    - RED (tuple): The color red.
    - ORANGE (tuple): The color orange.
    - YELLOW (tuple): The color yellow.
    - GREEN (tuple): The color green.
    - BLUE (tuple): The color blue.
    - PINK (tuple): The color pink.
    - PURPLE (tuple): The color purple.
    - CYAN (tuple): The color cyan.
    - GREY (tuple): The color grey.

    Methods:
    - star_color(side): Returns the color of the star based on the player side.
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
    GREY = (128, 128, 128)

    @staticmethod
    def star_color(side):
        '''
        Returns the color of the star based on the player side.

        Args:
            side (str): The player side.

        Returns:
            tuple: The color of the star.
        '''
        return PlayerSide.is_dark(side) and Color.ORANGE or Color.CYAN

class GameMode:
    '''
    A class that represents the game modes.

    Attributes:
    - PvP (int): Player vs Player game mode.
    - PvC (int): Player vs Computer game mode.
    - CvC (int): Computer vs Computer game mode.

    Methods:
    - is_pvp(mode): Check if the mode is player vs player.
    - is_pvc(mode): Check if the mode is player vs computer.
    - is_cvc(mode): Check if the mode is computer vs computer.
    '''
    PvP = 1
    PvC = 2
    CvC = 3

    @staticmethod
    def is_pvp(mode):
        '''
        Check if the mode is player vs player.

        Args:
            mode (int): The mode.

        Returns:
            bool: True if the mode is player vs player, False otherwise.
        '''
        return mode == GameMode.PvP
    
    @staticmethod
    def is_pvc(mode):
        '''
        Check if the mode is player vs computer.

        Args:
            mode (int): The mode.

        Returns:
            bool: True if the mode is player vs computer, False otherwise.
        '''
        return mode == GameMode.PvC
    
    @staticmethod
    def is_cvc(mode):
        '''
        Check if the mode is computer vs computer.

        Args:
            mode (int): The mode.

        Returns:
            bool: True if the mode is computer vs computer, False otherwise.
        '''
        return mode == GameMode.CvC

class GameState:
    '''
    The state of the game.
    
    Attributes:
    - NEW (int): The new game state.
    - RUNNING (int): The running game state.
    - OVER (int): The over game state.

    Methods:
    - is_new(state): Check if the state is new.
    - is_running(state): Check if the state is running.
    - is_over(state): Check if the state is over.
    '''
    NEW = 1
    RUNNING = 2
    OVER = 3

    @staticmethod
    def is_new(state):
        '''
        Check if the state is new.

        Args:
            state (int): The state.

        Returns:
            bool: True if the state is new, False otherwise.
        '''
        return state == GameState.NEW
    
    @staticmethod
    def is_running(state):
        '''
        Check if the state is running.

        Args:
            state (int): The state.

        Returns:
            bool: True if the state is running, False otherwise.
        '''
        return state == GameState.RUNNING
    
    @staticmethod
    def is_over(state):
        '''
        Check if the state is over.

        Args:
            state (int): The state.

        Returns:
            bool: True if the state is over, False otherwise.
        '''
        return state == GameState.OVER

class PlayerSide:
    '''
    The side of the player.

    Attributes:
    - DARK (str): The dark side.
    - LIGHT (str): The light side.

    Methods:
    - is_dark(side): Check if the side is dark.
    - is_light(side): Check if the side is light.
    - player_den_position(side): Get the den position of the side.
    - opponent_den_position(side): Get the den position of the side.
    - player_of(side): Get the player side.
    - opponent_of(side): Get the opponent side.
    '''
    DARK = 'Dark'
    LIGHT = 'Light'

    @staticmethod
    def is_dark(side):
        '''
        Check if the side is dark.

        Args:
            side (str): The side.

        Returns:
            bool: True if the side is dark, False otherwise.
        '''
        return side == PlayerSide.DARK
    
    @staticmethod
    def is_light(side):
        '''
        Check if the side is light.

        Args:
            side (str): The side.

        Returns:
            bool: True if the side is light, False otherwise.
        '''
        return side == PlayerSide.LIGHT
    
    @staticmethod
    def player_den_position(side):
        '''
        Get the den position of the side.

        Args:
            side (str): The side.

        Returns:
            tuple: The den position.
        '''
        return PlayerSide.is_dark(side) and CellPosition.DARK_DEN or CellPosition.LIGHT_DEN

    @staticmethod
    def opponent_den_position(side):
        '''
        Get the den position of the side.

        Args:
            side (str): The side.

        Returns:
            tuple: The den position.
        '''
        return PlayerSide.is_dark(side) and CellPosition.LIGHT_DEN or CellPosition.DARK_DEN
    
    @staticmethod
    def player_of(side):
        '''
        Get the player side.

        Args:
            side (str): The side.

        Returns:
            str: The player side.
        '''
        return side

    @staticmethod
    def opponent_of(side):
        '''
        Get the opponent side.

        Args:
            side (str): The side.

        Returns:
            str: The opponent side.
        '''
        return PlayerSide.is_dark(side) and PlayerSide.LIGHT or PlayerSide.DARK

class CellLabel:
    '''
    The label of the cell.
    
    Attributes:
    - EMPTY (int): Represents an empty cell.
    - RIVER (int): Represents a river cell.
    - DARK_TRAP (int): Represents a trap cell for the dark side.
    - LIGHT_TRAP (int): Represents a trap cell for the light side.
    - DARK_DEN (int): Represents a den cell for the dark side.
    - LIGHT_DEN (int): Represents a den cell for the light side.

    Methods:
    - is_empty(label): Check if the label is empty.
    - is_river(label): Check if the label is a river.
    - is_dark_trap(label): Check if the label is a dark trap.
    - is_light_trap(label): Check if the label is a light trap.
    - is_trap(label): Check if the label is a trap.
    - is_player_trap(label, side): Check if the label is a player trap.
    - is_opponent_trap(label, side): Check if the label is an opponent trap.
    - is_dark_den(label): Check if the label is a dark den.
    - is_light_den(label): Check if the label is a light den.
    - is_den(label): Check if the label is a den.
    - is_player_den(label, side): Check if the label is a player den.
    - is_opponent_den(label, side): Check if the label is an opponent den.
    '''
    EMPTY = 1
    RIVER = 2
    DARK_TRAP = 3
    LIGHT_TRAP = 4
    DARK_DEN = 5
    LIGHT_DEN = 6

    @staticmethod
    def is_empty(label):
        '''
        Check if the label is empty.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is empty, False otherwise.
        '''
        return label == CellLabel.EMPTY
    
    @staticmethod
    def is_river(label):
        '''
        Check if the label is a river.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a river, False otherwise.
        '''
        return label == CellLabel.RIVER
    
    @staticmethod
    def is_dark_trap(label):
        '''
        Check if the label is a dark trap.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a dark trap, False otherwise.
        '''
        return label == CellLabel.DARK_TRAP
    
    @staticmethod
    def is_light_trap(label):
        '''
        Check if the label is a light trap.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a light trap, False otherwise.
        '''
        return label == CellLabel.LIGHT_TRAP
    
    @staticmethod
    def is_trap(label):
        '''
        Check if the label is a trap.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a trap, False otherwise.
        '''
        return CellLabel.is_dark_trap(label) or CellLabel.is_light_trap(label)
    
    @staticmethod
    def is_player_trap(label, side):
        '''
        Check if the label is a player trap.

        Args:
            label (int): The label.
            side (str): The side.

        Returns:
            bool: True if the label is a player trap, False otherwise.
        '''
        return CellLabel.is_dark_trap(label) and PlayerSide.is_dark(side) or CellLabel.is_light_trap(label) and PlayerSide.is_light(side)

    @staticmethod
    def is_opponent_trap(label, side):
        '''
        Check if the label is an opponent trap.

        Args:
            label (int): The label.
            side (str): The side.

        Returns:
            bool: True if the label is an opponent trap, False otherwise.
        '''
        return CellLabel.is_dark_trap(label) and PlayerSide.is_light(side) or CellLabel.is_light_trap(label) and PlayerSide.is_dark(side)

    @staticmethod
    def is_dark_den(label):
        '''
        Check if the label is a dark den.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a dark den, False otherwise.
        '''
        return label == CellLabel.DARK_DEN
    
    @staticmethod
    def is_light_den(label):
        '''
        Check if the label is a light den.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a light den, False otherwise.
        '''
        return label == CellLabel.LIGHT_DEN
    
    @staticmethod
    def is_den(label):
        '''
        Check if the label is a den.

        Args:
            label (int): The label.

        Returns:
            bool: True if the label is a den, False otherwise.
        '''
        return CellLabel.is_dark_den(label) or CellLabel.is_light_den(label)
    
    @staticmethod
    def is_player_den(label, side):
        '''
        Check if the label is a player den.

        Args:
            label (int): The label.
            side (str): The side.

        Returns:
            bool: True if the label is a player den, False otherwise.
        '''
        return CellLabel.is_dark_den(label) and PlayerSide.is_dark(side) or CellLabel.is_light_den(label) and PlayerSide.is_light(side)
    
    @staticmethod
    def is_opponent_den(label, side):
        '''
        Check if the label is an opponent den.

        Args:
            label (int): The label.
            side (str): The side.

        Returns:
            bool: True if the label is an opponent den, False otherwise.
        '''
        return CellLabel.is_dark_den(label) and PlayerSide.is_light(side) or CellLabel.is_light_den(label) and PlayerSide.is_dark(side)
    
class CellPosition:
    '''
    The position of the cell.

    Attributes:
    - RIVER_1_1 (tuple): The position of the river 1-1 cell.
    - RIVER_1_2 (tuple): The position of the river 1-2 cell.
    - RIVER_1_3 (tuple): The position of the river 1-3 cell.
    - RIVER_1_4 (tuple): The position of the river 1-4 cell.
    - RIVER_1_5 (tuple): The position of the river 1-5 cell.
    - RIVER_1_6 (tuple): The position of the river 1-6 cell.
    - RIVER_2_1 (tuple): The position of the river 2-1 cell.
    - RIVER_2_2 (tuple): The position of the river 2-2 cell.
    - RIVER_2_3 (tuple): The position of the river 2-3 cell.
    - RIVER_2_4 (tuple): The position of the river 2-4 cell.
    - RIVER_2_5 (tuple): The position of the river 2-5 cell.
    - RIVER_2_6 (tuple): The position of the river 2-6 cell.
    - DARK_TRAP_1 (tuple): The position of the dark trap 1 cell.
    - DARK_TRAP_2 (tuple): The position of the dark trap 2 cell.
    - DARK_TRAP_3 (tuple): The position of the dark trap 3 cell.
    - LIGHT_TRAP_1 (tuple): The position of the light trap 1 cell.
    - LIGHT_TRAP_2 (tuple): The position of the light trap 2 cell.
    - LIGHT_TRAP_3 (tuple): The position of the light trap 3 cell.
    - DARK_DEN (tuple): The position of the dark den cell.
    - LIGHT_DEN (tuple): The position of the light den cell.
    - DARK_RAT (tuple): The position of the dark rat cell.
    - DARK_CAT (tuple): The position of the dark cat cell.
    - DARK_DOG (tuple): The position of the dark dog cell.
    - DARK_WOLF (tuple): The position of the dark wolf cell.
    - DARK_LEOPARD (tuple): The position of the dark leopard cell.
    - DARK_TIGER (tuple): The position of the dark tiger cell.
    - DARK_LION (tuple): The position of the dark lion cell.
    - DARK_ELEPHANT (tuple): The position of the dark elephant cell.
    - LIGHT_RAT (tuple): The position of the light rat cell.
    - LIGHT_CAT (tuple): The position of the light cat cell.
    - LIGHT_DOG (tuple): The position of the light dog cell.
    - LIGHT_WOLF (tuple): The position of the light wolf cell.
    - LIGHT_LEOPARD (tuple): The position of the light leopard cell.
    - LIGHT_TIGER (tuple): The position of the light tiger cell.
    - LIGHT_LION (tuple): The position of the light lion cell.
    - LIGHT_ELEPHANT (tuple): The position of the light elephant cell.

    Methods:
    - rat(side): Get the position of the rat.
    - cat(side): Get the position of the cat.
    - dog(side): Get the position of the dog.
    - wolf(side): Get the position of the wolf.
    - leopard(side): Get the position of the leopard.
    - tiger(side): Get the position of the tiger.
    - lion(side): Get the position of the lion.
    - elephant(side): Get the position of the elephant.
    '''
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
    DARK_CAT = (5, 1)
    DARK_DOG = (1, 1)
    DARK_WOLF = (4, 2)
    DARK_LEOPARD = (2, 2)
    DARK_TIGER = (6, 0)
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

    @staticmethod
    def rat(side):
        '''
        Get the position of the rat.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the rat.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_RAT or CellPosition.LIGHT_RAT
    
    @staticmethod
    def cat(side):
        '''
        Get the position of the cat.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the cat.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_CAT or CellPosition.LIGHT_CAT
    
    @staticmethod
    def dog(side):
        '''
        Get the position of the dog.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the dog.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_DOG or CellPosition.LIGHT_DOG
    
    @staticmethod
    def wolf(side):
        '''
        Get the position of the wolf.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the wolf.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_WOLF or CellPosition.LIGHT_WOLF
    
    @staticmethod
    def leopard(side):
        '''
        Get the position of the leopard.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the leopard.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_LEOPARD or CellPosition.LIGHT_LEOPARD
    
    @staticmethod
    def tiger(side):
        '''
        Get the position of the tiger.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the tiger.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_TIGER or CellPosition.LIGHT_TIGER
    
    @staticmethod
    def lion(side):
        '''
        Get the position of the lion.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the lion.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_LION or CellPosition.LIGHT_LION
    
    @staticmethod
    def elephant(side):
        '''
        Get the position of the elephant.

        Args:
            side (str): The side.

        Returns:
            tuple: The position of the elephant.
        '''
        return side == PlayerSide.DARK and CellPosition.DARK_ELEPHANT or CellPosition.LIGHT_ELEPHANT

class CellImage:
    '''
    The image of the cell.

    Attributes:
    - DEN (str): The den image.
    - TRAP (str): The trap image.
    - RIVER_1 (str): The river 1 image.
    - RIVER_2 (str): The river 2 image.
    - RIVER_3 (str): The river 3 image.
    - RIVER_4 (str): The river 4 image.
    - RIVER_5 (str): The river 5 image.
    - RIVER_6 (str): The river 6 image.
    '''
    DEN = 'assets/images/den.png'
    TRAP = 'assets/images/trap.png'
    RIVER_1 = 'assets/images/rivers/river_1.png'
    RIVER_2 = 'assets/images/rivers/river_2.png'
    RIVER_3 = 'assets/images/rivers/river_3.png'
    RIVER_4 = 'assets/images/rivers/river_4.png'
    RIVER_5 = 'assets/images/rivers/river_5.png'
    RIVER_6 = 'assets/images/rivers/river_6.png'

class PieceName:
    '''
    The name of the piece.
    
    Attributes:
    - DARK_RAT (str): The name of the dark rat.
    - DARK_CAT (str): The name of the dark cat.
    - DARK_DOG (str): The name of the dark dog.
    - DARK_WOLF (str): The name of the dark wolf.
    - DARK_LEOPARD (str): The name of the dark leopard.
    - DARK_TIGER (str): The name of the dark tiger.
    - DARK_LION (str): The name of the dark lion.
    - DARK_ELEPHANT (str): The name of the dark elephant.
    - LIGHT_RAT (str): The name of the light rat.
    - LIGHT_CAT (str): The name of the light cat.
    - LIGHT_DOG (str): The name of the light dog.
    - LIGHT_WOLF (str): The name of the light wolf.
    - LIGHT_LEOPARD (str): The name of the light leopard.
    - LIGHT_TIGER (str): The name of the light tiger.
    - LIGHT_LION (str): The name of the light lion.
    - LIGHT_ELEPHANT (str): The name of the light elephant.

    Methods:
    - rat(side): Get the name of the rat.
    - cat(side): Get the name of the cat.
    - dog(side): Get the name of the dog.
    - wolf(side): Get the name of the wolf.
    - leopard(side): Get the name of the leopard.
    - tiger(side): Get the name of the tiger.
    - lion(side): Get the name of the lion.
    - elephant(side): Get the name of the elephant.
    '''
    DARK_RAT = 'Rat'
    DARK_CAT = 'Sphynx'
    DARK_DOG = 'Saluki'
    DARK_WOLF = 'Grey Wolf'
    DARK_LEOPARD = 'Black Panther'
    DARK_TIGER = 'White Tiger'
    DARK_LION = 'Smilodon'
    DARK_ELEPHANT = 'Mammoth'
    LIGHT_RAT = 'Mouse'
    LIGHT_CAT = 'Wildcat'
    LIGHT_DOG = 'Pitbull'
    LIGHT_WOLF = 'Silver Fang'
    LIGHT_LEOPARD = 'Siberi Leopard'
    LIGHT_TIGER = 'Bengal Tiger'
    LIGHT_LION = 'Panthera Leo'
    LIGHT_ELEPHANT = 'Loxodonta'

    @staticmethod
    def rat(side):
        '''
        Get the name of the rat.

        Args:
            side (str): The side.

        Returns:
            str: The name of the rat.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT
    
    @staticmethod
    def cat(side):
        '''
        Get the name of the cat.

        Args:
            side (str): The side.

        Returns:
            str: The name of the cat.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_CAT or PieceName.LIGHT_CAT
    
    @staticmethod
    def dog(side):
        '''
        Get the name of the dog.

        Args:
            side (str): The side.

        Returns:
            str: The name of the dog.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG
    
    @staticmethod
    def wolf(side):
        '''
        Get the name of the wolf.

        Args:
            side (str): The side.

        Returns:
            str: The name of the wolf.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_WOLF or PieceName.LIGHT_WOLF
    
    @staticmethod
    def leopard(side):
        '''
        Get the name of the leopard.

        Args:
            side (str): The side.

        Returns:
            str: The name of the leopard.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_LEOPARD or PieceName.LIGHT_LEOPARD
    
    @staticmethod
    def tiger(side):
        '''
        Get the name of the tiger.

        Args:
            side (str): The side.

        Returns:
            str: The name of the tiger.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_TIGER or PieceName.LIGHT_TIGER
    
    @staticmethod
    def lion(side):
        '''
        Get the name of the lion.

        Args:
            side (str): The side.

        Returns:
            str: The name of the lion.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION
    
    @staticmethod
    def elephant(side):
        '''
        Get the name of the elephant.

        Args:
            side (str): The side.

        Returns:
            str: The name of the elephant.
        '''
        return side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT

class PieceDetail:
    '''
    The detail of the piece.
    
    Attributes:
    - RAT (str): The detail of the rat.
    - CAT (str): The detail of the cat.
    - DOG (str): The detail of the dog.
    - WOLF (str): The detail of the wolf.
    - LEOPARD (str): The detail of the leopard.
    - TIGER (str): The detail of the tiger.
    - LION (str): The detail of the lion.
    - ELEPHANT (str): The detail of the elephant.
    '''
    RAT = """Effect:
- The Rat can enter the River region.
- The Rat has the lowest rank but can defeat an Elephant at the highest rank. This is explained by the Rat running into the ear and nibbling on the Elephant's brain."""
    CAT = """Description: The Cat can defeat the Rat."""
    DOG = """Description: The Dog can defeat the Cat and Rat.
Effect: The Dog can enter the River region."""
    WOLF = """Description: The Wolf can defeat the Dog, Cat and Rat."""
    LEOPARD = """Description: The Leopard can defeat the Wolf, Dog, Cat and Rat."""
    TIGER = """Description: The Tiger can defeat the Leopard, Wolf, Dog, Cat and Rat."""
    LION = """Description: The Lion can defeat the Tiger, Leopard, Wolf, Dog, Cat and Rat."""
    ELEPHANT = """Description: The Elephant can defeat the Lion, Tiger, Leopard, Wolf, Dog and Cat."""

class PieceAtk:
    '''
    The attack of the piece.
    
    Attributes:
    - RAT (int): The attack of the rat.
    - CAT (int): The attack of the cat.
    - DOG (int): The attack of the dog.
    - WOLF (int): The attack of the wolf.
    - LEOPARD (int): The attack of the leopard.
    - TIGER (int): The attack of the tiger.
    - LION (int): The attack of the lion.
    - ELEPHANT (int): The attack of the elephant.
    '''
    RAT = 1
    CAT = 2
    DOG = 3
    WOLF = 4
    LEOPARD = 5
    TIGER = 6
    LION = 7
    ELEPHANT = 8

class PieceAvatar:
    '''
    The avatar of the piece.
    
    Attributes:
    - DARK_RAT (str): The avatar of the dark rat.
    - DARK_CAT (str): The avatar of the dark cat.
    - DARK_DOG (str): The avatar of the dark dog.
    - DARK_WOLF (str): The avatar of the dark wolf.
    - DARK_LEOPARD (str): The avatar of the dark leopard.
    - DARK_TIGER (str): The avatar of the dark tiger.
    - DARK_LION (str): The avatar of the dark lion.
    - DARK_ELEPHANT (str): The avatar of the dark elephant.
    - LIGHT_RAT (str): The avatar of the light rat.
    - LIGHT_CAT (str): The avatar of the light cat.
    - LIGHT_DOG (str): The avatar of the light dog.
    - LIGHT_WOLF (str): The avatar of the light wolf.
    - LIGHT_LEOPARD (str): The avatar of the light leopard.
    - LIGHT_TIGER (str): The avatar of the light tiger.
    - LIGHT_LION (str): The avatar of the light lion.
    - LIGHT_ELEPHANT (str): The avatar of the light elephant.

    Methods:
    - rat(side): Get the avatar of the rat.
    - cat(side): Get the avatar of the cat.
    - dog(side): Get the avatar of the dog.
    - wolf(side): Get the avatar of the wolf.
    - leopard(side): Get the avatar of the leopard.
    - tiger(side): Get the avatar of the tiger.
    - lion(side): Get the avatar of the lion.
    - elephant(side): Get the avatar of the elephant.
    '''
    DARK_RAT = 'assets/pieces/dark/rat.png'
    DARK_CAT = 'assets/pieces/dark/cat.png'
    DARK_DOG = 'assets/pieces/dark/dog.png'
    DARK_WOLF = 'assets/pieces/dark/wolf.png'
    DARK_LEOPARD = 'assets/pieces/dark/leopard.png'
    DARK_TIGER = 'assets/pieces/dark/tiger.png'
    DARK_LION = 'assets/pieces/dark/lion.png'
    DARK_ELEPHANT = 'assets/pieces/dark/elephant.png'
    LIGHT_RAT = 'assets/pieces/light/rat.png'
    LIGHT_CAT = 'assets/pieces/light/cat.png'
    LIGHT_DOG = 'assets/pieces/light/dog.png'
    LIGHT_WOLF = 'assets/pieces/light/wolf.png'
    LIGHT_LEOPARD = 'assets/pieces/light/leopard.png'
    LIGHT_TIGER = 'assets/pieces/light/tiger.png'
    LIGHT_LION = 'assets/pieces/light/lion.png'
    LIGHT_ELEPHANT = 'assets/pieces/light/elephant.png'

    @staticmethod
    def rat(side):
        '''
        Get the avatar of the rat.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the rat.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_RAT or PieceAvatar.LIGHT_RAT
    
    @staticmethod
    def cat(side):
        '''
        Get the avatar of the cat.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the cat.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_CAT or PieceAvatar.LIGHT_CAT
    
    @staticmethod
    def dog(side):
        '''
        Get the avatar of the dog.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the dog.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_DOG or PieceAvatar.LIGHT_DOG
    
    @staticmethod
    def wolf(side):
        '''
        Get the avatar of the wolf.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the wolf.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_WOLF or PieceAvatar.LIGHT_WOLF
    
    @staticmethod
    def leopard(side):
        '''
        Get the avatar of the leopard.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the leopard.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_LEOPARD or PieceAvatar.LIGHT_LEOPARD
    
    @staticmethod
    def tiger(side):
        '''
        Get the avatar of the tiger.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the tiger.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_TIGER or PieceAvatar.LIGHT_TIGER
    
    @staticmethod
    def lion(side):
        '''
        Get the avatar of the lion.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the lion.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_LION or PieceAvatar.LIGHT_LION
    
    @staticmethod
    def elephant(side):
        '''
        Get the avatar of the elephant.

        Args:
            side (str): The side.

        Returns:
            str: The avatar of the elephant.
        '''
        return side == PlayerSide.DARK and PieceAvatar.DARK_ELEPHANT or PieceAvatar.LIGHT_ELEPHANT

class PieceArtWork:
    '''
    The artwork of the piece.
    
    Attributes:
    - DARK_RAT (str): The artwork of the dark rat.
    - DARK_CAT (str): The artwork of the dark cat.
    - DARK_DOG (str): The artwork of the dark dog.
    - DARK_WOLF (str): The artwork of the dark wolf.
    - DARK_LEOPARD (str): The artwork of the dark leopard.
    - DARK_TIGER (str): The artwork of the dark tiger.
    - DARK_LION (str): The artwork of the dark lion.
    - DARK_ELEPHANT (str): The artwork of the dark elephant.
    - LIGHT_RAT (str): The artwork of the light rat.
    - LIGHT_CAT (str): The artwork of the light cat.
    - LIGHT_DOG (str): The artwork of the light dog.
    - LIGHT_WOLF (str): The artwork of the light wolf.
    - LIGHT_LEOPARD (str): The artwork of the light leopard.
    - LIGHT_TIGER (str): The artwork of the light tiger.
    - LIGHT_LION (str): The artwork of the light lion.
    - LIGHT_ELEPHANT (str): The artwork of the light elephant.

    Methods:
    - rat(side): Get the artwork of the rat.
    - cat(side): Get the artwork of the cat.
    - dog(side): Get the artwork of the dog.
    - wolf(side): Get the artwork of the wolf.
    - leopard(side): Get the artwork of the leopard.
    - tiger(side): Get the artwork of the tiger.
    - lion(side): Get the artwork of the lion.
    - elephant(side): Get the artwork of the elephant.
    '''
    DARK_RAT = 'assets/artworks/dark/rat.png'
    DARK_CAT = 'assets/artworks/dark/cat.png'
    DARK_DOG = 'assets/artworks/dark/dog.png'
    DARK_WOLF = 'assets/artworks/dark/wolf.png'
    DARK_LEOPARD = 'assets/artworks/dark/leopard.png'
    DARK_TIGER = 'assets/artworks/dark/tiger.png'
    DARK_LION = 'assets/artworks/dark/lion.png'
    DARK_ELEPHANT = 'assets/artworks/dark/elephant.png'
    LIGHT_RAT = 'assets/artworks/light/rat.png'
    LIGHT_CAT = 'assets/artworks/light/cat.png'
    LIGHT_DOG = 'assets/artworks/light/dog.png'
    LIGHT_WOLF = 'assets/artworks/light/wolf.png'
    LIGHT_LEOPARD = 'assets/artworks/light/leopard.png'
    LIGHT_TIGER = 'assets/artworks/light/tiger.png'
    LIGHT_LION = 'assets/artworks/light/lion.png'
    LIGHT_ELEPHANT = 'assets/artworks/light/elephant.png'

    @staticmethod
    def rat(side):
        '''
        Get the artwork of the rat.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the rat.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_RAT or PieceArtWork.LIGHT_RAT
    
    @staticmethod
    def cat(side):
        '''
        Get the artwork of the cat.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the cat.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_CAT or PieceArtWork.LIGHT_CAT
    
    @staticmethod
    def dog(side):
        '''
        Get the artwork of the dog.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the dog.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_DOG or PieceArtWork.LIGHT_DOG
    
    @staticmethod
    def wolf(side):
        '''
        Get the artwork of the wolf.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the wolf.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_WOLF or PieceArtWork.LIGHT_WOLF
    
    @staticmethod
    def leopard(side):
        '''
        Get the artwork of the leopard.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the leopard.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_LEOPARD or PieceArtWork.LIGHT_LEOPARD
    
    @staticmethod
    def tiger(side):
        '''
        Get the artwork of the tiger.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the tiger.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_TIGER or PieceArtWork.LIGHT_TIGER
    
    @staticmethod
    def lion(side):
        '''
        Get the artwork of the lion.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the lion.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_LION or PieceArtWork.LIGHT_LION
    
    @staticmethod
    def elephant(side):
        '''
        Get the artwork of the elephant.

        Args:
            side (str): The side.

        Returns:
            str: The artwork of the elephant.
        '''
        return side == PlayerSide.DARK and PieceArtWork.DARK_ELEPHANT or PieceArtWork.LIGHT_ELEPHANT
