import scripts.common as common
from pygame import transform, image
from scripts.common import Size, PlayerSide, CellPosition

class Piece:

    def __init__(self, name, detail, position, atk, side, image_path=None, artwork_path=None):
        self.name = name
        self.image = image_path and transform.scale(image.load(image_path), Size.CELL) or None
        self.artwork = artwork_path and transform.scale(image.load(artwork_path), Size.ARTWORK) or None
        self.detail = detail
        self.position = position
        self.atk = atk
        self.side = side

    def clone(self):
        return Piece(self.name, self.detail, self.position, self.atk, self.side)

    def left(self, step, board):
        if self.position[0] - step < 0:
            return None
        return board.get_cell((self.position[0] - step, self.position[1]))
    
    def right(self, step, board):
        if self.position[0] + step >= common.W:
            return None
        return board.get_cell((self.position[0] + step, self.position[1]))
    
    def up(self, step, board):
        if self.position[1] - step < 0:
            return None
        return board.get_cell((self.position[0], self.position[1] - step))
    
    def down(self, step, board):
        if self.position[1] + step >= common.H:
            return None
        return board.get_cell((self.position[0], self.position[1] + step))
    
    def can_defeat(self, piece):
        return not piece or self.atk >= piece.atk
    
    def is_cell_valid(self, cell):
        if not cell.is_in_board:
            return False
        if cell.is_river:
            return False
        if cell.is_occupied_own(self.side):
            return False
        if cell.piece and not self.can_defeat(cell.piece):
            return False
        return True
    
    def available_cells(self, board):
        moves = []
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)
            if next_cell and self.is_cell_valid(next_cell):
                moves.append(next_cell)
        return moves
    
    def weaker_pieces_positions(self, board):
        result = [self.is_dark and CellPosition.LIGHT_DEN or CellPosition.DARK_DEN]
        for row in board.cells:
            for cell in row:
                if cell.piece and cell.piece.side != self.side and cell.piece.atk <= self.atk:
                    result.append(cell.position)
        return result
    
    @property
    def is_dark(self):
        return self.side == PlayerSide.DARK
    
    @property
    def is_light(self):
        return self.side == PlayerSide.LIGHT
