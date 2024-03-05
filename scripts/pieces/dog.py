from scripts.piece import Piece
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork

class Dog(Piece):
    '''
    The Dog piece.
    '''

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG,
            PieceDetail.DOG,
            side == PlayerSide.DARK and CellPosition.DARK_DOG or CellPosition.LIGHT_DOG,
            PieceAtk.DOG,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_DOG or PieceAvatar.LIGHT_DOG,
            side == PlayerSide.DARK and PieceArtWork.DARK_DOG or PieceArtWork.LIGHT_DOG
        )

    def clone(self):
        return Dog(self.side)

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
