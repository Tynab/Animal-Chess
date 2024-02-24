from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.pieces.rat import Rat
from scripts.player import PlayerSide

class Elephant(Piece):
    '''
    The Elephant piece.
    '''
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT, PieceDetail.ELEPHANT, side == PlayerSide.DARK and CellPosition.DARK_ELEPHANT or CellPosition.LIGHT_ELEPHANT, PieceAtk.ELEPHANT, side, PieceAvatar.DARK_ELEPHANT, PieceArtWork.DARK_ELEPHANT)

    def is_defeated_by_own_piece(self, cell):
        '''
        Check if the piece is defeated by own piece.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the piece is defeated by own piece, False otherwise.
        '''
        if isinstance(cell.piece, Rat):
            return False
        return self.atk >= cell.piece.atk
