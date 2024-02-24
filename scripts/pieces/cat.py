from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Cat(Piece):
    '''
    The Cat piece.
    '''
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_CAT or PieceName.LIGHT_CAT, PieceDetail.CAT, side == PlayerSide.DARK and CellPosition.DARK_CAT or CellPosition.LIGHT_CAT, PieceAtk.CAT, side, PieceAvatar.DARK_CAT, PieceArtWork.DARK_CAT)
