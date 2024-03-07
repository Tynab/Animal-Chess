import scripts.pieces.rat as rat
from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Elephant(Piece):

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_ELEPHANT or PieceName.LIGHT_ELEPHANT,
            PieceDetail.ELEPHANT,
            side == PlayerSide.DARK and CellPosition.DARK_ELEPHANT or CellPosition.LIGHT_ELEPHANT,
            PieceAtk.ELEPHANT,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_ELEPHANT or PieceAvatar.LIGHT_ELEPHANT,
            side == PlayerSide.DARK and PieceArtWork.DARK_ELEPHANT or PieceArtWork.LIGHT_ELEPHANT
        )

    def clone(self):
        return Elephant(self.side)

    def can_defeat(self, piece):
        return not isinstance(piece, rat.Rat) and self.atk >= piece.atk

    def weaker_pieces_positions(self, board):
        return [PlayerSide.opponent_den_position(self.side)] + [cell.position for row in board.cells for cell in row if cell.piece and cell.piece.side != self.side and cell.piece.atk <= self.atk and not isinstance(cell.piece, rat.Rat)]
