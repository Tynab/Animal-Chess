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
from scripts.common import CellLabel, CellImage, CellPosition, PlayerSide

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
        self.pieces = [cell.piece for row in self.cells for cell in row if cell.piece]
        self.captured_pieces = []

    def clone(self):
        cloned_board = Board()
        for i in range(common.W):
            for j in range(common.H):
                cloned_board.cells[i][j].piece =  self.cells[i][j].piece and self.cells[i][j].piece.clone() or None
        cloned_board.update_pieces()
        return cloned_board
    
    def get_cell(self, position):
        return self.cells[position[0]][position[1]]

    def get_valid_moves(self, side):
        valid_moves = []
        for row in self.cells:
            for cell in row:
                if cell.piece and cell.piece.side == side:
                    valid_moves.extend([(cell.position, move.position) for move in cell.piece.available_moves(self)])
        return valid_moves

    def make_move(self, move):
        source_cell = self.get_cell(move[0])
        target_cell = self.get_cell(move[1])
        if target_cell.piece:
            self.captured_pieces.append((target_cell.piece, move[1]))
            target_cell.remove_piece()
        target_cell.add_piece(source_cell.piece)
        source_cell.remove_piece()
        self.update_pieces()

    def undo_move(self, move):
        source_cell = self.get_cell(move[0])
        target_cell = self.get_cell(move[1])
        source_cell.add_piece(target_cell.piece)
        target_cell.remove_piece()
        if self.captured_pieces and self.captured_pieces[-1][1] == move[1]:
            captured_piece, _ = self.captured_pieces.pop()
            target_cell.add_piece(captured_piece)
        self.update_pieces()

    def update_pieces(self):
        self.pieces = [cell.piece for row in self.cells for cell in row if cell.piece]

    def is_game_over(self):
        dark_den_piece = self.get_cell(CellPosition.DARK_DEN).piece
        light_den_piece = self.get_cell(CellPosition.LIGHT_DEN).piece
        if dark_den_piece and dark_den_piece.side == PlayerSide.LIGHT or light_den_piece and light_den_piece.side == PlayerSide.DARK:
            return True
        if not [cell.piece for row in self.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.DARK] or not [cell.piece for row in self.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.LIGHT]:
            return True
        else:
            return False
