from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Wolf(Piece):
    """
    Represents the Wolf piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Wolf class.

        Args:
            side (PlayerSide): The side of the player who owns the Wolf piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Wolf piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_WOLF or PieceName.LIGHT_WOLF,  # Piece name
            PieceDetail.WOLF,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_WOLF or CellPosition.LIGHT_WOLF,  # Initial position
            PieceAtk.WOLF,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_WOLF or PieceAvatar.LIGHT_WOLF,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_WOLF or PieceArtWork.LIGHT_WOLF  # Artwork
        )