from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Lion(Piece):
    '''
    The Lion piece.
    '''

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_LION or PieceName.LIGHT_LION,
            PieceDetail.LION,
            side == PlayerSide.DARK and CellPosition.DARK_LION or CellPosition.LIGHT_LION,
            PieceAtk.LION,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_LION or PieceAvatar.LIGHT_LION,
            side == PlayerSide.DARK and PieceArtWork.DARK_LION or PieceArtWork.LIGHT_LION
        )

    def clone(self):
        return Lion(self.side)

    def available_moves(self, board):
        '''
        Get available moves for the piece.

        Args:
            board (Board): The board.

        Returns:
            list: The available moves.
        '''
        moves = []
        for direction_method in [self.left, self.right, self.up, self.down]:
            next_cell = direction_method(1, board)
            new_cell = self.jump_over_river(next_cell, direction_method, board)
            if new_cell:
                next_cell = new_cell
            if next_cell and self.is_move_valid(next_cell):
                moves.append(next_cell)
        return moves

    def jump_over_river(self, cell, direction_method, board):
        '''
        Jump over the river.

        Args:
            cell (Cell): The position to move to.
            direction_method (function): The direction method.
            board (Board): The board.

        Returns:
            Cell: The position to move to.
        '''
        if not cell:
            return cell
        step = 1
        while cell.is_river():
            cell = direction_method(step, board)
            if cell and cell.piece:
                return None and cell.is_river() or cell
            step += 1
        return cell
