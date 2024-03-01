from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Dog(Piece):
    """
    Represents the Dog piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Dog class.

        Args:
            side (PlayerSide): The side of the player who owns the Dog piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Dog piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG,  # Piece name
            PieceDetail.DOG,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_DOG or CellPosition.LIGHT_DOG,  # Initial position
            PieceAtk.DOG,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_DOG or PieceAvatar.LIGHT_DOG,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_DOG or PieceArtWork.LIGHT_DOG  # Artwork
        )

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