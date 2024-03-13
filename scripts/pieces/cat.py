from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Cat(Piece):
    '''
    Cat piece class.

    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side):
        '''
        Initialize the cat.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.cat(side), PieceDetail.CAT, CellPosition.cat(side), PieceAtk.CAT, side, PieceAvatar.cat(side), PieceArtWork.cat(side))

    def copy(self):
        '''
        Return a copy of the piece.
        
        Returns:
            Cat: A new Cat instance.
        '''
        return Cat(self.side)
