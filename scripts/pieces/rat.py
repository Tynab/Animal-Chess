import scripts.pieces.elephant as elephant
from scripts.common import CellPosition, PieceAtk, PieceAvatar, PieceArtWork, PieceDetail, PieceName, PlayerSide
from scripts.piece import Piece

class Rat(Piece):

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_RAT or PieceName.LIGHT_RAT,
            PieceDetail.RAT,
            side == PlayerSide.DARK and CellPosition.DARK_RAT or CellPosition.LIGHT_RAT,
            PieceAtk.RAT,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_RAT or PieceAvatar.LIGHT_RAT,
            side == PlayerSide.DARK and PieceArtWork.DARK_RAT or PieceArtWork.LIGHT_RAT
        )

    def clone(self):
        return Rat(self.side)

    def can_defeat(self, piece):
        return isinstance(piece, elephant.Elephant) or self.atk >= piece.atk

    def is_cell_valid(self, cell):
        return cell.is_in_board and not cell.is_occupied_own(self.side) and (not cell.piece or self.can_defeat(cell.piece))

    def weaker_pieces_positions(self, board):
        return [PlayerSide.opponent_den_position(self.side)] + [cell.position for row in board.cells for cell in row if cell.piece and cell.piece.side != self.side and isinstance(cell.piece, elephant.Elephant)]
