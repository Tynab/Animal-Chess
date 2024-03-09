from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Wolf(Piece):

    def __init__(self, side):
        super().__init__(PieceName.wolf(side), PieceDetail.WOLF, CellPosition.wolf(side), PieceAtk.WOLF, side, PieceAvatar.wolf(side), PieceArtWork.wolf(side))

    def copy(self):
        return Wolf(self.side)
