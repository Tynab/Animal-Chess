from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Dog(Piece):
    '''
    Dog class.
    
    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side):
        '''
        Initialize the dog.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.dog(side), PieceDetail.DOG, CellPosition.dog(side), PieceAtk.DOG, side, PieceAvatar.dog(side), PieceArtWork.dog(side))

    def copy(self):
        '''
        Creates a copy of the dog.
        
        Returns:
            Dog: The copied dog.
        '''
        return Dog(self.side)

    def is_valid_cell(self, cell):
        '''
        Checks if a cell is a valid move for the piece.
        
        Args:
            cell (Cell): The cell.
        
        Returns:
            bool: True if the cell is a valid move for the piece, False otherwise.
        '''
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))
