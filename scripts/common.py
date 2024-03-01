W = 7
H = 9
FPS = 60
TIT = 'Animal Chess'
SPAN = 100

class Size:
    BOARD = (W * SPAN, H * SPAN)
    CELL = (SPAN, SPAN)
    ARTWORK = (500, 500)
    START_BTN = (190, 50)

class ImagePath:
    COVER = 'assets/images/cover.png'
    START_BTN = 'assets/images/button.png'

class FontName:
    TIT = 'Garamond'
    BTN = 'Lato'
    TXT = 'Arial'

class Color:
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

class GameState:
    NEW = 1
    RUNNING = 2
    OVER = 3

class PlayerSide:
    DARK = 'Dark'
    LIGHT = 'Light'

class CellLabel:
    EMPTY = 1
    RIVER = 2
    DARK_TRAP = 3
    LIGHT_TRAP = 4
    DARK_DEN = 5
    LIGHT_DEN = 6

class CellPosition:
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

class CellImage:
    DEN = 'assets/images/den.png'
    TRAP = 'assets/images/trap.png'
    RIVER_1 = 'assets/images/rivers/river_1.png'
    RIVER_2 = 'assets/images/rivers/river_2.png'
    RIVER_3 = 'assets/images/rivers/river_3.png'
    RIVER_4 = 'assets/images/rivers/river_4.png'
    RIVER_5 = 'assets/images/rivers/river_5.png'
    RIVER_6 = 'assets/images/rivers/river_6.png'

class PieceLabel:
    DARK_RAT = 1
    DARK_CAT = 2
    DARK_DOG = 3
    DARK_WOLF = 4
    DARK_LEOPARD = 5
    DARK_TIGER = 6
    DARK_LION = 7
    DARK_ELEPHANT = 8
    LIGHT_RAT = 11
    LIGHT_CAT = 12
    LIGHT_DOG = 13
    LIGHT_WOLF = 14
    LIGHT_LEOPARD = 15
    LIGHT_TIGER = 16
    LIGHT_LION = 17
    LIGHT_ELEPHANT = 18

class PieceName:
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

class PieceDetail:
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

class PieceAtk:
    RAT = 1
    CAT = 2
    DOG = 3
    WOLF = 4
    LEOPARD = 5
    TIGER = 6
    LION = 7
    ELEPHANT = 8

class PieceAvatar:
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

class PieceArtWork:
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
