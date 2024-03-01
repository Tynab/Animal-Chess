from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Tiger(Piece):
    """
    Represents the Tiger piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Tiger class.

        Args:
            side (PlayerSide): The side of the player who owns the Tiger piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Tiger piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_TIGER or PieceName.LIGHT_TIGER,  # Piece name
            PieceDetail.TIGER,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_TIGER or CellPosition.LIGHT_TIGER,  # Initial position
            PieceAtk.TIGER,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_TIGER or PieceAvatar.LIGHT_TIGER,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_TIGER or PieceArtWork.LIGHT_TIGER  # Artwork
        )

    def available_moves(self, board):
        """
        Determines the available moves for the Tiger piece.

        Args:
            board: The game board.

        Returns:
            A list of available moves.
        """
        moves = []  # Initialize an empty list to store the available moves
        # Iterate over the four possible directions
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)  # Get the next cell in the current direction
            new_cell = self.jump_over_river(next_cell, direction_method, board)  # Check if the Tiger can jump over a river
            if new_cell:  # If the Tiger can jump over a river, update the next cell
                next_cell = new_cell
            if next_cell and self.is_move_valid(next_cell):  # If the next cell is valid, add it to the list of available moves
                moves.append(next_cell)
        return moves  # Return the list of available moves

    def jump_over_river(self, cell, direction_method, board):
        """
        Checks if the Tiger can jump over a river.

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