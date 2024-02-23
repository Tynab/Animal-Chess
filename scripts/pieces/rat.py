from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Rat(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT, PieceDetail.RAT, side == PlayerSide.DARK and CellPosition.DARK_RAT or CellPosition.LIGHT_RAT, PieceAtk.RAT, side, PieceAvatar.DARK_RAT, PieceArtWork.DARK_RAT)

    def is_move_valid(self, cell):
        if not cell.is_in_board():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if not cell.is_defeated_by_own_piece(self):
            return False
        return True

