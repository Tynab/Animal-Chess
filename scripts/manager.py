import random
from scripts.board import Board
from scripts.bot import Bot
from scripts.common import GameState, PlayerSide, GameMode

class GameManager:
    '''
    Game manager class.

    Attributes:
    - board (Board): The board.
    - game_state (GameState): The game state.
    - game_mode (GameMode): The game mode.
    - game_result (str): The game result.
    - current_side (PlayerSide): The current side.
    - opponent_side (PlayerSide): The opponent side.
    - selected_piece (Piece): The selected piece.
    '''

    def __init__(self):
        '''
        Initialize the game manager.
        '''
        self.board = Board()
        self.game_state = GameState.NEW
        self.game_mode = GameMode.PvC
        self.game_result = None
        self.current_side = PlayerSide.LIGHT
        self.opponent_side = PlayerSide.opponent_of(self.current_side)
        self.selected_piece = None

    def reset_game(self):
        '''
        Reset the game.
        '''
        self.board = Board()
        self.game_state = GameState.RUNNING

    def switch_player(self):
        '''
        Switch the player.
        '''
        self.current_side, self.opponent_side = self.opponent_side, self.current_side
        self.board.captured_pieces.clear()
        print('\a')
    
    def handle_piece_selection(self, mouse_position):
        '''
        Handle the piece selection.
        
        Args:
            mouse_position (tuple): The mouse position.
        '''
        # Get the cell at the mouse position
        cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
        
        # Check if the cell has a piece and if it belongs to the current player
        if cell.piece and cell.piece.side == self.current_side:
            self.selected_piece = cell.piece

    def handle_piece_move(self, mouse_position):
        '''
        Handle the piece move.
        
        Args:
            mouse_position (tuple): The mouse position.
            
        Returns:
            bool: True if the move is valid, False otherwise.
        '''
        # Check if a piece is selected
        if not self.selected_piece:
            return False
        
        # Get the source and target cells
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))

        # Check if the target cell is in the available cells of the selected piece
        if target_cell in self.selected_piece.available_cells(self.board):
            # Make the move
            self.board.make_move((source_cell.position, target_cell.position))
            self.selected_piece = None

            # Check if the game ends
            if self.check_game_end():
                return True
            
            # Switch the player
            self.switch_player()

            # Check if the game mode is PvC
            return True
        
        # Check if the target cell is occupied by the opponent's piece
        return False
    
    def computer_move(self):
        '''
        Make the computer move.
        '''
        # Get the best move
        best_move = Bot.mcts_move(self.board, self.current_side)

        # Make the move
        self.board.make_move(best_move)

        # Check if the game ends
        if self.board.is_game_over:
            self.game_state = GameState.OVER
        else:
            self.switch_player()

    def check_game_end(self):
        '''
        Check if the game ends.
        
        Returns:
            bool: True if the game ends, False otherwise.
        '''
        # Check if the opponent has no pieces or if the opponent's den is invaded
        if self.board.is_opponent_pieceless(self.current_side) or self.board.is_opponent_den_invaded(self.current_side):
            # Set the game state to OVER
            self.game_state = GameState.OVER

            # Set the game result to the current side's win
            self.game_result = f'{self.current_side.upper()}\nWIN!!!'

            # Return True to indicate that the game ends
            return True
        
        # Return False to indicate that the game continues
        return False
