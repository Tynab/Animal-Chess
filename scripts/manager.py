import random
import scripts.board as board
import scripts.player as player
from scripts.common import GameState, PlayerSide, CellPosition

class GameManager:
    '''
    The game manager.
    '''
    def __init__(self):
        self.game_state = GameState.NEW
        self.board = board.Board()
        self.players = {
            PlayerSide.DARK: player.Player(PlayerSide.DARK, [cell.piece for row in self.board.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.DARK]),
            PlayerSide.LIGHT: player.Player(PlayerSide.LIGHT, [cell.piece for row in self.board.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.LIGHT])
        }
        self.current_player = self.players[PlayerSide.LIGHT]
        self.opponent_player = self.players[PlayerSide.DARK]
        self.selected_piece = None
        self.game_result = None

    def set_game_state(self, game_state):
        '''
        Set the game state.
        
        Args:
            game_state (GameState): The game state.
        '''
        self.game_state = game_state

    def set_current_player(self, player):
        '''
        Set the current player.
        
        Args:
            player (Player): The player.
        '''
        self.current_player = player
    
    def set_selected_piece(self, piece):
        '''
        Set the selected piece.
        
        Args:
            piece (Piece): The piece.
        '''
        self.selected_piece = piece

    def set_game_result(self, game_result):
        '''
        Set the game result.
        
        Args:
            game_result (str): The game result.
        '''
        self.game_result = game_result
        
    def get_player(self, side):
        '''
        Get the player by the given side.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            Player: The player.
        '''
        return self.players[side]

    def switch_player(self):
        '''
        Switch the current player.
        '''
        self.current_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.LIGHT] or self.players[PlayerSide.DARK]
        self.opponent_player = self.current_player == self.players[PlayerSide.DARK] and self.players[PlayerSide.LIGHT] or self.players[PlayerSide.DARK]
        if self.current_player.side == PlayerSide.DARK:
            self.computer_move()
    
    def handle_piece_selection(self, mouse_position):
        '''
        Handle the piece selection.
        
        Args:
            mouse_position (tuple): The position of the mouse.
        '''
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece and cell.piece.side == self.current_player.side:
            self.selected_piece = cell.piece

    def handle_piece_move(self, mouse_position):
        '''
        Handle the piece move.
        
        Args:
            mouse_position (tuple): The position of the mouse.
            
        Returns:
            bool: True if the piece is moved, False otherwise.
        '''
        if not self.selected_piece:
            return False
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if target_cell in self.selected_piece.available_moves(self.board):
            # self.current_player.remove_piece(self.selected_piece)
            source_cell.remove_piece()
            if target_cell.piece:
                self.opponent_player.remove_piece(target_cell.piece)
                target_cell.remove_piece()
            # self.current_player.add_piece(self.selected_piece)
            target_cell.add_piece(self.selected_piece)
            self.selected_piece = None
            if self.check_game_end(target_cell):
                return True
            self.switch_player()
            return True
        return False

    def computer_move(self):
        if self.current_player.side == PlayerSide.DARK:
            dark_pieces = [cell.piece for row in self.board.cells for cell in row if cell.piece and cell.piece.side == PlayerSide.DARK]
            selected_piece = random.choice(dark_pieces)
            available_moves = selected_piece.available_moves(self.board)
            if available_moves:
                source_cell = self.board.get_cell(selected_piece.position)
                target_cell = random.choice(available_moves)
                # self.current_player.remove_piece(selected_piece)
                source_cell.remove_piece()
                if target_cell.piece:
                    self.opponent_player.remove_piece(target_cell.piece)
                    target_cell.remove_piece()
                # self.current_player.add_piece(selected_piece)
                target_cell.add_piece(selected_piece)
                if self.check_game_end(target_cell):
                    return
                self.switch_player()

    def check_game_end(self, destination_cell):
        '''
        Check if the game is ended.
        
        Args:
            destination_cell (Cell): The destination cell.
        
        Returns:
            bool: True if the game is ended, False otherwise.
        '''
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
