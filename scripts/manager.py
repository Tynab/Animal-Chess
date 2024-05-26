import numpy
import random
from scripts.board import *
from scripts.bot import *
from scripts.common import *
from scripts.log import *
from tensorflow.keras import models

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
    - autoplay(self): Make the computer move.
    - computer_move(self): Make the computer move.
    - breadth_first_search_moves(self, best_moves): Get the moves using the breadth-first search algorithm.
    - a_star_search_moves(self, best_moves): Get the moves using the A* search algorithm.
    - ai_move(self): Make the computer move using the AI model.
    - is_game_end(self): Check if the game ends.
    - encode_piece(piece_char): Encode the piece.
    - encode_board(board_str): Encode the board.
    - algorithm_random(opponent_pieces): Get the random algorithm.
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
    
    def autoplay(self):
        '''
        Make the computer move.
        '''
        # Get the best move
        best_move = self.computer_move()
        # best_move = self.ai_move()
        self.board.make_move(best_move)
        self.log.insert_chess_record(self.board, best_move)

        # Check if the game ends
        if self.is_game_end:
            self.log.save()
            return

        # Switch the player
        self.switch_player()

    def computer_move(self):
        '''
        Make the computer move using the minimax algorithm.
        
        Returns:
            tuple: The best move.
        '''
        # Get the best moves
        new_board = self.board.copy()
        _, best_moves = random.choice([1, 2]) == 1 and Bot.minimax(new_board, self.current_side, 2, True) or Bot.minimax_alpha_beta_pruning(new_board, self.current_side, 2, float('-inf'), float('inf'), True)

        # Check if the best moves exist
        if not best_moves:
            best_moves = self.board.get_valid_moves(self.current_side)

        # Return the best move
        return random.choice(GameManager.algorithm_random(len(self.board.pieces_of[self.opponent_side])) == 1 and self.breadth_first_search_moves(best_moves) or self.a_star_search_moves(best_moves) + best_moves)
    
    def breadth_first_search_moves(self, best_moves):
        '''
        Get the moves using the breadth-first search algorithm.
        
        Args:
            best_moves (list): The best moves.
        
        Returns:
            list: The moves.
        '''
        # Declare the minimum path and the moves
        min_path = float('inf')
        moves = []

        # Iterate through the pieces
        for piece in self.board.pieces_of[self.current_side]:
            # Get the valid paths
            ends = piece.weaker_pieces_positions(self.board)
            paths = Bot.breadth_first_search(self.board, piece, piece.position, ends)
            
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
        
        # Return the moves
        return moves
    
    def a_star_search_moves(self, best_moves):
        '''
        Get the moves using the A* search algorithm.
        
        Args:
            best_moves (list): The best moves.
        
        Returns:
            list: The moves.
        '''
        # Declare the minimum path and the moves
        min_path = float('inf')
        moves = []

        # Iterate through the pieces
        for piece in self.board.pieces_of[self.current_side]:
            # Get the valid paths
            ends = piece.weaker_pieces_positions(self.board)
            paths = Bot.a_star_search(self.board, piece, piece.position, ends)
            
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
        
        # Return the moves
        return moves

    def ai_move(self):
        '''
        Make the computer move using the AI model.
        
        Returns:
            tuple: The best move.
        '''
        # Load the best model
        model = models.load_model('best_model.h5')

        # Initialize the best move and the best score
        best_move = None
        best_score = float('-inf')

        # Iterate through the valid moves
        for move in self.board.get_valid_moves(self.current_side):
            # Copy the board
            new_board = self.board.copy()

            # Make the move
            new_board.make_move(move)

            # Encode the board
            board_encoded = GameManager.encode_board(Log.board_to_enum(new_board))
            board_encoded_reshaped = board_encoded.reshape(1, *board_encoded.shape)

            # Get the predicted score
            predicted_score = model.predict(board_encoded_reshaped)

            # Update the best move and the best score
            if predicted_score > best_score:
                best_score = predicted_score
                best_move = move

        # Return the best move
        return best_move

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
    
    @staticmethod
    def encode_piece(piece_char):
        '''
        Encode the piece.
        
        Args:
            piece_char (str): The piece character.
            
        Returns:
            int: The piece encoding.
        '''
        # Define the piece mapping
        piece_mapping = {'-': 0, 'r': 1, 'c': 2, 'd': 3, 'w': 4, 'p': 5, 't': 6, 'l': 7, 'e': 8, 'R': -1, 'C': -2, 'D': -3, 'W': -4, 'P': -5, 'T': -6, 'L': -7, 'E': -8}

        # Return the piece encoding
        return piece_mapping.get(piece_char, 0)
    
    @staticmethod
    def encode_board(board_str):
        '''
        Encode the board.
        
        Args:
            board_str (str): The board string.
        
        Returns:
            numpy.ndarray: The board matrix.
        '''
        # Initialize the board matrix
        board_matrix = numpy.zeros((9, 7))

        # Iterate through the board string
        for i, piece in enumerate(board_str[::-1]):
            row, col = divmod(i, 9)
            board_matrix[col][row] = GameManager.encode_piece(piece)

        # Return the board matrix
        return numpy.flip(numpy.flip(board_matrix, 0), 1)

    @staticmethod
    def algorithm_random(opponent_pieces):
        '''
        Get the random algorithm.
        
        Args:
            opponent_pieces (int): The number of opponent pieces.
        
        Returns:
            int: The algorithm.
        '''
        return random.choice([1] * (8 + opponent_pieces * 2) + [2] * (24 - opponent_pieces * 2))
