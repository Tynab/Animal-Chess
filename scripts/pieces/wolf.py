from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Wolf(Piece):
    '''
    Wolf class.
    
    Attributes:
    - side (PlayerSide): The player side.
    - name (PieceName): The piece name.
    - detail (PieceDetail): The piece detail.
    - position (CellPosition): The initial position.
    - atk (PieceAtk): The piece attack value.
    - avatar (PieceAvatar): The piece avatar.
    - artwork (PieceArtWork): The piece artwork.

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
            Wolf: The copied wolf.
        '''
        return Wolf(self.side, True)
