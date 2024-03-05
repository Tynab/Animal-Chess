import scripts.board as board
import scripts.bot as bot
import scripts.player as player
from scripts.common import GameState, PlayerSide, CellPosition

class GameManager:
    def __init__(self):
        self.board = board.Board()
        self.players = {
            PlayerSide.DARK: player.Player(PlayerSide.DARK, [cell.piece for row in self.board.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.DARK]),
            PlayerSide.LIGHT: player.Player(PlayerSide.LIGHT, [cell.piece for row in self.board.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.LIGHT])
        }
        self.game_state = GameState.NEW
        self.current_player = self.players[PlayerSide.LIGHT]
        self.opponent_player = self.players[PlayerSide.DARK]
        self.selected_piece = None
        self.game_result = None

    def switch_player(self):
        self.current_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.LIGHT] or self.players[PlayerSide.DARK]
        self.opponent_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.LIGHT] or self.players[PlayerSide.DARK]
        if self.current_player.side == PlayerSide.DARK:
            self.computer_move()
        self.board.captured_pieces = []
    
    def handle_piece_selection(self, mouse_position):
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece and cell.piece.side == self.current_player.side:
            self.selected_piece = cell.piece
            if self.selected_piece.side == PlayerSide.LIGHT:
                cc = self.board.clone()
                bot.shortest_paths(cc, self.selected_piece.clone(), self.selected_piece.position, self.selected_piece.weaker_pieces_positions(cc))

    def handle_piece_move(self, mouse_position):
        if not self.selected_piece:
            return False
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if target_cell in self.selected_piece.available_moves(self.board):
            self.board.make_move((source_cell.position, target_cell.position))
            self.selected_piece = None
            if self.check_game_end(target_cell):
                return True
            self.switch_player()
            return True
        return False

    def computer_move(self):
        if self.current_player.side == PlayerSide.DARK:
            _, move = bot.minimax(self.board, 3, float('-inf'), float('inf'), True)
            if move:
                self.board.make_move(move)
            else:
                self.board.make_move(bot.random_move(self.board))
            if self.check_game_end(self.board.get_cell(move[1])):
                return
            self.switch_player()

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
            self.game_result = f'{self.current_player.side.upper()}\nWIN!!!'
            return True
        return False
