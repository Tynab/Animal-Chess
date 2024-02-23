from scripts.cell import CellPosition
from scripts.piece import Piece, PieceName, PieceDetail, PieceAtk, PieceAvatar, PieceArtWork
from scripts.player import PlayerSide

class Dog(Piece):
    def __init__(self, side):
        super().__init__(side == PlayerSide.DARK and PieceName.DARK_DOG or PieceName.LIGHT_DOG, PieceDetail.DOG, side == PlayerSide.DARK and CellPosition.DARK_DOG or CellPosition.LIGHT_DOG, PieceAtk.DOG, side, PieceAvatar.DARK_DOG, PieceArtWork.DARK_DOG)

    def is_move_valid(self, cell):
        if not cell.is_in_board():
            return False
        if cell.is_occupied_by_own_piece(self.side):
            return False
        if not cell.is_defeated_by_own_piece(self):
            return False
        return True
