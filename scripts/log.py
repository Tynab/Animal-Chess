class Log:
    """
    Represents a log in the Animal Chess game.
    """

    def __init__(self, player, piece, cell):
        """
        Initializes a new instance of the Log class.

        Args:
            player: The player who made the move.
            piece: The piece that was moved.
            cell: The cell that the piece was moved to.
        """
        self.player = player.side  # Store the side of the player
        self.piece = piece.__class__.__name__  # Store the name of the class of the piece
        self.x, self.y = cell.position  # Store the position of the cell