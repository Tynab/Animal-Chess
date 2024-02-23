from enum import Enum
from scripts.cell import CellPosition
from scripts.pieces.rat import Rat
from scripts.pieces.cat import Cat
from scripts.pieces.dog import Dog
from scripts.pieces.wolf import Wolf
from scripts.pieces.leopard import Leopard
from scripts.pieces.tiger import Tiger
from scripts.pieces.lion import Lion
from scripts.pieces.elephant import Elephant

class PlayerSide(Enum):
    DARK = 'Dark'
    LIGHT = 'Light'

class Player:
    def __init__(self, side):
        self.side = side
        self.pieces = [Rat(side), Cat(side), Dog(side), Wolf(side), Leopard(side), Tiger(side), Lion(side), Elephant(side)]
        self.den =  side == PlayerSide.DARK and CellPosition.DARK_DEN.value or CellPosition.LIGHT_DEN.value
        self.traps = side == PlayerSide.DARK and [CellPosition.DARK_TRAP_1.value, CellPosition.DARK_TRAP_2.value, CellPosition.DARK_TRAP_3.value] or [CellPosition.LIGHT_TRAP_1.value, CellPosition.LIGHT_TRAP_2.value, CellPosition.LIGHT_TRAP_3.value]
