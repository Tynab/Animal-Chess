from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Cat(Piece):
    '''
    Cat piece class.

    Attributes:
    - side (PlayerSide): The player side.
    - name (PieceName): The piece name.
    - detail (PieceDetail): The piece detail.
    - position (CellPosition): The initial position.
    - atk (PieceAtk): The piece attack value.
    - avatar (PieceAvatar): The piece avatar.
    - artwork (PieceArtWork): The piece artwork.

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
