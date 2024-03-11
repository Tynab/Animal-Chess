import random
from scripts.board import Board
from scripts.bot import Bot
from scripts.common import GameState, PlayerSide, GameMode

class GameManager:

    def __init__(self):
        self.board = Board()
        self.game_state = GameState.NEW
        self.game_mode = GameMode.PvC
        self.game_result = None
        self.current_side = PlayerSide.LIGHT
        self.opponent_side = PlayerSide.opponent_of(self.current_side)
        self.selected_piece = None

    def switch_player(self):
        self.current_side, self.opponent_side = self.opponent_side, self.current_side
        self.board.captured_pieces.clear()
    
    def handle_piece_selection(self, mouse_position):
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece and cell.piece.side == self.current_side:
            self.selected_piece = cell.piece

    def handle_piece_move(self, mouse_position):
        if not self.selected_piece:
            return False
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if target_cell in self.selected_piece.available_cells(self.board):
            self.board.make_move((source_cell.position, target_cell.position))
            self.selected_piece = None
            if self.check_game_end():
                return True
            self.switch_player()
            return True
        return False

    def computer_move(self):
        _, best_moves = Bot.minimax_alpha_beta_pruning(self.board.copy(), self.current_side, 3, float('-inf'), float('inf'), True)
        min_path = float('inf')
        moves = []
        for piece in self.board.pieces_of[self.current_side]:
            paths = Bot.breadth_first_search(self.board, piece, piece.position, piece.weaker_pieces_positions(self.board))
            if paths and paths[0] and paths[0][0]:
                path_length = paths[0][0][0]
                valid_moves = [move for move in [tuple(path[1][:2]) for path in paths[0]] if move in best_moves]
                if not valid_moves:
                    continue
                if path_length < min_path:
                    min_path = path_length
                    moves = valid_moves
                elif path_length == min_path:
                    moves.extend(valid_moves)
        move = moves and random.choice(moves) or random.choice(best_moves)
        self.board.make_move(move)
        if self.check_game_end():
            return
        self.switch_player()

    def check_game_end(self):
        if self.board.is_opponent_pieceless(self.current_side) or self.board.is_opponent_den_invaded(self.current_side):
            self.game_state = GameState.OVER
            self.game_result = f'{self.current_side.upper()}\nWIN!!!'
            return True
        return False
