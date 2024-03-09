from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Leopard(Piece):

    def __init__(self, side):
        super().__init__(PieceName.leopard(side), PieceDetail.LEOPARD, CellPosition.leopard(side), PieceAtk.LEOPARD, side, PieceAvatar.leopard(side), PieceArtWork.leopard(side))

    def copy(self):
        return Leopard(self.side)
