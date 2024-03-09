import scripts.pieces.rat as rat
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Elephant(Piece):

    def __init__(self, side):
        super().__init__(PieceName.elephant(side), PieceDetail.ELEPHANT, CellPosition.elephant(side), PieceAtk.ELEPHANT, side, PieceAvatar.elephant(side), PieceArtWork.elephant(side))

    def copy(self):
        return Elephant(self.side)

    def can_defeat(self, piece):
        return not isinstance(piece, rat.Rat) and self.atk >= piece.atk

    def weaker_pieces_positions(self, board):
        return [PlayerSide.opponent_den_position(self.side)] + [piece.position for piece in board.pieces_of[PlayerSide.opponent_of(self.side)] if piece.atk < self.atk and not isinstance(piece, rat.Rat)]
