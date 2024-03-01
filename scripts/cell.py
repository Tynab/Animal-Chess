from pygame import transform, image
from scripts.common import Size, CellLabel, PlayerSide, PieceAtk
from scripts.pieces.rat import Rat
from scripts.pieces.cat import Cat
from scripts.pieces.dog import Dog
from scripts.pieces.wolf import Wolf
from scripts.pieces.leopard import Leopard
from scripts.pieces.tiger import Tiger
from scripts.pieces.lion import Lion
from scripts.pieces.elephant import Elephant

import scripts.common as common

class Cell:
    """
    Represents a cell in the Animal Chess game.
    """

    def __init__(self, label, position):
        """
        Initializes a new instance of the Cell class.

        Args:
            label: The label of the cell.
            position: The position of the cell.
        """
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def set_label(self, label):
        """
        Sets the label of the cell.

        Args:
            label: The new label.
        """
        self.label = label

    def set_image(self, image_path):
        """
        Sets the image of the cell.

        Args:
            image_path: The path to the new image.
        """
        self.image = transform.scale(image.load(image_path), Size.CELL)  # Load and scale the image

    def add_piece(self, piece):
        """
        Adds a piece to the cell.

        Args:
            piece: The piece to add.
        """
        self.piece = piece
        self.piece.move(self.position)  # Move the piece to the cell's position
        # If the cell is a trap and the piece is of the opposite side, set the piece's attack power to 0
        if self.label == CellLabel.DARK_TRAP and self.piece.side == PlayerSide.LIGHT or self.label == CellLabel.LIGHT_TRAP and self.piece.side == PlayerSide.DARK:
            self.piece.set_atk(0)
        # If the piece's attack power is 0, set it to the appropriate value based on the type of the piece
        elif self.piece.atk == 0:
            if isinstance(self.piece, Rat):
                self.piece.set_atk(PieceAtk.RAT)
            elif isinstance(self.piece, Cat):
                self.piece.set_atk(PieceAtk.CAT)
            elif isinstance(self.piece, Dog):
                self.piece.set_atk(PieceAtk.DOG)
            elif isinstance(self.piece, Wolf):
                self.piece.set_atk(PieceAtk.WOLF)
            elif isinstance(self.piece, Leopard):
                self.piece.set_atk(PieceAtk.LEOPARD)
            elif isinstance(self.piece, Tiger):
                self.piece.set_atk(PieceAtk.TIGER)
            elif isinstance(self.piece, Lion):
                self.piece.set_atk(PieceAtk.LION)
            elif isinstance(self.piece, Elephant):
                self.piece.set_atk(PieceAtk.ELEPHANT)

    def remove_piece(self):
        """
        Removes the piece from the cell.
        """
        self.piece = None

    def is_in_board(self):
        """
        Checks if the cell is within the board.

        Returns:
            True if the cell is within the board, False otherwise.
        """
        return 0 <= self.position[0] < common.W and 0 <= self.position[1] < common.H
    
    def is_empty(self):
        """
        Checks if the cell is empty.

        Returns:
            True if the cell is empty, False otherwise.
        """
        return not self.piece
    
    def is_river(self):
        """
        Checks if the cell is a river.

        Returns:
            True if the cell is a river, False otherwise.
        """
        return self.label == CellLabel.RIVER
    
    def is_opponent_trap(self, side):
        """
        Checks if the cell is an opponent's trap.

        Args:
            side: The side of the player.

        Returns:
            True if the cell is an opponent's trap, False otherwise.
        """
        if self.label in [CellLabel.DARK_TRAP, CellLabel.LIGHT_TRAP]:
            return self.label != side
        return False
    
    def is_opponent_den(self, side):
        """
        Checks if the cell is an opponent's den.

        Args:
            side: The side of the player.

        Returns:
            True if the cell is an opponent's den, False otherwise.
        """
        if self.label in [CellLabel.DARK_DEN, CellLabel.LIGHT_DEN]:
            return self.label != side
        return False
    
    def is_occupied_by_own_piece(self, side):
        """
        Checks if the cell is occupied by a piece of the player's side.

        Args:
            side: The side of the player.

        Returns:
            True if the cell is occupied by a piece of the player's side, False otherwise.
        """
        return self.piece and self.piece.side == side