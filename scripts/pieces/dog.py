from scripts.piece import Piece
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork

class Dog(Piece):

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG,
            PieceDetail.DOG,
            side == PlayerSide.DARK and CellPosition.DARK_DOG or CellPosition.LIGHT_DOG,
            PieceAtk.DOG,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_DOG or PieceAvatar.LIGHT_DOG,
            side == PlayerSide.DARK and PieceArtWork.DARK_DOG or PieceArtWork.LIGHT_DOG
        )

    def clone(self):
        return Dog(self.side)

    def is_cell_valid(self, cell):
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))
