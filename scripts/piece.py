import scripts.common as common
from pygame import transform, image
from scripts.common import Size, PlayerSide, CellPosition

class Piece:
    '''
    The piece.
    '''
    
    def __init__(self, name, detail, position, atk, side, image_path=None, artwork_path=None):
        self.name = name
        self.image = image_path and transform.scale(image.load(image_path), Size.CELL) or None
        self.artwork = artwork_path and transform.scale(image.load(artwork_path), Size.ARTWORK) or None
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side

    def clone(self):
        return Piece(self.name, self.detail, self.position, self.atk, self.side)

    def left(self, step, board):
        '''
        Get the cell to the left of the piece.
        
        Args:
            step (int): The step to move.
            board (Board): The board.
        
        Returns:
            Cell: The cell to the left of the piece.
        '''
        if self.position[0] - step < 0:
            return None
        return board.get_cell((self.position[0] - step, self.position[1]))
    
    def right(self, step, board):
        '''
        Get the cell to the right of the piece.
        
        Args:
            step (int): The step to move.
            board (Board): The board.
        
        Returns:
            Cell: The cell to the right of the piece.
        '''
        if self.position[0] + step >= common.W:
            return None
        return board.get_cell((self.position[0] + step, self.position[1]))
    
    def up(self, step, board):
        '''
        Get the cell to the top of the piece.
        
        Args:
            step (int): The step to move.
            board (Board): The board.
        
        Returns:
            Cell: The cell to the top of the piece.
        '''
        if self.position[1] - step < 0:
            return None
        return board.get_cell((self.position[0], self.position[1] - step))
    
    def down(self, step, board):
        '''
        Get the cell to the bottom of the piece.
        
        Args:
            step (int): The step to move.
            board (Board): The board.
            
        Returns:
            Cell: The cell to the bottom of the piece.
        '''
        if self.position[1] + step >= common.H:
            return None
        return board.get_cell((self.position[0], self.position[1] + step))
    
    def is_defeated_by_own_piece(self, cell):
        '''
        Check if the piece is defeated by own piece.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the piece is defeated by own piece, False otherwise.
        '''
        if not cell.piece:
            return True
        return self.atk >= cell.piece.atk
    
    def is_move_valid(self, cell):
        '''
        Check if the move is valid.
        
        Args:
            cell (Cell): The cell to move to.
        
        Returns:
            bool: True if the move is valid, False otherwise.'''
        if not cell.is_in_board():
            return False
        if cell.is_river():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if cell.piece and not self.is_defeated_by_own_piece(cell):
            return False
        return True
    
    def available_moves(self, board):
        '''
        Get the available moves for the piece.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: The available moves for the piece.'''
        moves = []
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)
            if next_cell and self.is_move_valid(next_cell):
                moves.append(next_cell)
        return moves
    
    def weaker_pieces_positions(self, board):
        result = [self.side == PlayerSide.DARK and CellPosition.LIGHT_DEN or CellPosition.DARK_DEN]
        for row in board.cells:
            for cell in row:
                if cell.piece and cell.piece.side != self.side and cell.piece.atk <= self.atk:
                    result.append(cell.position)
        return result
