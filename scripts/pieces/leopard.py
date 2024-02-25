from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Leopard(Piece):
    '''
    The Leopard piece.
    '''
    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_LEOPARD or PieceName.LIGHT_LEOPARD,
            PieceDetail.LEOPARD,
            side == PlayerSide.DARK and CellPosition.DARK_LEOPARD or CellPosition.LIGHT_LEOPARD,
            PieceAtk.LEOPARD,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_LEOPARD or PieceAvatar.LIGHT_LEOPARD,
            side == PlayerSide.DARK and PieceArtWork.DARK_LEOPARD or PieceArtWork.LIGHT_LEOPARD
        )
