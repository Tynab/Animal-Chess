
from enum import Enum, auto
from pygame import image, transform
from scripts.game import GameConstant

class CellLabel(Enum):
    EMPTY = auto
    RIVER = auto
    DARK_TRAP = auto
    LIGHT_TRAP = auto
    DARK_DEN = auto
    LIGHT_DEN = auto

class CellPosition(Enum):
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
    DEN = 'assets/images/den.png'
    TRAP = 'assets/images/trap.png'
    RIVER_1 = 'assets/images/rivers/river_1.png'
    RIVER_2 = 'assets/images/rivers/river_2.png'
    RIVER_3 = 'assets/images/rivers/river_3.png'
    RIVER_4 = 'assets/images/rivers/river_4.png'
    RIVER_5 = 'assets/images/rivers/river_5.png'
    RIVER_6 = 'assets/images/rivers/river_6.png'

class Cell:
    def __init__(self, label, position):
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def set_label(self, label):
        self.label = label

    def set_image(self, image_path):
        self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def is_in_board(self):
        return 0 <= self.position[0] < GameConstant.WIDTH.value and 0 <= self.position[1] < GameConstant.HEIGHT.value
    
    def is_empty(self):
        return self.piece is None
    
    def is_river(self):
        return self.label == CellLabel.RIVER
    
    def is_opponent_trap(self, side):
        if self.label in [CellLabel.DARK_TRAP, CellLabel.LIGHT_TRAP]:
            return self.label.value != side
        return False
    
    def is_opponent_den(self, side):
        if self.label in [CellLabel.DARK_DEN, CellLabel.LIGHT_DEN]:
            return self.label.value != side
        return False
    
    def is_occupied_by_own_piece(self, side):
        return self.piece and self.piece.side == side
    
    def is_defeated_by_own_piece(self, piece):
        if self.piece and self.piece.side != piece.side:
            if isinstance(piece, Rat) and isinstance(self.piece, Elephant):
                return True
            if isinstance(self.piece, Rat) and isinstance(piece, Elephant):
                return False
            return self.piece.atk >= piece.atk
        return False
