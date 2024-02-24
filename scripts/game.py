from board import Board
from cell import CellPosition
from enum import Enum, auto
from player import Player, PlayerSide

class GameConstant(Enum):
    '''
    The constant of the game.
    
    Attributes:
        WIDTH (int): The width of the game.
        HEIGHT (int): The height of the game.
        FPS (int): The frame per second of the game.
        TITLE (str): The title of the game.
        SPAN (int): The span of the game.
        SIZE (tuple): The size of the game.
        CELL_SIZE (tuple): The size of the cell.
        ARTWORK_SIZE (tuple): The size of the artwork.
        START_BTN_SIZE (tuple): The size of the start button.
    '''
    WIDTH = 7
    HEIGHT = 9
    FPS = 60
    TITLE = 'Animal Chess'
    SPAN = 100
    SIZE = (WIDTH * SPAN, HEIGHT * SPAN)
    CELL_SIZE = (SPAN, SPAN)
    ARTWORK_SIZE = (500, 500)
    START_BTN_SIZE = (190, 50)

class GameStatus(Enum):
    '''
    The status of the game.
    
    Attributes:
        NEW (auto): The game is new.
        RUNNING (auto): The game is running.
        OVER (auto): The game is over.
    '''
    NEW = auto
    RUNNING = auto
    OVER = auto

class GameManager:
    '''
    The game manager.
    '''
    def __init__(self):
        self.game_status = GameStatus.NEW
        self.board = Board()
        self.players = {
            PlayerSide.DARK: Player(PlayerSide.DARK),
            PlayerSide.LIGHT: Player(PlayerSide.LIGHT)
        }
        self.current_player = self.players[PlayerSide.LIGHT]
        self.selected_piece = None
        self.game_result = None

    def switch_player(self):
        '''
        Switch the current player.
        '''
        self.current_player = self.players[PlayerSide.DARK] and self.current_player == self.players[PlayerSide.LIGHT] or self.players[PlayerSide.LIGHT]
    
    def handle_piece_selection(self, mouse_position):
        '''
        Handle the piece selection.
        
        Args:
            mouse_position (tuple): The position of the mouse.
        '''
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        if cell.piece is not None:
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
            source_cell.remove_piece()
            target_cell.add_piece(self.selected_piece)
            self.selected_piece = None
            if self.check_game_end(target_cell):
                return True
            self.switch_player()
            return True
        return False

    def check_game_end(self, destination_cell):
        '''
        Check if the game is ended.
        
        Args:
            destination_cell (Cell): The destination cell.
        
        Returns:
            bool: True if the game is ended, False otherwise.
        '''
        if destination_cell.position == CellPosition.DARK_DEN.value and self.current_player.side == PlayerSide.LIGHT:
            self.game_status = GameStatus.OVER
            self.game_result = 'LIGHT\nWIN!!!'
            return True
        if destination_cell.position == CellPosition.LIGHT_DEN.value and self.current_player.side == PlayerSide.DARK:
            self.game_status = GameStatus.OVER
            self.game_result = 'DARK\nWIN!!!'
            return True
        if self.players[self.current_player.side == PlayerSide.LIGHT and PlayerSide.DARK or PlayerSide.LIGHT].pieces.count() == 0:
            self.game_status = GameStatus.OVER
            self.game_result = f'{self.current_player.side.value.upper()}\nWIN!!!'
            return True
        return False
