from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Leopard(Piece):
    '''
    Leopard class.
    
    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side):
        '''
        Initialize the leopard.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.leopard(side), PieceDetail.LEOPARD, CellPosition.leopard(side), PieceAtk.LEOPARD, side, PieceAvatar.leopard(side), PieceArtWork.leopard(side))

    def copy(self):
        '''
        Creates a copy of the leopard.
        
        Returns:
            Leopard: The copied leopard.
        '''
        return Leopard(self.side)
