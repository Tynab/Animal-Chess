import random
from scripts.board import Board
from scripts.bot import Bot
from scripts.common import GameState, PlayerSide, GameMode
from scripts.log import Log

class GameManager:
    '''
    Game manager class.

    Attributes:
    - log (Log): The log.
    - board (Board): The board.
    - game_state (GameState): The game state.
    - game_mode (GameMode): The game mode.
    - game_result (str): The game result.
    - current_side (PlayerSide): The current side.
    - opponent_side (PlayerSide): The opponent side.
    - selected_piece (Piece): The selected piece.

    Methods:
    - __init__: Initialize the game manager.
    - reset_game: Reset the game.
    - switch_player: Switch the player.
    - handle_piece_selection: Handle the piece selection.
    - handle_piece_move: Handle the piece move.
    - computer_move: Make the computer move.
    - is_game_end: Check if the game ends.
    '''

    def __init__(self, game_mode=GameMode.PvC):
        '''
        Initialize the game manager.

        Args:
            game_mode (GameMode): The game mode.

        Returns:
            GameManager: A new GameManager instance.
        '''
        self.log = Log()
        self.board = Board()
        self.game_state = GameState.NEW
        self.game_mode = game_mode
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
            move = (source_cell.position, target_cell.position)
            self.board.make_move(move)
            self.selected_piece = None

            # Log the move
            self.log.insert_chess_record(self.board, move)

            # Check if the game ends
            if self.is_game_end:
                self.log.save()
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
        # Use minimax algorithm with alpha-beta pruning to find the best moves
        choosen_moves = random.choice([1, 2, 3])
        _, best_moves = Bot.minimax(self.board.copy(), self.current_side, 2, True) if choosen_moves == 1 else (Bot.minimax_alpha_beta_pruning(self.board.copy(), self.current_side, 2, float('-inf'), float('inf'), True) if choosen_moves == 2 else (None, self.board.get_valid_moves(self.current_side)))

        # Initialize variables for finding the move with the shortest path
        min_path = float('inf')
        moves = []

        # Iterate over the pieces of the current side
        for piece in self.board.pieces_of[self.current_side]:
            # Find all possible paths for the piece
            paths = Bot.breadth_first_search(self.board, piece, piece.position, piece.weaker_pieces_positions(self.board))
            
            # Check if there are valid paths
            if paths and paths[0] and paths[0][0]:
                # Get the length of the first path
                path_length = paths[0][0][0]
                
                # Filter the valid moves based on the best moves
                valid_moves = [move for move in [tuple(path[1][:2]) for path in paths[0]] if move in best_moves]
                
                # Continue to the next piece if there are no valid moves
                if not valid_moves:
                    continue
                
                # Update the move with the shortest path
                if path_length < min_path:
                    min_path = path_length
                    moves = valid_moves
                elif path_length == min_path:
                    moves.extend(valid_moves)
        
        # Get the best move
        best_move = random.choice([1, 2]) == 1 and moves and random.choice(moves) or random.choice(best_moves)

        # Make the move
        self.board.make_move(best_move)

        # Log the move
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
        # Check if the opponent has no pieces or if the opponent's den is invaded
        if self.board.is_game_over:
            # Set the game state to OVER
            self.game_state = GameState.OVER

            # Set the game result to the current side's win
            self.game_result = f'{self.board.winner.upper()}\nWIN!!!'

            # Return True to indicate that the game ends
            return True
        
        # Return False to indicate that the game continues
        return False
