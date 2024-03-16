from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Wolf(Piece):
    '''
    Wolf class.
    
    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the wolf.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.wolf(side), PieceDetail.WOLF, CellPosition.wolf(side), PieceAtk.WOLF, side, None if is_copy else PieceAvatar.wolf(side), None if is_copy else PieceArtWork.wolf(side))

    def copy(self):
        '''
        Creates a copy of the wolf.
        
        Returns:
            Wolf: The copied wolf.
        '''
        return Wolf(self.side, True)
