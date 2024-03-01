from scripts.common import GameState, PlayerSide, CellPosition

import scripts.board as board
import scripts.player as player

class GameManager:
    def __init__(self):
        self.game_state = GameState.NEW
        self.board = board.Board()
        self.players = {
            PlayerSide.DARK: player.Player(PlayerSide.DARK),
            PlayerSide.LIGHT: player.Player(PlayerSide.LIGHT)
        }
        self.current_player = self.players[PlayerSide.LIGHT]
        self.opponent_player = self.players[PlayerSide.DARK]
        self.selected_piece = None
        self.game_result = None

    def set_game_state(self, game_state):
        self.game_state = game_state

    def set_current_player(self, player):
        self.current_player = player
    
    def set_selected_piece(self, piece):
        self.selected_piece = piece

    def set_game_result(self, game_result):
        self.game_result = game_result
        
    def get_player(self, side):
        return self.players[side]

    def switch_player(self):
        self.current_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.LIGHT] or self.players[PlayerSide.DARK]
        self.opponent_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.DARK] or self.players[PlayerSide.LIGHT]
    
    def handle_piece_selection(self, mouse_position):
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece and cell.piece.side == self.current_player.side:
            self.selected_piece = cell.piece

    def handle_piece_move(self, mouse_position):
        if not self.selected_piece:
            return False
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if target_cell in self.selected_piece.available_moves(self.board):
            source_cell.remove_piece()
            target_cell.add_piece(self.selected_piece)
            self.selected_piece = None
            if self.check_game_end(target_cell):
                return True
            self.switch_player()
            return True
        return False

    def check_game_end(self, destination_cell):
        if destination_cell.position == CellPosition.DARK_DEN and self.current_player.side == PlayerSide.LIGHT:
            self.game_state = GameState.OVER
            self.game_result = 'LIGHT\nWIN!!!'
            return True
        if destination_cell.position == CellPosition.LIGHT_DEN and self.current_player.side == PlayerSide.DARK:
            self.game_state = GameState.OVER
            self.game_result = 'DARK\nWIN!!!'
            return True
        if len(self.players[self.current_player.side == PlayerSide.LIGHT and PlayerSide.DARK or PlayerSide.LIGHT].pieces) == 0:
            self.game_state = GameState.OVER
            self.game_result = f'{self.current_player.side.value.upper()}\nWIN!!!'
            return True
        return False
