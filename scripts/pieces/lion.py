from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Lion(Piece):
    """
    Represents the Lion piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Lion class.

        Args:
            side (PlayerSide): The side of the player who owns the Lion piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Lion piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION,  # Piece name
            PieceDetail.LION,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_LION or CellPosition.LIGHT_LION,  # Initial position
            PieceAtk.LION,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_LION or PieceAvatar.LIGHT_LION,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_LION or PieceArtWork.LIGHT_LION  # Artwork
        )

    def available_moves(self, board):
        """
        Determines the available moves for the Lion piece.

        Args:
            board: The game board.

        Returns:
            A list of available moves.
        """
        moves = []  # Initialize an empty list to store the available moves
        # Iterate over the four possible directions
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)  # Get the next cell in the current direction
            new_cell = self.jump_over_river(next_cell, direction_method, board)  # Check if the Lion can jump over a river
            if new_cell:  # If the Lion can jump over a river, update the next cell
                next_cell = new_cell
            if next_cell and self.is_move_valid(next_cell):  # If the next cell is valid, add it to the list of available moves
                moves.append(next_cell)
        return moves  # Return the list of available moves

    def jump_over_river(self, cell, direction_method, board):
        """
        Checks if the Lion can jump over a river.

        Args:
            cell: The cell to jump to.
            direction_method: The method to use to determine the direction of the jump.
            board: The game board.

        Returns:
            The cell after the jump if the jump is valid, None otherwise.
        """
        if not cell:  # If the cell is None, return None
            return cell
        step = 1  # Initialize the step counter
        while cell.is_river():  # While the cell is a river
            cell = direction_method(step, board)  # Get the next cell in the current direction
            # If the cell is occupied by a piece or is not a river, return None
            if cell and cell.piece or not cell.is_river():
                return None and cell.is_river() or cell
            step += 1  # Increment the step counter
        return cell  # Return the cell after the jump