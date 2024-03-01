from scripts.common import CellLabel, CellImage, CellPosition, PlayerSide

import scripts.cell as cell
import scripts.common as common
import scripts.pieces.rat as rat
import scripts.pieces.cat as cat
import scripts.pieces.dog as dog
import scripts.pieces.wolf as wolf
import scripts.pieces.leopard as leopard
import scripts.pieces.tiger as tiger
import scripts.pieces.lion as lion
import scripts.pieces.elephant as elephant

class Board:
    def __init__(self):
        self.cells = [[cell.Cell(CellLabel.EMPTY, (x, y)) for y in range(common.H)] for x in range(common.W)]
        self.cells[CellPosition.RIVER_1_1[0]][CellPosition.RIVER_1_1[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_2[0]][CellPosition.RIVER_1_2[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_3[0]][CellPosition.RIVER_1_3[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_4[0]][CellPosition.RIVER_1_4[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_5[0]][CellPosition.RIVER_1_5[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_1_6[0]][CellPosition.RIVER_1_6[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_1[0]][CellPosition.RIVER_2_1[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_2[0]][CellPosition.RIVER_2_2[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_3[0]][CellPosition.RIVER_2_3[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_4[0]][CellPosition.RIVER_2_4[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_5[0]][CellPosition.RIVER_2_5[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.RIVER_2_6[0]][CellPosition.RIVER_2_6[1]].set_label(CellLabel.RIVER)
        self.cells[CellPosition.DARK_TRAP_1[0]][CellPosition.DARK_TRAP_1[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.DARK_TRAP_2[0]][CellPosition.DARK_TRAP_2[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.DARK_TRAP_3[0]][CellPosition.DARK_TRAP_3[1]].set_label(CellLabel.DARK_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_1[0]][CellPosition.LIGHT_TRAP_1[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_2[0]][CellPosition.LIGHT_TRAP_2[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.LIGHT_TRAP_3[0]][CellPosition.LIGHT_TRAP_3[1]].set_label(CellLabel.LIGHT_TRAP)
        self.cells[CellPosition.DARK_DEN[0]][CellPosition.DARK_DEN[1]].set_label(CellLabel.DARK_DEN)
        self.cells[CellPosition.LIGHT_DEN[0]][CellPosition.LIGHT_DEN[1]].set_label(CellLabel.LIGHT_DEN)
        self.cells[CellPosition.RIVER_1_1[0]][CellPosition.RIVER_1_1[1]].set_image(CellImage.RIVER_1)
        self.cells[CellPosition.RIVER_1_2[0]][CellPosition.RIVER_1_2[1]].set_image(CellImage.RIVER_2)
        self.cells[CellPosition.RIVER_1_3[0]][CellPosition.RIVER_1_3[1]].set_image(CellImage.RIVER_3)
        self.cells[CellPosition.RIVER_1_4[0]][CellPosition.RIVER_1_4[1]].set_image(CellImage.RIVER_4)
        self.cells[CellPosition.RIVER_1_5[0]][CellPosition.RIVER_1_5[1]].set_image(CellImage.RIVER_5)
        self.cells[CellPosition.RIVER_1_6[0]][CellPosition.RIVER_1_6[1]].set_image(CellImage.RIVER_6)
        self.cells[CellPosition.RIVER_2_1[0]][CellPosition.RIVER_2_1[1]].set_image(CellImage.RIVER_1)
        self.cells[CellPosition.RIVER_2_2[0]][CellPosition.RIVER_2_2[1]].set_image(CellImage.RIVER_2)
        self.cells[CellPosition.RIVER_2_3[0]][CellPosition.RIVER_2_3[1]].set_image(CellImage.RIVER_3)
        self.cells[CellPosition.RIVER_2_4[0]][CellPosition.RIVER_2_4[1]].set_image(CellImage.RIVER_4)
        self.cells[CellPosition.RIVER_2_5[0]][CellPosition.RIVER_2_5[1]].set_image(CellImage.RIVER_5)
        self.cells[CellPosition.RIVER_2_6[0]][CellPosition.RIVER_2_6[1]].set_image(CellImage.RIVER_6)
        self.cells[CellPosition.DARK_TRAP_1[0]][CellPosition.DARK_TRAP_1[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.DARK_TRAP_2[0]][CellPosition.DARK_TRAP_2[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.DARK_TRAP_3[0]][CellPosition.DARK_TRAP_3[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.LIGHT_TRAP_1[0]][CellPosition.LIGHT_TRAP_1[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.LIGHT_TRAP_2[0]][CellPosition.LIGHT_TRAP_2[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.LIGHT_TRAP_3[0]][CellPosition.LIGHT_TRAP_3[1]].set_image(CellImage.TRAP)
        self.cells[CellPosition.DARK_DEN[0]][CellPosition.DARK_DEN[1]].set_image(CellImage.DEN)
        self.cells[CellPosition.LIGHT_DEN[0]][CellPosition.LIGHT_DEN[1]].set_image(CellImage.DEN)
        self.cells[CellPosition.DARK_RAT[0]][CellPosition.DARK_RAT[1]].add_piece(rat.Rat(PlayerSide.DARK))
        self.cells[CellPosition.DARK_CAT[0]][CellPosition.DARK_CAT[1]].add_piece(cat.Cat(PlayerSide.DARK))
        self.cells[CellPosition.DARK_DOG[0]][CellPosition.DARK_DOG[1]].add_piece(dog.Dog(PlayerSide.DARK))
        self.cells[CellPosition.DARK_WOLF[0]][CellPosition.DARK_WOLF[1]].add_piece(wolf.Wolf(PlayerSide.DARK))
        self.cells[CellPosition.DARK_LEOPARD[0]][CellPosition.DARK_LEOPARD[1]].add_piece(leopard.Leopard(PlayerSide.DARK))
        self.cells[CellPosition.DARK_TIGER[0]][CellPosition.DARK_TIGER[1]].add_piece(tiger.Tiger(PlayerSide.DARK))
        self.cells[CellPosition.DARK_LION[0]][CellPosition.DARK_LION[1]].add_piece(lion.Lion(PlayerSide.DARK))
        self.cells[CellPosition.DARK_ELEPHANT[0]][CellPosition.DARK_ELEPHANT[1]].add_piece(elephant.Elephant(PlayerSide.DARK))
        self.cells[CellPosition.LIGHT_RAT[0]][CellPosition.LIGHT_RAT[1]].add_piece(rat.Rat(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_CAT[0]][CellPosition.LIGHT_CAT[1]].add_piece(cat.Cat(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_DOG[0]][CellPosition.LIGHT_DOG[1]].add_piece(dog.Dog(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_WOLF[0]][CellPosition.LIGHT_WOLF[1]].add_piece(wolf.Wolf(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_LEOPARD[0]][CellPosition.LIGHT_LEOPARD[1]].add_piece(leopard.Leopard(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_TIGER[0]][CellPosition.LIGHT_TIGER[1]].add_piece(tiger.Tiger(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_LION[0]][CellPosition.LIGHT_LION[1]].add_piece(lion.Lion(PlayerSide.LIGHT))
        self.cells[CellPosition.LIGHT_ELEPHANT[0]][CellPosition.LIGHT_ELEPHANT[1]].add_piece(elephant.Elephant(PlayerSide.LIGHT))

    def get_cell(self, position):
        return self.cells[position[0]][position[1]]
