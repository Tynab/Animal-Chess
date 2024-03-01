from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Leopard(Piece):
    """
    Represents the Leopard piece in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Leopard class.

        Args:
            side (PlayerSide): The side of the player who owns the Leopard piece.
        """
        # Call the superclass's constructor with the appropriate parameters for a Leopard piece
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_LEOPARD or PieceName.LIGHT_LEOPARD,  # Piece name
            PieceDetail.LEOPARD,  # Piece detail
            side == PlayerSide.DARK and CellPosition.DARK_LEOPARD or CellPosition.LIGHT_LEOPARD,  # Initial position
            PieceAtk.LEOPARD,  # Attack power
            side,  # Player side
            side == PlayerSide.DARK and PieceAvatar.DARK_LEOPARD or PieceAvatar.LIGHT_LEOPARD,  # Avatar
            side == PlayerSide.DARK and PieceArtWork.DARK_LEOPARD or PieceArtWork.LIGHT_LEOPARD  # Artwork
        )