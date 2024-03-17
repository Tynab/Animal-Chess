import os
import pandas
from scripts.common import Utils

class Log:

    def __init__(self):
        self.chess_df = pandas.DataFrame(columns=['board', 'move', 'winner'])
        self.position_df = pandas.DataFrame(columns=['position', 'piece', 'den', 'trap', 'river'])
        self.piece_df = pandas.DataFrame(columns=['piece', 'atk'])

    def insert_chess_record(self, board, move):
        self.chess_df = self.chess_df.append({'board': Utils.board_to_enum(board), 'move': Utils.move_to_enum(move), 'winner': Utils.winner_to_enum(board.winner)}, ignore_index=True)

    def insert_position_record(self, cell):
        self.position_df = self.position_df.append({'position': Utils.position_to_enum(cell.position), 'piece': Utils.cell_piece_to_enum(cell), 'den': Utils.cell_den_to_enum(cell), 'trap': Utils.cell_trap_to_enum(cell), 'river': Utils.cell_river_to_enum(cell)}, ignore_index=True)

    def insert_piece_record(self, piece):
        self.piece_df = self.piece_df.append({'piece': Utils.map_piece_name(piece), 'atk': piece.atk}, ignore_index=True)

    def save(self):
        self.chess_df.to_csv('chess.csv', mode='a', header=not os.path.isfile('chess.csv'), index=False)
        self.position_df.to_csv('position.csv', mode='a', header=not os.path.isfile('position.csv'), index=False)
        self.piece_df.to_csv('piece.csv', mode='a', header=not os.path.isfile('piece.csv'), index=False)
