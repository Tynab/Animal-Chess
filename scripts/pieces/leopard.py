from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Leopard(Piece):
    '''
    Leopard class.
    
    Attributes:
    - side (PlayerSide): The player side.
    - name (PieceName): The piece name.
    - detail (PieceDetail): The piece detail.
    - position (CellPosition): The initial position.
    - atk (PieceAtk): The piece attack value.
    - avatar (PieceAvatar): The piece avatar.
    - artwork (PieceArtWork): The piece artwork.

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
            Leopard: The copied leopard.
        '''
        return Leopard(self.side, True)
