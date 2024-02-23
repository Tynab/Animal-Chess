from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Elephant(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT, PieceDetail.ELEPHANT, side == PlayerSide.DARK and CellPosition.DARK_ELEPHANT or CellPosition.LIGHT_ELEPHANT, PieceAtk.ELEPHANT, side, PieceAvatar.DARK_ELEPHANT, PieceArtWork.DARK_ELEPHANT)
