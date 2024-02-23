from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Wolf(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_WOLF or PieceName.LIGHT_WOLF, PieceDetail.WOLF, side == PlayerSide.DARK and CellPosition.DARK_WOLF or CellPosition.LIGHT_WOLF, PieceAtk.WOLF, side, PieceAvatar.DARK_WOLF, PieceArtWork.DARK_WOLF)
