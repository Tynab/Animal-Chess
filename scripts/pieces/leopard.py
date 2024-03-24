from scripts.common import *
from scripts.piece import *

class Leopard(Piece):
    '''
    Leopard class.
    
    Attributes:
    - side (PlayerSide): The player side.
    
    Methods:
    - __init__: Initialize the leopard.
    - copy: Creates a copy of the leopard.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the leopard.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.
        
        Returns:
            Leopard: A new Leopard instance.
        '''
        super().__init__(PieceName.leopard(side), PieceDetail.LEOPARD, CellPosition.leopard(side), PieceAtk.LEOPARD, side, None if is_copy else PieceAvatar.leopard(side), None if is_copy else PieceArtWork.leopard(side))

    def copy(self):
        '''
        Creates a copy of the leopard.
        
        Returns:
            Leopard: A new Leopard instance.
        '''
        return Leopard(self.side, True)
