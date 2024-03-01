from scripts.common import CellPosition, PieceAtk, PieceAvatar, PieceArtWork, PieceDetail, PieceName, PlayerSide
from scripts.piece import Piece

import scripts.pieces.elephant as elephant

class Rat(Piece):
    """
    Represents the Rat piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Rat class.

        Args:
            side (PlayerSide): The side of the player who owns the Rat piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Rat piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT,  # Piece name
            PieceDetail.RAT,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_RAT or CellPosition.LIGHT_RAT,  # Initial position
            PieceAtk.RAT,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_RAT or PieceAvatar.LIGHT_RAT,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_RAT or PieceArtWork.LIGHT_RAT  # Artwork
        )

    def is_defeated_by_own_piece(self, cell):
        """
        Checks if the Rat is defeated by its own piece.

        Args:
            cell: The cell to check.

        Returns:
            True if the Rat is defeated, False otherwise.
        """
        if isinstance(cell.piece, elephant.Elephant):  # If the piece in the cell is an Elephant, the Rat is defeated
            return True
        return self.atk >= cell.piece.atk  # If the Rat's attack power is greater than or equal to the piece's attack power, the Rat is not defeated

    def is_move_valid(self, cell):
        """
        Checks if a move to the given cell is valid.

        Args:
            cell: The cell to move to.

        Returns:
            True if the move is valid, False otherwise.
        """
        if not cell.is_in_board():  # Check if the cell is within the board
            return False
        if cell.is_occupied_by_own_piece(self.side):  # Check if the cell is occupied by a piece of the same side
            return False
        if cell.piece and not self.is_defeated_by_own_piece(cell):  # Check if the cell is occupied by a piece of the opposite side that cannot be defeated
            return False
        return True  # If none of the above conditions are met, the move is valid