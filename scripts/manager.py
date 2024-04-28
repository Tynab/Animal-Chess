import random
from scripts.board import *
from scripts.bot import *
from scripts.common import *
from scripts.log import Log

from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

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
        self.ohe = OneHotEncoder()
        self.scaler = MinMaxScaler()

        # Giả sử 'trap' và 'den' nhận các giá trị từ -1, 0, đến 1
        example_data = np.array([
            [0, 0],  # Không phải bẫy hoặc hang
            [1, 0],  # Bẫy cho đối phương
            [-1, 0], # Bẫy cho bên mình
            [0, 1],  # Hang đối phương
            [0, -1]  # Hang bên mình
        ])
        self.ohe.fit(example_data)

        # Huấn luyện MinMaxScaler với giá trị 'atk' giả định từ -8 đến 8
        example_atk = np.array([[i] for i in range(-8, 9)])
        self.scaler.fit(example_atk)

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
        # best_move = random.choice([1, 2]) == 1 and moves and random.choice(moves) or random.choice(best_moves)
        # best_move = self.computer_move_v2()
        best_move = self.computer_move_v3()
        self.board.make_move(best_move)
        self.log.insert_chess_record(self.board, best_move)

        # Check if the game ends
        if self.is_game_end:
            self.log.save()
            return

        # Switch the player
        self.switch_player()

    def computer_move_v2(self):
        model = load_model('my_chess_model.h5')

        # Mã hóa trạng thái bàn cờ hiện tại
        board_encoded = GameManager.encode_board(Log.board_to_enum(self.board))
        board_encoded_flattened = board_encoded.flatten().reshape(1, -1)


        # Giả sử chúng ta đã có sẵn danh sách các nước đi hợp lệ
        possible_moves = self.board.get_valid_moves(self.current_side)
        best_move = None
        best_score = float('-inf')
        
        # Duyệt qua từng nước đi và dự đoán điểm số cho mỗi nước đi
        for move in possible_moves:
            move_encoded = GameManager.encode_move(Log.move_to_enum(move))
            move_encoded_flattened = np.array(move_encoded).reshape(1, -1)
            
            # Mã hóa các thuộc tính khác
            cell = self.board.get_cell(move[0])
            categorical_features = self.ohe.transform([[GameManager.encode_trap(cell), GameManager.encode_den(cell)]]).toarray()
            atk_encoded = np.array([GameManager.encode_piece(Log.map_piece_name(cell.piece))]).reshape(1, -1)
            numeric_features = self.scaler.transform(atk_encoded)

            input_features = np.concatenate([board_encoded_flattened, move_encoded_flattened, categorical_features, numeric_features], axis=1)
            
            # Dự đoán điểm số cho nước đi này
            predicted_score = model.predict(input_features)
            
            # Chọn nước đi với điểm số cao nhất
            if predicted_score > best_score:
                best_score = predicted_score
                best_move = move
        
        return best_move
    
    def computer_move_v3(self):
        model = load_model('best_model.h5')

        possible_moves = self.board.get_valid_moves(self.current_side)
        best_move = None
        best_score = float('-inf')

        # Duyệt qua từng nước đi và dự đoán điểm số cho mỗi nước đi
        for move in possible_moves:
            new_board = self.board.copy()

            # Thực hiện nước đi
            new_board.make_move(move)

            # Mã hóa trạng thái bàn cờ hiện tại
            board_encoded = GameManager.encode_board(Log.board_to_enum(new_board))
            board_encoded_reshaped = board_encoded.reshape(1, *board_encoded.shape)  # Đảm bảo kích thước phù hợp với mô hình

            # Dự đoán điểm số cho nước đi này
            predicted_score = model.predict(board_encoded_reshaped)

            # Chọn nước đi với điểm số cao nhất
            if predicted_score > best_score:
                best_score = predicted_score
                best_move = move

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
        piece_mapping = {'-': 0, 'r': 1, 'c': 2, 'd': 3, 'w': 4, 'p': 5, 't': 6, 'l': 7, 'e': 8, 'R': -1, 'C': -2, 'D': -3, 'W': -4, 'P': -5, 'T': -6, 'L': -7, 'E': -8}
        return piece_mapping.get(piece_char, 0)
    
    @staticmethod
    def encode_board(board_str):
        board_matrix = np.zeros((9, 7))
        for i, piece in enumerate(board_str[::-1]):
            row, col = divmod(i, 9)
            board_matrix[col][row] = GameManager.encode_piece(piece)
        return np.flip(np.flip(board_matrix, 0), 1)
    
    @staticmethod
    def encode_move(move_str):
        col_from = ord(move_str[0]) - ord('A')
        row_from = int(move_str[1]) - 1
        col_to = ord(move_str[2]) - ord('A')
        row_to = int(move_str[3]) - 1
        return [row_from, col_from, row_to, col_to]
    
    @staticmethod
    def encode_trap(cell):
        return 1 if CellLabel.is_dark_trap(cell.label) else -1 if CellLabel.is_light_trap(cell.label) else 0
    
    @staticmethod
    def encode_den(cell):
        return 1 if CellLabel.is_dark_den(cell.label) else -1 if CellLabel.is_light_den(cell.label) else 0
