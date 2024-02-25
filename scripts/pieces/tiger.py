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
    