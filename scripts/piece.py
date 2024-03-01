from pygame import transform, image
from scripts.common import Size

import scripts.common as common

class Piece:
    """
    Represents a piece in the Animal Chess game.
    """

    def __init__(self, name, detail, position, atk, side, image_path, artwork_path):
        """
        Initializes a new instance of the Piece class.

        Args:
            name: The name of the piece.
            detail: The detail of the piece.
            position: The initial position of the piece.
            atk: The attack power of the piece.
            side: The side of the player who owns the piece.
            image_path: The path to the image of the piece.
            artwork_path: The path to the artwork of the piece.
        """
        self.name = name
        self.image = transform.scale(image.load(image_path), Size.CELL)  # Load and scale the image of the piece
        self.artwork_ = transform.scale(image.load(artwork_path), Size.ARTWORK)  # Load and scale the artwork of the piece
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side

    def set_atk(self, atk):
        """
        Sets the attack power of the piece.

        Args:
            atk: The new attack power.
        """
        self.atk = atk

    def move(self, position):
        """
        Moves the piece to a new position.

        Args:
            position: The new position.
        """
        self.position = position

    def left(self, step, board):
        """
        Moves the piece to the left.

        Args:
            step: The number of steps to move.
            board: The game board.

        Returns:
            The new cell after moving, or None if the move is not valid.
        """
        if self.position[0] - step < 0:  # Check if the move is within the board
            return None
        return board.get_cell((self.position[0] - step, self.position[1]))  # Return the new cell after moving

    def right(self, step, board):
        """
        Moves the piece to the right.

        Args:
            step: The number of steps to move.
            board: The game board.

        Returns:
            The new cell after moving, or None if the move is not valid.
        """
        if self.position[0] + step >= common.W:  # Check if the move is within the board
            return None
        return board.get_cell((self.position[0] + step, self.position[1]))  # Return the new cell after moving

    def up(self, step, board):
        """
        Moves the piece up.

        Args:
            step: The number of steps to move.
            board: The game board.

        Returns:
            The new cell after moving, or None if the move is not valid.
        """
        if self.position[1] - step < 0:  # Check if the move is within the board
            return None
        return board.get_cell((self.position[0], self.position[1] - step))  # Return the new cell after moving

    def down(self, step, board):
        """
        Moves the piece down.

        Args:
            step: The number of steps to move.
            board: The game board.

        Returns:
            The new cell after moving, or None if the move is not valid.
        """
        if self.position[1] + step >= common.H:  # Check if the move is within the board
            return None
        return board.get_cell((self.position[0], self.position[1] + step))  # Return the new cell after moving

    def is_defeated_by_own_piece(self, cell):
        """
        Checks if the piece is defeated by its own piece.

        Args:
            cell: The cell to check.

        Returns:
            True if the piece is defeated, False otherwise.
        """
        if not cell.piece:  # If the cell is not occupied by a piece, the piece is defeated
            return True
        return self.atk >= cell.piece.atk  # If the piece's attack power is greater than or equal to the cell's piece's attack power, the piece is not defeated

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
        if cell.is_river():  # Check if the cell is a river
            return False
        if cell.is_occupied_by_own_piece(self.side):  # Check if the cell is occupied by a piece of the same side
            return False
        if cell.piece and not self.is_defeated_by_own_piece(cell):  # Check if the cell is occupied by a piece of the opposite side that cannot be defeated
            return False
        return True  # If none of the above conditions are met, the move is valid

    def available_moves(self, board):
        """
        Determines the available moves for the piece.

        Args:
            board: The game board.

        Returns:
            A list of available moves.
        """
        moves = []  # Initialize an empty list to store the available moves
        # Iterate over the four possible directions
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)  # Get the next cell in the current direction
            if next_cell and self.is_move_valid(next_cell):  # If the next cell is valid, add it to the list of available moves
                moves.append(next_cell)
        return moves  # Return the list of available moves