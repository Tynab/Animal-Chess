from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Cat(Piece):
    """
    Represents the Cat piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Cat class.

        Args:
            side (PlayerSide): The side of the player who owns the Cat piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Cat piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_CAT or PieceName.LIGHT_CAT,  # Piece name
            PieceDetail.CAT,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_CAT or CellPosition.LIGHT_CAT,  # Initial position
            PieceAtk.CAT,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_CAT or PieceAvatar.LIGHT_CAT,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_CAT or PieceArtWork.LIGHT_CAT  # Artwork
        )