import scripts.common as common
from pygame import transform, image
from scripts.common import Size, PlayerSide

class Piece:

    def __init__(self, name, detail, position, atk, side, image_path=None, artwork_path=None):
        self.name = name
        self.image = image_path and transform.scale(image.load(image_path), Size.CELL) or None
        self.artwork = artwork_path and transform.scale(image.load(artwork_path), Size.ARTWORK) or None
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side

    def copy(self):
        return Piece(self.name, self.detail, self.position, self.atk, self.side)

    def left(self, step, board):
        return None if self.position[0] - step < 0 else board.get_cell((self.position[0] - step, self.position[1]))
    
    def right(self, step, board):
        return None if self.position[0] + step >= common.W else board.get_cell((self.position[0] + step, self.position[1]))
    
    def up(self, step, board):
        return None if self.position[1] - step < 0 else board.get_cell((self.position[0], self.position[1] - step))
    
    def down(self, step, board):
        return None if self.position[1] + step >= common.H else board.get_cell((self.position[0], self.position[1] + step))
    
    def can_defeat(self, piece):
        return not piece or self.atk >= piece.atk

    def is_valid_cell(self, cell):
        return cell.is_in_board and not cell.is_river and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))

    def available_cells(self, board):
        return [cell for direction in [self.left, self.right, self.up, self.down] if (cell := direction(1, board)) and self.is_valid_cell(cell)]

    def weaker_pieces_positions(self, board):
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk]
    
    @property
    def is_dark(self):
        return PlayerSide.is_dark(self.side)

    @property
    def is_light(self):
        return PlayerSide.is_light(self.side)
