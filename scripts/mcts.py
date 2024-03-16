class MCTSNode:
    '''
    Monte Carlo Tree Search node class.

    Attributes:
    - board (Board): The board.
    - parent (MCTSNode): The parent node.
    - move (tuple): The move.
    - side (PlayerSide): The side.
    - children (list): The children nodes.
    - visits (int): The number of visits.
    - wins (int): The number of wins.
    '''

    def __init__(self, board, parent=None, move=None, side=None):
        '''
        Initialize the Monte Carlo Tree Search node.
        
        Args:
            board (Board): The board.
            parent (MCTSNode): The parent node.
            move (tuple): The move.
            side (PlayerSide): The side.
        '''
        self.board = board
        self.parent = parent
        self.move = move
        self.side = side
        self.children = []
        self.visits = 0
        self.wins = 0
