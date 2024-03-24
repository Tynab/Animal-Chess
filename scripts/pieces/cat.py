from scripts.common import *
from scripts.piece import *

class Cat(Piece):
    '''
    Cat class.

    Attributes:
    - side (PlayerSide): The player side.

    Methods:
    - __init__: Initialize the cat.
    - copy: Return a copy of the piece.
    '''
    
    def __init__(self, side, is_copy=False):
        '''
        Initialize the cat.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.
        
        Returns:
            Cat: A new Cat instance.
        '''
        super().__init__(PieceName.cat(side), PieceDetail.CAT, CellPosition.cat(side), PieceAtk.CAT, side, None if is_copy else PieceAvatar.cat(side), None if is_copy else PieceArtWork.cat(side))

    def copy(self):
        '''
        Return a copy of the piece.
        
        Returns:
            Cat: A new Cat instance.
        '''
        return Cat(self.side, True)
