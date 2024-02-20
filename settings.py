from enum import Enum, auto
from pygame import image, transform

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

class PlayerSide(Enum):
    DARK = 'Dark'
    LIGHT = 'Light'

class CellLabel(Enum):
    EMPTY = auto
    RIVER = auto
    DARK_TRAP = auto
    LIGHT_TRAP = auto
    DARK_DEN = auto
    LIGHT_DEN = auto

class PieceLabel(Enum):
    DARK_RAT = auto
    DARK_CAT = auto
    DARK_DOG = auto
    DARK_WOLF = auto
    DARK_LEOPARD = auto
    DARK_TIGER = auto
    DARK_LION = auto
    DARK_ELEPHANT = auto
    LIGHT_RAT = auto
    LIGHT_CAT = auto
    LIGHT_DOG = auto
    LIGHT_WOLF = auto
    LIGHT_LEOPARD = auto
    LIGHT_TIGER = auto
    LIGHT_LION = auto
    LIGHT_ELEPHANT = auto

class GameStatus(Enum):
    NEW = auto
    RUNNING = auto
    OVER = auto

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

class Avatar(Enum):
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

class ArtWork(Enum):
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

class Detail(Enum):
    RAT = """ATK: 1
The Rat can enter the River region.
The Rat has the lowest rank but can defeat an Elephant at the highest rank. This is explained by the Rat running into the ear and nibbling on the Elephant's brain."""
    CAT = """ATK: 2
The Cat can defeat the Rat."""
    DOG = """ATK: 3
The Dog can enter the River region.
The Dog can defeat the Cat and Rat."""
    WOLF = """ATK: 4
The Wolf can defeat the Dog, Cat and Rat."""
    LEOPARD = """ATK: 5
The Leopard can defeat the Wolf, Dog, Cat and Rat."""
    TIGER = """ATK: 6
The Tiger can defeat the Leopard, Wolf, Dog, Cat and Rat."""
    LION = """ATK: 7
The Lion can defeat the Tiger, Leopard, Wolf, Dog, Cat and Rat."""
    ELEPHANT = """ATK: 8
The Elephant can defeat the Lion, Tiger, Leopard, Wolf, Dog and Cat."""

class Cell:
    def __init__(self, label, position, image_path=None, piece=None):
        self.label = label
        self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)
        self.position = position
        self.piece = piece

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def is_empty(self):
        return self.piece is None
    
    def is_river(self):
        return self.label == CellLabel.RIVER
    
    def is_opponent_trap(self, side):
        return (self.label == CellLabel.DARK_TRAP and side == PlayerSide.LIGHT) or (self.label == CellLabel.LIGHT_TRAP and side == PlayerSide.DARK)
    
    def is_opponent_den(self, side):
        return (self.label == CellLabel.DARK_DEN and side == PlayerSide.LIGHT) or (self.label == CellLabel.LIGHT_DEN and side == PlayerSide.DARK)
    
    def is_occupied_by_own_piece(self, side):
        return self.piece and self.piece.side == side
    
    def is_defeated_by_own_piece(self, piece):
        if self.piece and self.piece.side != piece.side:
            if isinstance(self.piece, Rat):
                return isinstance(piece, Elephant)
            return self.piece.atk >= piece.atk
        return False

class Piece:
    def __init__(self, name, detail, position, atk, side, image_path, artwork_path):
        self.name = name
        self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)
        self.artwork_ = transform.scale(image.load(artwork_path), GameConstant.ARTWORK_SIZE.value)
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side
        self.alive = True
        self.selected = False

    def move(self, position):
        self.position = position

    def available_moves(self):
        available_moves = []
        left = 
        if isinstance(self, Rat):
            return self.rat_moves(game_state)
        
    def left(self, step):
        return (self.position[0] - step, self.position[1])
    
    def right(self, step):
        return (self.position[0] + step, self.position[1])
    
    def up(self, step):
        return (self.position[0], self.position[1] - step)
    
    def down(self, step):
        return (self.position[0], self.position[1] + step)
    
    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

class Rat(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Rat', Detail.RAT, Position.DARK_RAT, 1, side, Avatar.DARK_RAT, ArtWork.DARK_RAT)
        else:
            super().__init__('Mouse', Detail.RAT, Position.LIGHT_RAT, 1, side, Avatar.LIGHT_RAT, ArtWork.LIGHT_RAT)

class Cat(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Sphynx', Detail.CAT, Position.DARK_CAT, 2, side, Avatar.DARK_CAT, ArtWork.DARK_CAT)
        else:
            super().__init__('Wildcat', Detail.CAT, Position.LIGHT_CAT, 2, side, Avatar.LIGHT_CAT, ArtWork.LIGHT_CAT)

class Dog(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Saluki', Detail.DOG, Position.DARK_DOG, 3, side, Avatar.DARK_DOG, ArtWork.DARK_DOG)
        else:
            super().__init__('Pitbull', Detail.DOG, Position.LIGHT_DOG, 3, side, Avatar.LIGHT_DOG, ArtWork.LIGHT_DOG)

class Wolf(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Grey Wolf', Detail.WOLF, Position.DARK_WOLF, 4, side, Avatar.DARK_WOLF, ArtWork.DARK_WOLF)
        else:
            super().__init__('Silver Fang', Detail.WOLF, Position.LIGHT_WOLF, 4, side, Avatar.LIGHT_WOLF, ArtWork.LIGHT_WOLF)

class Leopard(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Black Panther', Detail.LEOPARD, Position.DARK_LEOPARD, 5, side, Avatar.DARK_LEOPARD, ArtWork.DARK_LEOPARD)
        else:
            super().__init__('Siberi Leopard', Detail.LEOPARD, Position.LIGHT_LEOPARD, 5, side, Avatar.LIGHT_LEOPARD, ArtWork.LIGHT_LEOPARD)

class Tiger(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('White Tiger', Detail.TIGER, Position.DARK_TIGER, 6, side, Avatar.DARK_TIGER, ArtWork.DARK_TIGER)
        else:
            super().__init__('Bengal Tiger', Detail.TIGER, Position.LIGHT_TIGER, 6, side, Avatar.LIGHT_TIGER, ArtWork.LIGHT_TIGER)

class Lion(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Smilodon', Detail.LION, Position.DARK_LION, 7, side, Avatar.DARK_LION, ArtWork.DARK_LION)
        else:
            super().__init__('Panthera Leo', Detail.LION, Position.LIGHT_LION, 7, side, Avatar.LIGHT_LION, ArtWork.LIGHT_LION)

class Elephant(Piece):
    def __init__(self, side):
        if side == PlayerSide.DARK:
            super().__init__('Mammoth', Detail.ELEPHANT, Position.DARK_ELEPHANT, 8, side, Avatar.DARK_ELEPHANT, ArtWork.DARK_ELEPHANT)
        else:
            super().__init__('Loxodonta', Detail.ELEPHANT, Position.LIGHT_ELEPHANT, 8, side, Avatar.LIGHT_ELEPHANT, ArtWork.LIGHT_ELEPHANT)

class Player:
    def __init__(self, side):
        self.side = side
        self.pieces = [Rat(side), Cat(side), Dog(side), Wolf(side), Leopard(side), Tiger(side), Lion(side), Elephant(side)]