class Log:
    '''
    Log class to store the game log.

    Attributes:
    - player (PlayerSide): The player side.
    - piece (str): The piece name.
    - x (int): The x position.
    - y (int): The y position.
    '''

    def __init__(self, player, piece, cell):
        '''
        Initialize the log.
        
        Args:
            player (Player): The player.
            piece (Piece): The piece.
            cell (Cell): The cell.

        Returns:
            Log: A new Log instance.
        '''
        self.player = player.side
        self.piece = piece.__class__.__name__
        self.x, self.y = cell.position
