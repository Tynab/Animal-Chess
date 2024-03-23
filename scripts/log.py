import os
import pandas
import uuid
from pandas import DataFrame
from scripts.bot import Bot
from scripts.common import PlayerSide

class Log:
    '''
    Log class.
    
    Attributes:
    - df: The data frame.
    
    Methods:
    - __init__: Initialize the log.
    - insert_chess_record: Insert the chess record.
    - save: Save the chess record to a CSV file.
    - is_move_forbidden: Check if the move is forbidden.
    - map_piece_name: Map the piece name.
    - side_to_enum: Convert the side to enum.
    - enum_to_side: Convert the enum to side.
    - position_to_enum: Convert the position to enum.
    - enum_to_postion: Convert the enum to position.
    - move_to_enum: Convert the move to enum.
    - enum_to_move: Convert the enum to move.
    - cell_piece_to_enum: Convert the cell piece to enum.
    - cell_trap_to_enum: Convert the cell trap to enum.
    - cell_den_to_enum: Convert the cell den to enum.
    - cell_river_to_enum: Convert the cell river to enum.
    - board_to_enum: Convert the board to enum.
    '''

    def __init__(self):
        '''
        Initialize the log.

        Returns:
            Log: A new Log instance.
        '''
        self.new_df()

    def new_df(self):
        '''
        Create a new data frame.
        '''
        self.id = str(uuid.uuid4())
        self.df = DataFrame(columns=['Id', 'board', 'side', 'piece', 'atk', 'move', 'position', 'river', 'trap', 'den', 'score', 'winner'])

    def insert_chess_record(self, board, move):
        '''
        Insert the chess record.
        
        Args:
            board (Board): The board.
            move (tuple): The move.
        '''
        cell = board.get_cell(move[1])
        self.df = pandas.concat([self.df, DataFrame([{
            'Id': self.id,
            'board': Log.board_to_enum(board),
            'side': Log.side_to_enum(cell.piece.side),
            'piece': Log.cell_piece_to_enum(cell),
            'atk': cell.piece.atk,
            'move': Log.move_to_enum(move),
            'position': Log.position_to_enum(cell.position),
            'river': Log.cell_river_to_enum(cell),
            'trap': Log.cell_trap_to_enum(cell),
            'den': Log.cell_den_to_enum(cell),
            'score': Bot.evaluate_position(board, PlayerSide.DARK),
            'winner': Log.side_to_enum(board.winner)
        }])], ignore_index=True)
        forbidden_move = self.move_forbidden()
        board.forbidden_move = forbidden_move and Log.enum_to_move(forbidden_move) or None

    def save(self):
        '''
        Save the chess record to a CSV file.
        '''
        self.df.to_csv('animal_chess.csv', mode='a', header=not os.path.isfile('animal_chess.csv'), index=False)
        self.new_df()

    def move_forbidden(self):
        '''
        Check if the move is forbidden.
        
        Returns:
            str: The forbidden move.
        '''
        # Get the last 10 moves
        moves = self.df['move'][-4:-13:-4]

        # Check if the moves are the same
        return moves.iloc[0] if moves.nunique() == 1 and len(moves) == 3 else None

    @staticmethod
    def map_piece_name(piece):
        '''
        Map the piece name.
        
        Args:
            piece (Piece): The piece.
        
        Returns:
            str: The symbol.
        '''
        # Map the piece name to symbol
        symbol = {
            'rat': 'r',
            'cat': 'c',
            'dog': 'd',
            'wolf': 'w',
            'leopard': 'p',
            'tiger': 't',
            'lion': 'l',
            'elephant': 'e',
        }.get(piece.__class__.__name__.lower(), '-')
        
        # Return the symbol
        return piece.is_dark and symbol or symbol.upper()

    @staticmethod
    def side_to_enum(side):
        '''
        Convert the side to enum.

        Args:
            side (PlayerSide): The side.
        
        Returns:
            int: The enum.
        '''
        return 0 if not side else 1 if PlayerSide.is_dark(side) else -1
    
    @staticmethod
    def enum_to_side(enum):
        '''
        Convert the enum to side.

        Args:
            enum (int): The enum.
        
        Returns:
            PlayerSide: The side.
        '''
        return PlayerSide.DARK if enum == 1 else PlayerSide.LIGHT if enum == -1 else None
    
    @staticmethod
    def position_to_enum(position):
        '''
        Convert the position to enum.
        
        Args:
            position (tuple): The position.
            
        Returns:
            str: The enum.
        '''
        return f"{chr(ord('A') + position[0])}{position[1] + 1}"
    
    @staticmethod
    def enum_to_postion(enum):
        '''
        Convert the enum to position.
        
        Args:
            enum (str): The enum.
            
        Returns:
            tuple: The position.
        '''
        return (ord(enum[0]) - ord('A'), int(enum[1]) - 1)
    
    @staticmethod
    def move_to_enum(move):
        '''
        Convert the move to enum.
        
        Args:
            move (tuple): The move.
        
        Returns:
            str: The enum.
        '''
        return f"{chr(ord('A') + move[0][0])}{move[0][1] + 1}{chr(ord('A') + move[1][0])}{move[1][1] + 1}"
    
    @staticmethod
    def enum_to_move(enum):
        '''
        Convert the enum to move.
        
        Args:
            enum (str): The enum.
        
        Returns:
            tuple: The move.
        '''
        return ((ord(enum[0]) - ord('A'), int(enum[1]) - 1), (ord(enum[2]) - ord('A'), int(enum[3]) - 1))
    
    @staticmethod
    def cell_piece_to_enum(cell):
        '''
        Convert the cell piece to enum.
        
        Args:
            cell (Cell): The cell.
        
        Returns:
            str: The enum.
        '''
        return cell.piece and Log.map_piece_name(cell.piece) or '-'
    
    @staticmethod
    def cell_trap_to_enum(cell):
        '''
        Convert the cell trap to enum.
        
        Args:
            cell (Cell): The cell.
            
        Returns:
            int: The enum.
        '''
        return -1 if cell.is_light_trap else 1 if cell.is_dark_trap else 0
    
    @staticmethod
    def cell_den_to_enum(cell):
        '''
        Convert the cell den to enum.
        
        Args:
            cell (Cell): The cell.
            
        Returns:
            int: The enum.
        '''
        return -1 if cell.is_light_den else 1 if cell.is_dark_den else 0
    
    @staticmethod
    def cell_river_to_enum(cell):
        '''
        Convert the cell river to enum.
        
        Args:
            cell (Cell): The cell.
            
        Returns:
            int: The enum.
        '''
        return 1 if cell.is_river else 0
    
    @staticmethod
    def board_to_enum(board):
        '''
        Convert the board to enum.
        
        Args:
            board (Board): The board.
            
        Returns:
            str: The enum.
        '''
        return ''.join(Log.cell_piece_to_enum(cell) for row in board.cells for cell in row)
