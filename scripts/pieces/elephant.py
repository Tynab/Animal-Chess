import scripts.pieces.rat as rat
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Elephant(Piece):
    '''
    The Elephant piece.
    '''
    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT,
            PieceDetail.ELEPHANT,
            side == PlayerSide.DARK and CellPosition.DARK_ELEPHANT or CellPosition.LIGHT_ELEPHANT,
            PieceAtk.ELEPHANT,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_ELEPHANT or PieceAvatar.LIGHT_ELEPHANT,
            side == PlayerSide.DARK and PieceArtWork.DARK_ELEPHANT or PieceArtWork.LIGHT_ELEPHANT
        )

    def is_defeated_by_own_piece(self, cell):
        '''
        Check if the piece is defeated by own piece.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the piece is defeated by own piece, False otherwise.
        '''
        if isinstance(cell.piece, rat.Rat):
            return False
        return self.atk >= cell.piece.atk
