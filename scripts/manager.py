import random
from scripts.board import *
from scripts.bot import *
from scripts.common import *
from scripts.log import Log

class GameManager:
    '''
    The game manager.
    
    Attributes:
    - board (Board): The board.
    - game_state (GameState): The game state.
    - game_mode (GameMode): The game mode.
    - game_result (str): The game result.
    - current_side (PlayerSide): The current side.
    - opponent_side (PlayerSide): The opponent side.
    - selected_piece (Piece): The selected piece.
    - focused_piece (Piece): The focused piece.
    
    Methods:
    - reset_game(self): Reset the game.
    - switch_player(self): Switch the player.
    - handle_piece_focus(self, mouse_position): Handle the piece focus.
    - handle_piece_selection(self, mouse_position): Handle the piece selection.
    - handle_piece_move(self, mouse_position): Handle the piece move.
    - computer_move(self): Make the computer move.
    - is_game_end(self): Check if the game ends.
    '''

    def __init__(self, game_mode=GameMode.PvC):
        '''
        Initialize the game manager.
        
        Args:
            game_mode (GameMode): The game mode.
        
        Returns:
            GameManager: The game manager.
        '''
        self.log = Log()
        self.board = Board()
        self.game_state = GameState.NEW
        self.game_mode = game_mode
        self.game_result = None
        self.current_side = PlayerSide.LIGHT
        self.opponent_side = PlayerSide.opponent_of(self.current_side)
        self.selected_piece = None
        self.focused_piece = None

    def reset_game(self):
        '''
        Reset the game.
        '''
        self.board = Board()
        self.game_state = GameState.RUNNING
        self.game_result = None
        self.selected_piece = None

    def switch_player(self):
        '''
        Switch the player.
        '''
        self.current_side, self.opponent_side = self.opponent_side, self.current_side
        self.board.captured_pieces.clear()
        print('\a')

    def handle_piece_focus(self, mouse_position):
        '''
        Handle the piece focus.
        
        Args:
            mouse_position (tuple): The mouse position.
        '''
        if mouse_position[0] < Size.BOARD[0] and mouse_position[1] < Size.BOARD[1]:
            # Get the cell at the mouse position
            cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
            
            # Check if the cell has a piece
            if cell.piece:
                self.focused_piece = cell.piece
    
    def handle_piece_selection(self, mouse_position):
        '''
        Handle the piece selection.
        
        Args:
            mouse_position (tuple): The mouse position.
        '''
        if mouse_position[0] < Size.BOARD[0] and mouse_position[1] < Size.BOARD[1]:
            # Get the cell at the mouse position
            cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))
            
            # Check if the cell has a piece
            if cell.piece and cell.piece.side == self.current_side:
                self.selected_piece = cell.piece

    def handle_piece_move(self, mouse_position):
        '''
        Handle the piece move.
        
        Args:
            mouse_position (tuple): The mouse position.
        
        Returns:
            bool: True if the game ends, False otherwise.
        '''
        # Check if the selected piece exists
        if not self.selected_piece:
            return False
        
        # Get the source and target cells
        source_cell = self.board.get_cell(self.selected_piece.position)
        target_cell = self.board.get_cell((mouse_position[0] // 100, mouse_position[1] // 100))

        # Check if the target cell is occupied by the player's own piece
        if target_cell in self.selected_piece.available_cells(self.board):
            # Make the move
            move = (source_cell.position, target_cell.position)
            self.board.make_move(move)
            self.selected_piece = None
            self.log.insert_chess_record(self.board, move)

            # Check if the game ends
            if self.is_game_end:
                self.log.save()
                return True
            
            # Switch the player
            self.switch_player()

            # Check if the game mode is PvC
            return True
        
        # Check if the target cell is occupied by the player's own piece
        return False
    
    def computer_move(self):
        '''
        Make the computer move.
        '''
        # Get the best moves
        choosen_moves = random.choice([1, 2, 3])
        _, best_moves = Bot.minimax(self.board.copy(), self.current_side, 2, True) if choosen_moves == 1 else (Bot.minimax_alpha_beta_pruning(self.board.copy(), self.current_side, 2, float('-inf'), float('inf'), True) if choosen_moves == 2 else (None, self.board.get_valid_moves(self.current_side)))
        min_path = float('inf')
        moves = []

        # Iterate through the pieces
        for piece in self.board.pieces_of[self.current_side]:
            # Get the valid paths
            paths = Bot.breadth_first_search(self.board, piece, piece.position, piece.weaker_pieces_positions(self.board))
            
            # Check if the paths exist
            if paths and paths[0] and paths[0][0]:
                # Get the path length and the valid moves
                path_length = paths[0][0][0]
                valid_moves = [move for move in [tuple(path[1][:2]) for path in paths[0]] if move in best_moves]
                
                # Check if the valid moves exist
                if not valid_moves:
                    continue
                
                # Update the minimum path and the moves
                if path_length < min_path:
                    min_path = path_length
                    moves = valid_moves
                elif path_length == min_path:
                    moves.extend(valid_moves)
        
        # Get the best move
        best_move = random.choice([1, 2]) == 1 and moves and random.choice(moves) or random.choice(best_moves)
        self.board.make_move(best_move)
        self.log.insert_chess_record(self.board, best_move)

        # Check if the game ends
        if self.is_game_end:
            self.log.save()
            return

        # Switch the player
        self.switch_player()

    @property
    def is_game_end(self):
        '''
        Check if the game ends.
        
        Returns:
            bool: True if the game ends, False otherwise.
        '''
        # Check if the game is over
        if self.board.is_game_over:
            # Update the game state and the game result
            self.game_state = GameState.OVER
            self.game_result = f'{self.board.winner.upper()}\nWIN!!!'

            # Return True to indicate that the game ends
            return True
        
        # Check if the move is forbidden
        return False
