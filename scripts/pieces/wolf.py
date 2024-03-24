from scripts.common import *
from scripts.piece import *

class Wolf(Piece):
    '''
    Wolf class.
    
    Attributes:
    - side (PlayerSide): The player side.
    
    Methods:
    - __init__: Initialize the wolf.
    - copy: Creates a copy of the wolf.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the wolf.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.
            
        Returns:
            Wolf: A new Wolf instance.
        '''
        super().__init__(PieceName.wolf(side), PieceDetail.WOLF, CellPosition.wolf(side), PieceAtk.WOLF, side, None if is_copy else PieceAvatar.wolf(side), None if is_copy else PieceArtWork.wolf(side))

    def copy(self):
        '''
        Creates a copy of the wolf.
        
        Returns:
            Wolf: A new Wolf instance.
        '''
        return Wolf(self.side, True)
