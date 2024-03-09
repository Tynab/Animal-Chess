import scripts.pieces.elephant as elephant
from scripts.common import CellPosition, PieceAtk, PieceAvatar, PieceArtWork, PieceDetail, PieceName, PlayerSide
from scripts.piece import Piece

class Rat(Piece):

    def __init__(self, side):
        super().__init__(PieceName.rat(side), PieceDetail.RAT, CellPosition.rat(side), PieceAtk.RAT, side, PieceAvatar.rat(side), PieceArtWork.rat(side))

    def copy(self):
        return Rat(self.side)

    def can_defeat(self, piece):
        return isinstance(piece, elephant.Elephant) or self.atk >= piece.atk

    def is_valid_cell(self, cell):
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))

    def weaker_pieces_positions(self, board):
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk or isinstance(piece, elephant.Elephant)]
