from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Lion(Piece):
    '''
    Lion class.
    
    Attributes:
    - side (PlayerSide): The player side.
    - name (PieceName): The piece name.
    - detail (PieceDetail): The piece detail.
    - position (CellPosition): The initial position.
    - atk (PieceAtk): The piece attack value.
    - avatar (PieceAvatar): The piece avatar.
    - artwork (PieceArtWork): The piece artwork.

    Methods:
    - __init__: Initialize the lion.
    - copy: Creates a copy of the lion.
    - available_cells: Returns a list of available cells for the lion.
    - jump_over_river: Jumps over the river.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the lion.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.

        Returns:
            Lion: A new Lion instance.
        '''
        super().__init__(PieceName.lion(side), PieceDetail.LION, CellPosition.lion(side), PieceAtk.LION, side, None if is_copy else PieceAvatar.lion(side), None if is_copy else PieceArtWork.lion(side))

    def copy(self):
        '''
        Creates a copy of the lion.
        
        Returns:
            Lion: The copied lion.
        '''
        return Lion(self.side, True)

    def available_cells(self, board):
        '''
        Returns a list of available cells for the lion.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: The list of available cells.
        '''
        # Get the available cells in all directions
        result = [cell for direction in [self.left, self.right, self.up, self.down] if (cell := Lion.jump_over_river(direction(1, board), direction, board) or direction(1, board)) and self.is_valid_cell(cell)]

        # If the piece is a lion, add the den position to the available cells
        if board.forbidden_move and board.forbidden_move[0] == self.position and board.forbidden_cell in result:
            result.remove(board.forbidden_cell)

        # Return the result
        return result

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

        # While the cell is a river, keep moving
        while cell.is_river:
            # Get the next cell
            cell = direction(step, board)

            # If the cell is invalid, return None
            if cell and cell.piece:
                return cell.is_river and None or cell
            
            # Increment the step
            step += 1

        # Return the cell
        return cell
