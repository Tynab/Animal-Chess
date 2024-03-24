from scripts.common import *
from scripts.piece import *

class Dog(Piece):
    '''
    Dog class.
    
    Attributes:
    - side (PlayerSide): The player side.
    
    Methods:
    - __init__: Initializes the dog.
    - copy: Creates a copy of the dog.
    - is_valid_cell: Checks if a cell is a valid move for the piece.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initializes the dog.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.
        
        Returns:
            Dog: A new Dog instance.
        '''
        super().__init__(PieceName.dog(side), PieceDetail.DOG, CellPosition.dog(side), PieceAtk.DOG, side, None if is_copy else PieceAvatar.dog(side), None if is_copy else PieceArtWork.dog(side))

    def copy(self):
        '''
        Creates a copy of the dog.
        
        Returns:
            Dog: A new Dog instance.
        '''
        return Dog(self.side, True)

    def is_valid_cell(self, cell):
        '''
        Checks if a cell is a valid move for the piece.
        
        Args:
            cell (Cell): The cell to check.
        
        Returns:
            bool: True if the cell is a valid move, False otherwise.
        '''
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))
