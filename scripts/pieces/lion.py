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
            next_cell = self.jump_over_river(next_cell, direction_method, board)
            if self.is_move_valid(next_cell):
                moves.append(next_cell)
        return moves
        
    def jump_over_river(self, position, direction_method, board):
        '''
        Jump over the river.
        
        Args:
            position (Cell): The position to move to.
            direction_method (function): The direction method.
            board (Board): The board.
        
        Returns:
            Cell: The position to move to.
        '''
        while position.is_river():
            position = direction_method(1, board)
        return position
