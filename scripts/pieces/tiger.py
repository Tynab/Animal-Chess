from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Tiger(Piece):
    '''
    Tiger class.
    
    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side):
        '''
        Initialize the tiger.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.tiger(side), PieceDetail.TIGER, CellPosition.tiger(side), PieceAtk.TIGER, side, PieceAvatar.tiger(side), PieceArtWork.tiger(side))

    def copy(self):
        '''
        Creates a copy of the tiger.
        
        Returns:
            Tiger: The copied tiger.
        '''
        return Tiger(self.side)

    def available_cells(self, board):
        '''
        Returns a list of available cells for the tiger.
        
        Args:
            board (Board): The board.
            
        Returns:
            list: The list of available cells.
        '''
        return [cell for direction in [self.left, self.right, self.up, self.down] if (cell := Tiger.jump_over_river(direction(1, board), direction, board) or direction(1, board)) and self.is_valid_cell(cell)]

    @staticmethod
    def jump_over_river(cell, direction, board):
        '''
        Jumps over the river.
        
        Args:
            cell (Cell): The cell.
            direction (function): The direction.
            board (Board): The board.
        
        Returns:
            Cell: The cell.
        '''
        # If the cell is invalid, return None
        if not cell:
            return cell
        
        # Set the step to 1
        step = 1

        # While the cell is a river, get the next cell
        while cell.is_river:
            # Get the next cell
            cell = direction(step, board)
            
            # If the cell is valid and contains a piece, return None
            if cell and cell.piece:
                return None and cell.is_river or cell
            
            # Increment the step
            step += 1
        
        # Return the cell
        return cell
