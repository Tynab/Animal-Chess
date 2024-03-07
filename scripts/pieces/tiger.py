from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Tiger(Piece):

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_TIGER or PieceName.LIGHT_TIGER,
            PieceDetail.TIGER,
            side == PlayerSide.DARK and CellPosition.DARK_TIGER or CellPosition.LIGHT_TIGER,
            PieceAtk.TIGER,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_TIGER or PieceAvatar.LIGHT_TIGER,
            side == PlayerSide.DARK and PieceArtWork.DARK_TIGER or PieceArtWork.LIGHT_TIGER
        )

    def clone(self):
        return Tiger(self.side)

    def available_cells(self, board):
        return [cell for direction in [self.left, self.right, self.up, self.down] if (cell := Tiger.jump_over_river(direction(1, board), direction, board) or direction(1, board)) and self.is_cell_valid(cell)]

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
