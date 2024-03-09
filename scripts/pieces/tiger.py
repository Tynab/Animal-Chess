from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Tiger(Piece):

    def __init__(self, side):
        super().__init__(PieceName.tiger(side), PieceDetail.TIGER, CellPosition.tiger(side), PieceAtk.TIGER, side, PieceAvatar.tiger(side), PieceArtWork.tiger(side))

    def copy(self):
        return Tiger(self.side)

    def available_cells(self, board):
        return [cell for direction in [self.left, self.right, self.up, self.down] if (cell := Tiger.jump_over_river(direction(1, board), direction, board) or direction(1, board)) and self.is_valid_cell(cell)]

    @staticmethod
    def jump_over_river(cell, direction, board):
        if not cell:
            return cell
        step = 1
        while cell.is_river:
            cell = direction(step, board)
            if cell and cell.piece:
                return None and cell.is_river or cell
            step += 1
        return cell
