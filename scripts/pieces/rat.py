import scripts.pieces.elephant as elephant
from scripts.common import CellPosition, PieceAtk, PieceAvatar, PieceArtWork, PieceDetail, PieceName, PlayerSide
from scripts.piece import Piece

class Rat(Piece):
    '''
    Rat class.

    Attributes:
    - side (PlayerSide): The player side.
    '''

    def __init__(self, side):
        '''
        Initialize the rat.
        
        Args:
            side (PlayerSide): The player side.
        '''
        super().__init__(PieceName.rat(side), PieceDetail.RAT, CellPosition.rat(side), PieceAtk.RAT, side, PieceAvatar.rat(side), PieceArtWork.rat(side))

    def copy(self):
        '''
        Creates a copy of the rat.
        
        Returns:
            Rat: The copied rat.
        '''
        return Rat(self.side)

    def can_defeat(self, piece):
        '''
        Checks if the rat can defeat the piece.
        
        Args:
            piece (Piece): The piece.
        
        Returns:
            bool: True if the rat can defeat the piece, False otherwise.
        '''
        return isinstance(piece, elephant.Elephant) or self.atk >= piece.atk

    def is_valid_cell(self, cell):
        '''
        Checks if a cell is a valid move for the piece.
        
        Args:
            cell (Cell): The cell.
            
        Returns:
            bool: True if the cell is a valid move for the piece, False otherwise.
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
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk or isinstance(piece, elephant.Elephant)]
