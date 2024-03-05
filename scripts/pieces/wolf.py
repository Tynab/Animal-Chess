from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Wolf(Piece):
    '''
    The Wolf piece.
    '''

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_WOLF or PieceName.LIGHT_WOLF,
            PieceDetail.WOLF,
            side == PlayerSide.DARK and CellPosition.DARK_WOLF or CellPosition.LIGHT_WOLF,
            PieceAtk.WOLF,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_WOLF or PieceAvatar.LIGHT_WOLF,
            side == PlayerSide.DARK and PieceArtWork.DARK_WOLF or PieceArtWork.LIGHT_WOLF
        )

    def clone(self):
        return Wolf(self.side)
