import scripts.common as common
from pygame import *
from scripts.common import *
from scripts.pieces.rat import *
from scripts.pieces.cat import *
from scripts.pieces.dog import *
from scripts.pieces.wolf import *
from scripts.pieces.leopard import *
from scripts.pieces.tiger import *
from scripts.pieces.lion import *
from scripts.pieces.elephant import *

class Cell:
    '''
    The cell.
    
    Attributes:
    - label (CellLabel): The label.
    - position (tuple): The position.
    - image (Surface): The image.
    - piece (Piece): The piece.
    
    Methods:
    - copy(self): Copy the cell.
    - set_image(self, image_path): Set the image of the cell.
    - add_piece(self, piece): Add a piece to the cell.
    - remove_piece(self): Remove the piece from the cell.
    - is_occupied_own(self, side): Check if the cell is occupied by the player's own piece.
    - is_in_board: Check if the cell is in the board.
    - is_river: Check if the cell is a river.
    - is_dark_trap: Check if the cell is a dark trap.
    - is_light_trap: Check if the cell is a light trap.
    - is_trap: Check if the cell is a trap.
    - is_dark_den: Check if the cell is a dark den.
    - is_light_den: Check if the cell is a light den.
    - is_den: Check if the cell is a den.
    '''

    def __init__(self, label, position):
        '''
        Initialize the cell.
        
        Args:
            label (CellLabel): The label.
            position (tuple): The position.
        
        Returns:
            Cell: The cell.
        '''
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def copy(self):
        '''
        Copy the cell.
        
        Returns:
            Cell: The new cell.
        '''
        # Create a new cell with the same label and position
        cell = Cell(self.label, self.position)
        
        # Set the image of the new cell
        if self.piece:
            cell.add_piece(self.piece.copy())
        
        # Return the new cell
        return cell

    def set_image(self, image_path):
        '''
        Set the image of the cell.
        
        Args:
            image_path (str): The image path.
        '''
        self.image = transform.scale(image.load(image_path), Size.CELL)

    def add_piece(self, piece):
        '''
        Add a piece to the cell.
        
        Args:
            piece (Piece): The piece.
        '''
        self.piece = piece
        self.piece.position = self.position
        self.piece.atk = 0 if CellLabel.is_opponent_trap(self.label, piece.side) else {
            Rat: PieceAtk.RAT,
            Cat: PieceAtk.CAT,
            Dog: PieceAtk.DOG,
            Wolf: PieceAtk.WOLF,
            Leopard: PieceAtk.LEOPARD,
            Tiger: PieceAtk.TIGER,
            Lion: PieceAtk.LION,
            Elephant: PieceAtk.ELEPHANT,
        }[type(self.piece)]

    def remove_piece(self):
        '''
        Remove the piece from the cell.
        '''
        self.piece = None

    def is_occupied_own(self, side):
        '''
        Check if the cell is occupied by the player's own piece.
        
        Args:
            side (Side): The side.
            
        Returns:
            bool: True if the cell is occupied by the player's own piece, False otherwise.
        '''
        return self.piece and self.piece.side == side

    @property
    def is_in_board(self):
        '''
        Check if the cell is in the board.
        
        Returns:
            bool: True if the cell is in the board, False otherwise.
        '''
        return 0 <= self.position[0] < common.W and 0 <= self.position[1] < common.H

    @property
    def is_river(self):
        '''
        Check if the cell is a river.
        
        Returns:
            bool: True if the cell is a river, False otherwise.
        '''
        return CellLabel.is_river(self.label)
    
    @property
    def is_dark_trap(self):
        '''
        Check if the cell is a dark trap.
        
        Returns:
            bool: True if the cell is a dark trap, False otherwise.
        '''
        return CellLabel.is_dark_trap(self.label)
    
    @property
    def is_light_trap(self):
        '''
        Check if the cell is a light trap.
        
        Returns:
            bool: True if the cell is a light trap, False otherwise.
        '''
        return CellLabel.is_light_trap(self.label)
    
    @property
    def is_trap(self):
        '''
        Check if the cell is a trap.
        
        Returns:
            bool: True if the cell is a trap, False otherwise.
        '''
        return CellLabel.is_trap(self.label)
    
    @property
    def is_dark_den(self):
        '''
        Check if the cell is a dark den.
        
        Returns:
            bool: True if the cell is a dark den, False otherwise.
        '''
        return CellLabel.is_dark_den(self.label)
    
    @property
    def is_light_den(self):
        '''
        Check if the cell is a light den.
        
        Returns:
            bool: True if the cell is a light den, False otherwise.
        '''
        return CellLabel.is_light_den(self.label)
    
    @property
    def is_den(self):
        '''
        Check if the cell is a den.
        
        Returns:
            bool: True if the cell is a den, False otherwise.
        '''
        return CellLabel.is_den(self.label)
