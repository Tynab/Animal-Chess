import scripts.pieces.elephant as elephant
from scripts.common import CellPosition, PieceAtk, PieceAvatar, PieceArtWork, PieceDetail, PieceName, PlayerSide
from scripts.piece import Piece

class Rat(Piece):
    '''
    The Rat piece.
    '''
    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT,
            PieceDetail.RAT,
            side == PlayerSide.DARK and CellPosition.DARK_RAT or CellPosition.LIGHT_RAT,
            PieceAtk.RAT,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_RAT or PieceAvatar.LIGHT_RAT,
            side == PlayerSide.DARK and PieceArtWork.DARK_RAT or PieceArtWork.LIGHT_RAT
        )

    def is_defeated_by_own_piece(self, cell):
        '''
        Check if the piece is defeated by own piece.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the piece is defeated by own piece, False otherwise.
        '''
        if isinstance(cell.piece, elephant.Elephant):
            return True
        return self.atk >= cell.piece.atk
    
    def is_move_valid(self, cell):
        '''
        Check if the move is valid.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        '''
        if not cell.is_in_board():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if cell.piece and not self.is_defeated_by_own_piece(cell):
            return False
        return True
