import scripts.common as common
from pygame import *
from scripts.common import *

class Piece:
    '''
    The piece.
    
    Attributes:
    - name (str): The name.
    - image (Surface): The image.
    - artwork (Surface): The artwork.
    - detail (str): The detail.
    - position (tuple): The position.
    - atk (int): The attack power.
    - side (PlayerSide): The side.
    
    Methods:
    - copy(self): Copy the piece.
    - left(self, step, board): Get the cell to the left.
    - right(self, step, board): Get the cell to the right.
    - up(self, step, board): Get the cell above.
    - down(self, step, board): Get the cell below.
    - can_defeat(self, piece): Check if the piece can defeat another piece.
    - is_valid_cell(self, cell): Check if the cell is a valid move.
    - available_cells(self, board): Get the available cells.
    - weaker_pieces_positions(self, board): Get the positions of weaker pieces.
    - is_dark: Check if the piece belongs to the dark side.
    - is_light: Check if the piece belongs to the light side.
    '''

    def __init__(self, name, detail, position, atk, side, image_path=None, artwork_path=None):
        '''
        Initializes a new instance of the Piece class.
        
        Args:
            name (str): The name of the piece.
            detail (str): The details of the piece.
            position (tuple): The position of the piece on the board.
            atk (int): The attack power of the piece.
            side (PlayerSide): The side the piece belongs to.
            image_path (str): The path to the image of the piece.
            artwork_path (str): The path to the artwork of the piece.
            
        Returns:
            Piece: The new instance of the Piece class.
        '''
        self.name = name
        self.image = image_path and transform.scale(image.load(image_path), Size.CELL) or None
        self.artwork = artwork_path and transform.scale(image.load(artwork_path), Size.ARTWORK) or None
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side

    def copy(self):
        '''
        Creates a copy of the piece.
        
        Returns:
            Piece: The copy of the piece.
        '''
        return Piece(self.name, self.detail, self.position, self.atk, self.side)

    def left(self, step, board):
        '''
        Returns the cell to the left of the piece.
        
        Args:
            step (int): The step size.
            board (Board): The board.
            
        Returns:
            Cell: The cell to the left of the piece.
        '''
        return None if self.position[0] - step < 0 else board.get_cell((self.position[0] - step, self.position[1]))
    
    def right(self, step, board):
        '''
        Returns the cell to the right of the piece.
        
        Args:
            step (int): The step size.
            board (Board): The board.
            
        Returns:
            Cell: The cell to the right of the piece.
        '''
        return None if self.position[0] + step >= common.W else board.get_cell((self.position[0] + step, self.position[1]))
    
    def up(self, step, board):
        '''
        Returns the cell above the piece.
        
        Args:
            step (int): The step size.
            board (Board): The board.
        
        Returns:
            Cell: The cell above the piece.
        '''
        return None if self.position[1] - step < 0 else board.get_cell((self.position[0], self.position[1] - step))
    
    def down(self, step, board):
        '''
        Returns the cell below the piece.
        
        Args:
            step (int): The step size.
            board (Board): The board.
            
        Returns:
            Cell: The cell below the piece.
        '''
        return None if self.position[1] + step >= common.H else board.get_cell((self.position[0], self.position[1] + step))
    
    def can_defeat(self, piece):
        '''
        Checks if the piece can defeat another piece.
        
        Args:
            piece (Piece): The piece.
        
        Returns:
            bool: True if the piece can defeat another piece, False otherwise.
        '''
        return not piece or self.atk >= piece.atk

    def is_valid_cell(self, cell):
        '''
        Checks if a cell is a valid move for the piece.
        
        Args:
            cell (Cell): The cell.
        
        Returns:
            bool: True if the cell is a valid move for the piece, False otherwise.
        '''
        return cell.is_in_board and not cell.is_river and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))

    def available_cells(self, board):
        '''
        Returns a list of available cells for the piece.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: A list of available cells for the piece.
        '''
        # Get the available cells
        result = [cell for direction in [self.left, self.right, self.up, self.down] if (cell := direction(1, board)) and self.is_valid_cell(cell)]

        # Check if the piece is a rat
        if board.forbidden_move and board.forbidden_move[0] == self.position and board.forbidden_cell in result:
            result.remove(board.forbidden_cell)

        # Return the available cells
        return result

    def weaker_pieces_positions(self, board):
        '''
        Returns a list of positions of weaker pieces.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: A list of positions of weaker pieces.
        '''
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk]
    
    @property
    def is_dark(self):
        '''
        Checks if the piece belongs to the dark side.
        
        Returns:
            bool: True if the piece belongs to the dark side, False otherwise.
        '''
        return PlayerSide.is_dark(self.side)

    @property
    def is_light(self):
        '''
        Checks if the piece belongs to the light side.
        
        Returns:
            bool: True if the piece belongs to the light side, False otherwise.
        '''
        return PlayerSide.is_light(self.side)
