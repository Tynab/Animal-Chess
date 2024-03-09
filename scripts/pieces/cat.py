from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Cat(Piece):

    def __init__(self, side):
        super().__init__(PieceName.cat(side), PieceDetail.CAT, CellPosition.cat(side), PieceAtk.CAT, side, PieceAvatar.cat(side), PieceArtWork.cat(side))

    def copy(self):
        return Cat(self.side)
