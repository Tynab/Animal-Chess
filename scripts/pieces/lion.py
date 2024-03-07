from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Lion(Piece):

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION,
            PieceDetail.LION,
            side == PlayerSide.DARK and CellPosition.DARK_LION or CellPosition.LIGHT_LION,
            PieceAtk.LION,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_LION or PieceAvatar.LIGHT_LION,
            side == PlayerSide.DARK and PieceArtWork.DARK_LION or PieceArtWork.LIGHT_LION
        )

    def clone(self):
        return Lion(self.side)

    def available_cells(self, board):
        return [cell for direction in [self.left, self.right, self.up, self.down] if (cell := Lion.jump_over_river(direction(1, board), direction, board) or direction(1, board)) and self.is_cell_valid(cell)]

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
