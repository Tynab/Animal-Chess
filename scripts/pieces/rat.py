import scripts.pieces.elephant as elephant
from scripts.common import *
from scripts.piece import *

class Rat(Piece):
    '''
    Rat class.
    
    Attributes:
    - side (PlayerSide): The player side.
    
    Methods:
    - __init__: Initializes the rat.
    - copy: Creates a copy of the rat.
    - can_defeat: Checks if the rat can defeat the piece.
    - is_valid_cell: Checks if a cell is a valid move for the piece.
    - weaker_pieces_positions: Returns a list of positions of weaker pieces.
    '''

    def __init__(self, side, is_copy=False):
        '''
        Initialize the rat.
        
        Args:
            side (PlayerSide): The player side.
            is_copy (bool): True if the piece is a copy, False otherwise.
        
        Returns:
            Rat: A new Rat instance.
        '''
        super().__init__(PieceName.rat(side), PieceDetail.RAT, CellPosition.rat(side), PieceAtk.RAT, side, None if is_copy else PieceAvatar.rat(side), None if is_copy else PieceArtWork.rat(side))

    def copy(self):
        '''
        Creates a copy of the rat.
        
        Returns:
            Rat: A new Rat instance.
        '''
        return Rat(self.side, True)

    def can_defeat(self, piece):
        '''
        Checks if the rat can defeat the piece.
        
        Args:
            piece (Piece): The piece to defeat.
            
        Returns:
            bool: True if the rat can defeat the piece, False otherwise.
        '''
        return isinstance(piece, elephant.Elephant) and self.atk != 0 or self.atk >= piece.atk

    def is_valid_cell(self, cell):
        '''
        Checks if a cell is a valid move for the piece.
        
        Args:
            cell (Cell): The cell to check.
        
        Returns:
            bool: True if the cell is a valid move, False otherwise.
        '''
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))

    def weaker_pieces_positions(self, board):
        '''
        Returns a list of positions of weaker pieces.
        
        Args:
            board (Board): The board.
        
        Returns:
            list: A list of positions of weaker pieces.
        '''
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk or isinstance(piece, elephant.Elephant) and self.atk != 0]
