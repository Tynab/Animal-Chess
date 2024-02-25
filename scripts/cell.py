import scripts.common as common
from pygame import transform, image
from scripts.common import CellLabel, Size

class Cell:
    '''
    The cell of the board.
    '''
    def __init__(self, label, position):
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def set_label(self, label):
        '''
        Set the label of the cell.
        
        Args:
            label (CellLabel): The label of the cell.
        '''
        self.label = label

    def set_image(self, image_path):
        '''
        Set the image of the cell.
        
        Args:
            image_path (str): The path of the image.
        '''
        self.image = transform.scale(image.load(image_path), Size.CELL)

    def add_piece(self, piece):
        '''
        Add a piece to the cell.
        
        Args:
            piece (Piece): The piece to be added.
        '''
        self.piece = piece
        self.piece.move(self.position)

    def remove_piece(self):
        '''
        Remove the piece from the cell.
        '''
        self.piece = None

    def is_in_board(self):
        '''
        Check if the cell is in the board.
        
        Returns:
            bool: True if the cell is in the board, False otherwise.
        '''
        return 0 <= self.position[0] < common.W and 0 <= self.position[1] < common.H
    
    def is_empty(self):
        '''
        Check if the cell is empty.
        
        Returns:
            bool: True if the cell is empty, False otherwise.
        '''
        return not self.piece
    
    def is_river(self):
        '''
        Check if the cell is river.
        
        Returns:
            bool: True if the cell is river, False otherwise.
        '''
        return self.label == CellLabel.RIVER
    
    def is_opponent_trap(self, side):
        '''
        Check if the cell is opponent trap.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: True if the cell is opponent trap, False otherwise.
        '''
        if self.label in [CellLabel.DARK_TRAP, CellLabel.LIGHT_TRAP]:
            return self.label != side
        return False
    
    def is_opponent_den(self, side):
        '''
        Check if the cell is opponent den.
        
        Args:
            side (PlayerSide): The side of the player.
            
        Returns:
            bool: True if the cell is opponent den, False otherwise.
        '''
        if self.label in [CellLabel.DARK_DEN, CellLabel.LIGHT_DEN]:
            return self.label != side
        return False
    
    def is_occupied_by_own_piece(self, side):
        '''
        Check if the cell is occupied by own piece.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: True if the cell is occupied by own piece, False otherwise.
        '''
        return self.piece and self.piece.side == side
