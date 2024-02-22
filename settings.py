from enum import Enum, auto
from pygame import image, transform

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

class Atk(Enum):
    RAT = 1
    CAT = 2
    DOG = 3
    WOLF = 4
    LEOPARD = 5
    TIGER = 6
    LION = 7
    ELEPHANT = 8

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

class Board:
    def __init__(self):
        self.cells = [[Cell(CellLabel.EMPTY, (x, y)) for y in range(GameConstant.HEIGHT.value)] for x in range(GameConstant.WIDTH.value)]
        self.cells[Position.RIVER_1_1.value[0]][Position.RIVER_1_1.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_1_2.value[0]][Position.RIVER_1_2.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_1_3.value[0]][Position.RIVER_1_3.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_1_4.value[0]][Position.RIVER_1_4.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_1_5.value[0]][Position.RIVER_1_5.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_1_6.value[0]][Position.RIVER_1_6.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_1.value[0]][Position.RIVER_2_1.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_2.value[0]][Position.RIVER_2_2.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_3.value[0]][Position.RIVER_2_3.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_4.value[0]][Position.RIVER_2_4.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_5.value[0]][Position.RIVER_2_5.value[1]].label = CellLabel.RIVER
        self.cells[Position.RIVER_2_6.value[0]][Position.RIVER_2_6.value[1]].label = CellLabel.RIVER
        self.cells[Position.DARK_TRAP_1.value[0]][Position.DARK_TRAP_1.value[1]].label = CellLabel.DARK_TRAP
        self.cells[Position.DARK_TRAP_2.value[0]][Position.DARK_TRAP_2.value[1]].label = CellLabel.DARK_TRAP
        self.cells[Position.DARK_TRAP_3.value[0]][Position.DARK_TRAP_3.value[1]].label = CellLabel.DARK_TRAP
        self.cells[Position.LIGHT_TRAP_1.value[0]][Position.LIGHT_TRAP_1.value[1]].label = CellLabel.LIGHT_TRAP
        self.cells[Position.LIGHT_TRAP_2.value[0]][Position.LIGHT_TRAP_2.value[1]].label = CellLabel.LIGHT_TRAP
        self.cells[Position.LIGHT_TRAP_3.value[0]][Position.LIGHT_TRAP_3.value[1]].label = CellLabel.LIGHT_TRAP
        self.cells[Position.DARK_DEN.value[0]][Position.DARK_DEN.value[1]].label = CellLabel.DARK_DEN
        self.cells[Position.LIGHT_DEN.value[0]][Position.LIGHT_DEN.value[1]].label = CellLabel.LIGHT_DEN
        self.cells[Position.DARK_RAT.value[0]][Position.DARK_RAT.value[1]].add_piece(Rat(PlayerSide.DARK))
        self.cells[Position.DARK_CAT.value[0]][Position.DARK_CAT.value[1]].add_piece(Cat(PlayerSide.DARK))
        self.cells[Position.DARK_DOG.value[0]][Position.DARK_DOG.value[1]].add_piece(Dog(PlayerSide.DARK))
        self.cells[Position.DARK_WOLF.value[0]][Position.DARK_WOLF.value[1]].add_piece(Wolf(PlayerSide.DARK))
        self.cells[Position.DARK_LEOPARD.value[0]][Position.DARK_LEOPARD.value[1]].add_piece(Leopard(PlayerSide.DARK))
        self.cells[Position.DARK_TIGER.value[0]][Position.DARK_TIGER.value[1]].add_piece(Tiger(PlayerSide.DARK))
        self.cells[Position.DARK_LION.value[0]][Position.DARK_LION.value[1]].add_piece(Lion(PlayerSide.DARK))
        self.cells[Position.DARK_ELEPHANT.value[0]][Position.DARK_ELEPHANT.value[1]].add_piece(Elephant(PlayerSide.DARK))
        self.cells[Position.LIGHT_RAT.value[0]][Position.LIGHT_RAT.value[1]].add_piece(Rat(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_CAT.value[0]][Position.LIGHT_CAT.value[1]].add_piece(Cat(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_DOG.value[0]][Position.LIGHT_DOG.value[1]].add_piece(Dog(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_WOLF.value[0]][Position.LIGHT_WOLF.value[1]].add_piece(Wolf(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_LEOPARD.value[0]][Position.LIGHT_LEOPARD.value[1]].add_piece(Leopard(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_TIGER.value[0]][Position.LIGHT_TIGER.value[1]].add_piece(Tiger(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_LION.value[0]][Position.LIGHT_LION.value[1]].add_piece(Lion(PlayerSide.LIGHT))
        self.cells[Position.LIGHT_ELEPHANT.value[0]][Position.LIGHT_ELEPHANT.value[1]].add_piece(Elephant(PlayerSide.LIGHT))

    def get_cell(self, position):
        return self.cells[position[0]][position[1]]

class Cell:
    def __init__(self, label, position, image_path=None):
        self.label = label
        self.position = position
        self.image = image_path and transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value) or None
        self.piece = None

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
    
    def available_moves(self, board):
        moves = []
        left = self.left(1, board)
        right = self.right(1, board)
        up = self.up(1, board)
        down = self.down(1, board)
        if isinstance(self, Tiger) or isinstance(self, Lion):
            while left.is_river():
                left = left.left(1, board)
            while right.is_river():
                right = right.right(1, board)
            while up.is_river():
                up = up.up(1, board)
            while down.is_river():
                down = down.down(1, board)
        if isinstance(self, Rat) or isinstance(self, Dog):
            if left.is_in_board() and not left.is_occupied_by_own_piece(self.side) and not left.is_defeated_by_own_piece(self):
                moves.append(left)
            if right.is_in_board() and not right.is_occupied_by_own_piece(self.side) and not right.is_defeated_by_own_piece(self):
                moves.append(right)
            if up.is_in_board() and not up.is_occupied_by_own_piece(self.side) and not up.is_defeated_by_own_piece(self):
                moves.append(up)
            if down.is_in_board() and not down.is_occupied_by_own_piece(self.side) and not down.is_defeated_by_own_piece(self):
                moves.append(down)
        else:
            if left.is_in_board() and not left.is_river() and not left.is_occupied_by_own_piece(self.side) and not left.is_defeated_by_own_piece(self):
                moves.append(left)
            if right.is_in_board() and not right.is_river() and not right.is_occupied_by_own_piece(self.side) and not right.is_defeated_by_own_piece(self):
                moves.append(right)
            if up.is_in_board() and not up.is_river() and not up.is_occupied_by_own_piece(self.side) and not up.is_defeated_by_own_piece(self):
                moves.append(up)
            if down.is_in_board() and not down.is_river() and not down.is_occupied_by_own_piece(self.side) and not down.is_defeated_by_own_piece(self):
                moves.append(down)
        return moves
    
    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

# class Piece:
#     def __init__(self, name, detail, position, atk, side, image_path, artwork_path):
#         self.name = name
#         self.image = transform.scale(image.load(image_path), GameConstant.CELL_SIZE.value)
#         self.artwork = transform.scale(image.load(artwork_path), GameConstant.ARTWORK_SIZE.value)
#         self.detail = detail
#         self.position = position
#         self.atk = atk
#         self.side = side
#         self.selected = False

#     def move(self, position):
#         self.position = position

#     def get_direction(self, direction, step, board):
#         deltas = {'left': (-step, 0), 'right': (step, 0), 'up': (0, -step), 'down': (0, step)}
#         delta = deltas.get(direction, (0, 0))
#         return board.get_cell((self.position[0] + delta[0], self.position[1] + delta[1]))

#     def can_jump_over_river(self):
#         return isinstance(self, Tiger) or isinstance(self, Lion)

#     def is_move_valid(self, cell):
#         if not cell.is_in_board():
#             return False
#         if self.can_jump_over_river() and cell.is_river():
#             return True
#         return not cell.is_river() and not cell.is_occupied_by_own_piece(self.side) and not cell.is_defeated_by_own_piece(self)

#     def available_moves(self, board):
#         moves = []
#         directions = ['left', 'right', 'up', 'down']
#         for direction in directions:
#             step = 1
#             next_cell = self.get_direction(direction, step, board)
#             while next_cell.is_in_board() and (next_cell.is_river() if self.can_jump_over_river() else True):
#                 if self.is_move_valid(next_cell):
#                     moves.append(next_cell)
#                 if not next_cell.is_river():
#                     break
#                 step += 1
#                 next_cell = self.get_direction(direction, step, board)
#         return moves

#     def select(self):
#         self.selected = True

#     def unselect(self):
#         self.selected = False


class Rat(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT, Detail.RAT, side == PlayerSide.DARK and Position.DARK_RAT or Position.LIGHT_RAT, Atk.RAT, side, Avatar.DARK_RAT, ArtWork.DARK_RAT)

class Cat(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_CAT or PieceName.LIGHT_CAT, Detail.CAT, side == PlayerSide.DARK and Position.DARK_CAT or Position.LIGHT_CAT, Atk.CAT, side, Avatar.DARK_CAT, ArtWork.DARK_CAT)

class Dog(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG, Detail.DOG, side == PlayerSide.DARK and Position.DARK_DOG or Position.LIGHT_DOG, Atk.DOG, side, Avatar.DARK_DOG, ArtWork.DARK_DOG)

class Wolf(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_WOLF or PieceName.LIGHT_WOLF, Detail.WOLF, side == PlayerSide.DARK and Position.DARK_WOLF or Position.LIGHT_WOLF, Atk.WOLF, side, Avatar.DARK_WOLF, ArtWork.DARK_WOLF)

class Leopard(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_LEOPARD or PieceName.LIGHT_LEOPARD, Detail.LEOPARD, side == PlayerSide.DARK and Position.DARK_LEOPARD or Position.LIGHT_LEOPARD, Atk.LEOPARD, side, Avatar.DARK_LEOPARD, ArtWork.DARK_LEOPARD)

class Tiger(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_TIGER or PieceName.LIGHT_TIGER, Detail.TIGER, side == PlayerSide.DARK and Position.DARK_TIGER or Position.LIGHT_TIGER, Atk.TIGER, side, Avatar.DARK_TIGER, ArtWork.DARK_TIGER)

class Lion(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION, Detail.LION, side == PlayerSide.DARK and Position.DARK_LION or Position.LIGHT_LION, Atk.LION, side, Avatar.DARK_LION, ArtWork.DARK_LION)

class Elephant(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT, Detail.ELEPHANT, side == PlayerSide.DARK and Position.DARK_ELEPHANT or Position.LIGHT_ELEPHANT, Atk.ELEPHANT, side, Avatar.DARK_ELEPHANT, ArtWork.DARK_ELEPHANT)

class Player:
    def __init__(self, side):
        self.side = side
        self.pieces = [Rat(side), Cat(side), Dog(side), Wolf(side), Leopard(side), Tiger(side), Lion(side), Elephant(side)]
        self.den =  side == PlayerSide.DARK and Position.DARK_DEN.value or Position.LIGHT_DEN.value
        self.traps = side == PlayerSide.DARK and [Position.DARK_TRAP_1.value, Position.DARK_TRAP_2.value, Position.DARK_TRAP_3.value] or [Position.LIGHT_TRAP_1.value, Position.LIGHT_TRAP_2.value, Position.LIGHT_TRAP_3.value]

class Log:
    def __init__(self, player, piece, cell):
        self.player = player.side
        self.piece = piece.__class__.__name__
        self.x, self.y = cell.position
