from scripts.common import PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Dog(Piece):

    def __init__(self, side):
        super().__init__(PieceName.dog(side), PieceDetail.DOG, CellPosition.dog(side), PieceAtk.DOG, side, PieceAvatar.dog(side), PieceArtWork.dog(side))

    def copy(self):
        return Dog(self.side)

    def is_valid_cell(self, cell):
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))
