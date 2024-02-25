import scripts.pieces.rat as rat
import scripts.pieces.cat as cat
import scripts.pieces.dog as dog
import scripts.pieces.wolf as wolf
import scripts.pieces.leopard as leopard
import scripts.pieces.tiger as tiger
import scripts.pieces.lion as lion
import scripts.pieces.elephant as elephant
from scripts.common import PlayerSide, CellPosition

class Player:
    '''
    The player.
    '''
    def __init__(self, side):
        self.side = side
        self.pieces = [rat.Rat(side), cat.Cat(side), dog.Dog(side), wolf.Wolf(side), leopard.Leopard(side), tiger.Tiger(side), lion.Lion(side), elephant.Elephant(side)]
        self.den =  side == PlayerSide.DARK and CellPosition.DARK_DEN or CellPosition.LIGHT_DEN
        self.traps = side == PlayerSide.DARK and [CellPosition.DARK_TRAP_1, CellPosition.DARK_TRAP_2, CellPosition.DARK_TRAP_3] or [CellPosition.LIGHT_TRAP_1, CellPosition.LIGHT_TRAP_2, CellPosition.LIGHT_TRAP_3]
