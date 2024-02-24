from scripts.cell import Cell, CellLabel, CellImage, CellPosition
from scripts.game import GameConstant
from scripts.pieces.rat import Rat
from scripts.pieces.cat import Cat
from scripts.pieces.dog import Dog
from scripts.pieces.wolf import Wolf
from scripts.pieces.leopard import Leopard
from scripts.pieces.tiger import Tiger
from scripts.pieces.lion import Lion
from scripts.pieces.elephant import Elephant
from scripts.player import PlayerSide

class Board:
    '''
    The board.
    '''
    def __init__(self):
        # Create cells
        self.cells = [[Cell(CellLabel.EMPTY, (x, y)) for y in range(GameConstant.HEIGHT.value)] for x in range(GameConstant.WIDTH.value)]
        # Set labels
        self.cells[CellPosition.RIVER_1_1.value[0]][CellPosition.RIVER_1_1.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_2.value[0]][CellPosition.RIVER_1_2.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_3.value[0]][CellPosition.RIVER_1_3.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_4.value[0]][CellPosition.RIVER_1_4.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_5.value[0]][CellPosition.RIVER_1_5.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_6.value[0]][CellPosition.RIVER_1_6.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_1.value[0]][CellPosition.RIVER_2_1.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_2.value[0]][CellPosition.RIVER_2_2.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_3.value[0]][CellPosition.RIVER_2_3.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_4.value[0]][CellPosition.RIVER_2_4.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_5.value[0]][CellPosition.RIVER_2_5.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_6.value[0]][CellPosition.RIVER_2_6.value[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.DARK_TRAP_1.value[0]][CellPosition.DARK_TRAP_1.value[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.DARK_TRAP_2.value[0]][CellPosition.DARK_TRAP_2.value[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.DARK_TRAP_3.value[0]][CellPosition.DARK_TRAP_3.value[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_1.value[0]][CellPosition.LIGHT_TRAP_1.value[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_2.value[0]][CellPosition.LIGHT_TRAP_2.value[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_3.value[0]][CellPosition.LIGHT_TRAP_3.value[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.DARK_DEN.value[0]][CellPosition.DARK_DEN.value[1]].set_label(CellLabel.DARK_DEN)
        self.cells[CellPosition.LIGHT_DEN.value[0]][CellPosition.LIGHT_DEN.value[1]].set_label(CellLabel.LIGHT_DEN)
        # Set images
        self.cells[CellPosition.RIVER_1_1.value[0]][CellPosition.RIVER_1_1.value[1]].set_image(CellImage.RIVER_1.value)
        self.cells[CellPosition.RIVER_1_2.value[0]][CellPosition.RIVER_1_2.value[1]].set_image(CellImage.RIVER_2.value)
        self.cells[CellPosition.RIVER_1_3.value[0]][CellPosition.RIVER_1_3.value[1]].set_image(CellImage.RIVER_3.value)
        self.cells[CellPosition.RIVER_1_4.value[0]][CellPosition.RIVER_1_4.value[1]].set_image(CellImage.RIVER_4.value)
        self.cells[CellPosition.RIVER_1_5.value[0]][CellPosition.RIVER_1_5.value[1]].set_image(CellImage.RIVER_5.value)
        self.cells[CellPosition.RIVER_1_6.value[0]][CellPosition.RIVER_1_6.value[1]].set_image(CellImage.RIVER_6.value)
        self.cells[CellPosition.RIVER_2_1.value[0]][CellPosition.RIVER_2_1.value[1]].set_image(CellImage.RIVER_1.value)
        self.cells[CellPosition.RIVER_2_2.value[0]][CellPosition.RIVER_2_2.value[1]].set_image(CellImage.RIVER_2.value)
        self.cells[CellPosition.RIVER_2_3.value[0]][CellPosition.RIVER_2_3.value[1]].set_image(CellImage.RIVER_3.value)
        self.cells[CellPosition.RIVER_2_4.value[0]][CellPosition.RIVER_2_4.value[1]].set_image(CellImage.RIVER_4.value)
        self.cells[CellPosition.RIVER_2_5.value[0]][CellPosition.RIVER_2_5.value[1]].set_image(CellImage.RIVER_5.value)
        self.cells[CellPosition.RIVER_2_6.value[0]][CellPosition.RIVER_2_6.value[1]].set_image(CellImage.RIVER_6.value)
        self.cells[CellPosition.DARK_TRAP_1.value[0]][CellPosition.DARK_TRAP_1.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.DARK_TRAP_2.value[0]][CellPosition.DARK_TRAP_2.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.DARK_TRAP_3.value[0]][CellPosition.DARK_TRAP_3.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.LIGHT_TRAP_1.value[0]][CellPosition.LIGHT_TRAP_1.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.LIGHT_TRAP_2.value[0]][CellPosition.LIGHT_TRAP_2.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.LIGHT_TRAP_3.value[0]][CellPosition.LIGHT_TRAP_3.value[1]].set_image(CellImage.TRAP.value)
        self.cells[CellPosition.DARK_DEN.value[0]][CellPosition.DARK_DEN.value[1]].set_image(CellImage.DEN.value)
        self.cells[CellPosition.LIGHT_DEN.value[0]][CellPosition.LIGHT_DEN.value[1]].set_image(CellImage.DEN.value)
        # Set pieces
        self.cells[CellPosition.DARK_RAT.value[0]][CellPosition.DARK_RAT.value[1]].add_piece(Rat(PlayerSide.DARK))
        self.cells[CellPosition.DARK_CAT.value[0]][CellPosition.DARK_CAT.value[1]].add_piece(Cat(PlayerSide.DARK))
        self.cells[CellPosition.DARK_DOG.value[0]][CellPosition.DARK_DOG.value[1]].add_piece(Dog(PlayerSide.DARK))
        self.cells[CellPosition.DARK_WOLF.value[0]][CellPosition.DARK_WOLF.value[1]].add_piece(Wolf(PlayerSide.DARK))
        self.cells[CellPosition.DARK_LEOPARD.value[0]][CellPosition.DARK_LEOPARD.value[1]].add_piece(Leopard(PlayerSide.DARK))
        self.cells[CellPosition.DARK_TIGER.value[0]][CellPosition.DARK_TIGER.value[1]].add_piece(Tiger(PlayerSide.DARK))
        self.cells[CellPosition.DARK_LION.value[0]][CellPosition.DARK_LION.value[1]].add_piece(Lion(PlayerSide.DARK))
        self.cells[CellPosition.DARK_ELEPHANT.value[0]][CellPosition.DARK_ELEPHANT.value[1]].add_piece(Elephant(PlayerSide.DARK))
        self.cells[CellPosition.LIGHT_RAT.value[0]][CellPosition.LIGHT_RAT.value[1]].add_piece(Rat(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_CAT.value[0]][CellPosition.LIGHT_CAT.value[1]].add_piece(Cat(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_DOG.value[0]][CellPosition.LIGHT_DOG.value[1]].add_piece(Dog(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_WOLF.value[0]][CellPosition.LIGHT_WOLF.value[1]].add_piece(Wolf(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_LEOPARD.value[0]][CellPosition.LIGHT_LEOPARD.value[1]].add_piece(Leopard(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_TIGER.value[0]][CellPosition.LIGHT_TIGER.value[1]].add_piece(Tiger(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_LION.value[0]][CellPosition.LIGHT_LION.value[1]].add_piece(Lion(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_ELEPHANT.value[0]][CellPosition.LIGHT_ELEPHANT.value[1]].add_piece(Elephant(PlayerSide.LIGHT))

    def get_cell(self, position):
        '''
        Get the cell at the given position.
        
        Args:
            position (tuple): The position of the cell.
        
        Returns:
            Cell: The cell at the given position.
        '''
        return self.cells[position[0]][position[1]]
