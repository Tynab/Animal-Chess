from cell import CellPosition
from piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from player import PlayerSide

class Leopard(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_LEOPARD or PieceName.LIGHT_LEOPARD, PieceDetail.LEOPARD, side == PlayerSide.DARK and CellPosition.DARK_LEOPARD or CellPosition.LIGHT_LEOPARD, PieceAtk.LEOPARD, side, PieceAvatar.DARK_LEOPARD, PieceArtWork.DARK_LEOPARD)
