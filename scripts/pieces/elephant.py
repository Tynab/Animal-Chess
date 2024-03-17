import scripts.pieces.rat as rat
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Elephant(Piece):
    '''
    Elephant class.
    
    Attributes:
    - side (PlayerSide): The player side.
    - name (PieceName): The piece name.
    - detail (PieceDetail): The piece detail.
    - position (CellPosition): The initial position.
    - atk (PieceAtk): The piece attack value.
    - avatar (PieceAvatar): The piece avatar.
    - artwork (PieceArtWork): The piece artwork.

    Methods:
    - __init__: Initialize the elephant.
    - copy: Creates a copy of the elephant.
    - can_defeat: Checks if the elephant can defeat the piece.
    - weaker_pieces_positions: Returns a list of positions of weaker pieces.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the elephant.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.

        Returns:
            Elephant: A new Elephant instance.
        '''
        super().__init__(PieceName.elephant(side), PieceDetail.ELEPHANT, CellPosition.elephant(side), PieceAtk.ELEPHANT, side, None if is_copy else PieceAvatar.elephant(side), None if is_copy else PieceArtWork.elephant(side))

    def copy(self):
        '''
        Creates a copy of the elephant.
        
        Returns:
            Elephant: The copied elephant.
        '''
        return Elephant(self.side, True)

    def can_defeat(self, piece):
        '''
        Checks if the elephant can defeat the piece.
        
        Args:
            piece (Piece): The piece.
            
        Returns:
            bool: True if the elephant can defeat the piece, False otherwise.
        '''
        return not isinstance(piece, rat.Rat) and self.atk >= piece.atk

    def weaker_pieces_positions(self, board):
        '''
        Returns a list of positions of weaker pieces.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: The list of positions of weaker pieces.
        '''
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk and not isinstance(piece, rat.Rat)]
