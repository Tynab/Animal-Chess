from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Lion(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION, PieceDetail.LION, side == PlayerSide.DARK and CellPosition.DARK_LION or CellPosition.LIGHT_LION, PieceAtk.LION, side, PieceAvatar.DARK_LION, PieceArtWork.DARK_LION)

    def is_move_valid(self, cell):
        if not cell.is_in_board():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if not cell.is_defeated_by_own_piece(self):
            return False
        return True
    
    def available_moves(self, board):
        moves = []
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)
            next_cell = self.jump_over_river(next_cell, direction_method, board)
            if self.is_move_valid(next_cell):
                moves.append(next_cell)
        return moves
        
    def jump_over_river(self, position, direction_method, board):
        while position.is_river():
            position = direction_method(1, board)
        return position
