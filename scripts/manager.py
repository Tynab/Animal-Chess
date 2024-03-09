import random
from scripts.board import Board
from scripts.bot import Bot
from scripts.common import GameState, PlayerSide, GameMode

class GameManager:

    def __init__(self):
        self.board = Board()
        dark_pieces = []
        light_pieces = []
        for row in self.board.cells:
            for cell in row:
                if cell.piece:
                    if cell.piece.is_dark:
                        dark_pieces.append(cell.piece)
                    elif cell.piece.is_light:
                        light_pieces.append(cell.piece)
        self.game_state = GameState.NEW
        self.game_mode = GameMode.PvC
        self.game_result = None
        self.current_player = PlayerSide.LIGHT
        self.opponent_player = PlayerSide.opponent_of(self.current_player)
        self.selected_piece = None

    def switch_player(self):
        self.current_player, self.opponent_player = self.opponent_player, self.current_player
        if self.game_mode == GameMode.PvC and self.current_player == PlayerSide.DARK:
            self.computer_move()
        self.board.captured_pieces = []
    
    def handle_piece_selection(self, mouse_position):
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece and cell.piece.side == self.current_player:
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
        if self.game_mode == GameMode.PvC and self.current_player == PlayerSide.DARK:
            cc = self.board.copy()
            _, move = Bot.minimax_alpha_beta_pruning(cc, self.current_player, 3, float('-inf'), float('inf'), True)
            if move:
                self.board.make_move(move)
            else:
                min_path = float('inf')
                moves = []
                for piece in self.board.pieces_of[self.current_player]:
                    paths = Bot.shortest_paths(self.board, piece, piece.position, piece.weaker_pieces_positions(self.board))
                    if paths and paths[0] and paths[0][0] and paths[0][0][0] < min_path:
                        min_path = paths[0][0][0]
                        # move = paths[0][0][1]
                        # cc = paths[0]
                        # for c in cc:
                        #     qq = c[1]
                        #     moves.append(c[1])
                        moves = [path[1] for path in paths[0]]
                if moves:
                    move = random.choice(moves)
                    self.board.make_move(move)
            if self.check_game_end():
                return
            self.switch_player()

    def check_game_end(self):
        if len(self.board.pieces_of[self.opponent_player]) == 0 or self.board.is_opponent_den_invaded(self.current_player):
            self.game_state = GameState.OVER
            self.game_result = f'{self.current_player.upper()}\nWIN!!!'
            return True
        return False
