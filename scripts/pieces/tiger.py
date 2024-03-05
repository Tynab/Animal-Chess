from scripts.common import PlayerSide, PieceName, PieceDetail, CellPosition, PieceAtk, PieceAvatar, PieceArtWork
from scripts.piece import Piece

class Tiger(Piece):
    '''
    The Tiger piece.
    '''

    def __init__(self, side):
        super().__init__(
            side == PlayerSide.DARK and PieceName.DARK_TIGER or PieceName.LIGHT_TIGER,
            PieceDetail.TIGER,
            side == PlayerSide.DARK and CellPosition.DARK_TIGER or CellPosition.LIGHT_TIGER,
            PieceAtk.TIGER,
            side,
            side == PlayerSide.DARK and PieceAvatar.DARK_TIGER or PieceAvatar.LIGHT_TIGER,
            side == PlayerSide.DARK and PieceArtWork.DARK_TIGER or PieceArtWork.LIGHT_TIGER
        )

    def clone(self):
        return Tiger(self.side)

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
