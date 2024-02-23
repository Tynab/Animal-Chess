from enum import Enum, auto
from pygame import image, transform
from scripts.game import GameConstant

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

class PieceName(Enum):
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

class PieceDetail(Enum):
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

class PieceAtk(Enum):
    RAT = 1
    CAT = 2
    DOG = 3
    WOLF = 4
    LEOPARD = 5
    TIGER = 6
    LION = 7
    ELEPHANT = 8

class PieceAvatar(Enum):
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

class PieceArtWork(Enum):
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

class Piece:
    def __init__(self, name, detail, position, atk, side, image_path, artwork_path):
        self.name = name
        self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)
        self.artwork_ = transform.scale(image.load(artwork_path), GameConstant.ARTWORK_SIZE.value)
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side
        self.selected = False

    def set_can_swim(self, can_swim):
        self.can_swim = can_swim

    def set_can_jump(self, can_jump):
        self.can_jump = can_jump

    def move(self, position):
        self.position = position

    def left(self, step, board):
        return board.get_cell((self.position[0] - step, self.position[1]))
    
    def right(self, step, board):
        return board.get_cell((self.position[0] + step, self.position[1]))
    
    def up(self, step, board):
        return board.get_cell((self.position[0], self.position[1] - step))
    
    def down(self, step, board):
        return board.get_cell((self.position[0], self.position[1] + step))
    
    def is_defeated_by_own_piece(self, cell):
        if cell.piece is None:
            return True
        return self.atk >= cell.piece.atk
    
    def is_move_valid(self, cell):
        if not cell.is_in_board():
            return False
        if cell.is_river():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if not self.is_defeated_by_own_piece(cell):
            return False
        return True
    
    def available_moves(self, board):
        moves = []
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)
            if self.is_move_valid(next_cell):
                moves.append(next_cell)
        return moves
    
    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False
