class Log:
    '''
    Log class to store the game log.
    '''
    def __init__(self, player, piece, cell):
        self.player = player.side
        self.piece = piece.__class__.__name__
        self.x, self.y = cell.position
