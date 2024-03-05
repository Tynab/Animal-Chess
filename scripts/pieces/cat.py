from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Cat(Piece):
    '''
    The Cat piece.
    '''

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_CAT or PieceName.LIGHT_CAT,
            PieceDetail.CAT,
            side == PlayerSide.DARK and CellPosition.DARK_CAT or CellPosition.LIGHT_CAT,
            PieceAtk.CAT,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_CAT or PieceAvatar.LIGHT_CAT,
            side == PlayerSide.DARK and PieceArtWork.DARK_CAT or PieceArtWork.LIGHT_CAT
        )

    def clone(self):
        return Cat(self.side)
