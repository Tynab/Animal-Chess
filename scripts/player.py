from scripts.common import PlayerSide, CellPosition

class Player:
    '''
    The player.
    '''
    def __init__(self, side, pieces):
        self.side = side
        self.pieces = pieces
        self.den = side == PlayerSide.DARK and CellPosition.DARK_DEN or CellPosition.LIGHT_DEN
        self.traps = side == PlayerSide.DARK and [CellPosition.DARK_TRAP_1, CellPosition.DARK_TRAP_2, CellPosition.DARK_TRAP_3] or [CellPosition.LIGHT_TRAP_1, CellPosition.LIGHT_TRAP_2, CellPosition.LIGHT_TRAP_3]
    
    def add_piece(self, piece):
        '''
        Add the piece to the player.
        
        Args:
            piece (Piece): The piece to be added.
        '''
        self.pieces.append(piece)

    def remove_piece(self, piece):
        '''
        Remove the piece from the player.
        
        Args:
            piece (Piece): The piece to be removed.
        '''
        self.pieces.remove(piece)