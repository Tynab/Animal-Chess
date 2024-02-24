
from enum import Enum, auto
from pygame import image, transform
from scripts.game import GameConstant

class CellLabel(Enum):
    '''
    The label of the cell.
    
    Attributes:
        EMPTY (auto): The empty cell.
        RIVER (auto): The river cell.
        DARK_TRAP (auto): The dark trap cell.
        LIGHT_TRAP (auto): The light trap cell.
        DARK_DEN (auto): The dark den cell.
        LIGHT_DEN (auto): The light den cell.
    '''
    EMPTY = auto
    RIVER = auto
    DARK_TRAP = auto
    LIGHT_TRAP = auto
    DARK_DEN = auto
    LIGHT_DEN = auto

class CellPosition(Enum):
    '''
    The position of the cell.

    Attributes:
        RIVER_1_1 (tuple): The position of the river 1-1 cell.
        RIVER_1_2 (tuple): The position of the river 1-2 cell.
        RIVER_1_3 (tuple): The position of the river 1-3 cell.
        RIVER_1_4 (tuple): The position of the river 1-4 cell.
        RIVER_1_5 (tuple): The position of the river 1-5 cell.
        RIVER_1_6 (tuple): The position of the river 1-6 cell.
        RIVER_2_1 (tuple): The position of the river 2-1 cell.
        RIVER_2_2 (tuple): The position of the river 2-2 cell.
        RIVER_2_3 (tuple): The position of the river 2-3 cell.
        RIVER_2_4 (tuple): The position of the river 2-4 cell.
        RIVER_2_5 (tuple): The position of the river 2-5 cell.
        RIVER_2_6 (tuple): The position of the river 2-6 cell.
        DARK_TRAP_1 (tuple): The position of the dark trap 1 cell.
        DARK_TRAP_2 (tuple): The position of the dark trap 2 cell.
        DARK_TRAP_3 (tuple): The position of the dark trap 3 cell.
        LIGHT_TRAP_1 (tuple): The position of the light trap 1 cell.
        LIGHT_TRAP_2 (tuple): The position of the light trap 2 cell.
        LIGHT_TRAP_3 (tuple): The position of the light trap 3 cell.
        DARK_DEN (tuple): The position of the dark den cell.
        LIGHT_DEN (tuple): The position of the light den cell.
        DARK_RAT (tuple): The position of the dark rat cell.
        DARK_CAT (tuple): The position of the dark cat cell.
        DARK_DOG (tuple): The position of the dark dog cell.
        DARK_WOLF (tuple): The position of the dark wolf cell.
        DARK_LEOPARD (tuple): The position of the dark leopard cell.
        DARK_TIGER (tuple): The position of the dark tiger cell.
        DARK_LION (tuple): The position of the dark lion cell.
        DARK_ELEPHANT (tuple): The position of the dark elephant cell.
        LIGHT_RAT (tuple): The position of the light rat cell.
        LIGHT_CAT (tuple): The position of the light cat cell.
        LIGHT_DOG (tuple): The position of the light dog cell.
        LIGHT_WOLF (tuple): The position of the light wolf cell.
        LIGHT_LEOPARD (tuple): The position of the light leopard cell.
        LIGHT_TIGER (tuple): The position of the light tiger cell.
        LIGHT_LION (tuple): The position of the light lion cell.
        LIGHT_ELEPHANT (tuple): The position of the light elephant cell.
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

class CellImage(Enum):
    '''
    The image of the cell.
    '''
    DEN = 'assets/images/den.png'
    TRAP = 'assets/images/trap.png'
    RIVER_1 = 'assets/images/rivers/river_1.png'
    RIVER_2 = 'assets/images/rivers/river_2.png'
    RIVER_3 = 'assets/images/rivers/river_3.png'
    RIVER_4 = 'assets/images/rivers/river_4.png'
    RIVER_5 = 'assets/images/rivers/river_5.png'
    RIVER_6 = 'assets/images/rivers/river_6.png'

class Cell:
    '''
    The cell of the board.
    '''
    def __init__(self, label, position):
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def set_label(self, label):
        '''
        Set the label of the cell.
        
        Args:
            label (CellLabel): The label of the cell.
        '''
        self.label = label

    def set_image(self, image_path):
        '''
        Set the image of the cell.
        
        Args:
            image_path (str): The path of the image.
        '''
        self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)

    def add_piece(self, piece):
        '''
        Add a piece to the cell.
        
        Args:
            piece (Piece): The piece to be added.
        '''
        self.piece = piece

    def remove_piece(self):
        '''
        Remove the piece from the cell.
        '''
        self.piece = None

    def is_in_board(self):
        '''
        Check if the cell is in the board.
        
        Returns:
            bool: True if the cell is in the board, False otherwise.
        '''
        return 0 <= self.position[0] < GameConstant.WIDTH.value and 0 <= self.position[1] < GameConstant.HEIGHT.value
    
    def is_empty(self):
        '''
        Check if the cell is empty.
        
        Returns:
            bool: True if the cell is empty, False otherwise.
        '''
        return self.piece is None
    
    def is_river(self):
        '''
        Check if the cell is river.
        
        Returns:
            bool: True if the cell is river, False otherwise.
        '''
        return self.label == CellLabel.RIVER
    
    def is_opponent_trap(self, side):
        '''
        Check if the cell is opponent trap.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: True if the cell is opponent trap, False otherwise.
        '''
        if self.label in [CellLabel.DARK_TRAP, CellLabel.LIGHT_TRAP]:
            return self.label.value != side
        return False
    
    def is_opponent_den(self, side):
        '''
        Check if the cell is opponent den.
        
        Args:
            side (PlayerSide): The side of the player.
            
        Returns:
            bool: True if the cell is opponent den, False otherwise.
        '''
        if self.label in [CellLabel.DARK_DEN, CellLabel.LIGHT_DEN]:
            return self.label.value != side
        return False
    
    def is_occupied_by_own_piece(self, side):
        '''
        Check if the cell is occupied by own piece.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: True if the cell is occupied by own piece, False otherwise.
        '''
        return self.piece and self.piece.side == side

