import scripts.common as common
from pygame import transform, image
from scripts.common import Size, CellLabel, PieceAtk
from scripts.pieces.rat import Rat
from scripts.pieces.cat import Cat
from scripts.pieces.dog import Dog
from scripts.pieces.wolf import Wolf
from scripts.pieces.leopard import Leopard
from scripts.pieces.tiger import Tiger
from scripts.pieces.lion import Lion
from scripts.pieces.elephant import Elephant

class Cell:

    def __init__(self, label, position):
        self.label = label
        self.position = position
        self.image = None
        self.piece = None

    def copy(self):
        cell = Cell(self.label, self.position)
        cell.image = self.image
        if self.piece:
            cell.add_piece(self.piece.copy())
        return cell

    def set_image(self, image_path):
        self.image = transform.scale(image.load(image_path), Size.CELL)

    def add_piece(self, piece):
        piece_atk_map = {
            Rat: PieceAtk.RAT,
            Cat: PieceAtk.CAT,
            Dog: PieceAtk.DOG,
            Wolf: PieceAtk.WOLF,
            Leopard: PieceAtk.LEOPARD,
            Tiger: PieceAtk.TIGER,
            Lion: PieceAtk.LION,
            Elephant: PieceAtk.ELEPHANT,
        }
        self.piece = piece
        self.piece.position = self.position
        self.piece.atk = CellLabel.is_opponent_trap(self.label, piece.side) and float('-inf') or piece_atk_map[type(self.piece)]

    def remove_piece(self):
        self.piece = None

    def is_occupied_own(self, side):
        return self.piece and self.piece.side == side

    @property
    def is_in_board(self):
        return 0 <= self.position[0] < common.W and 0 <= self.position[1] < common.H

    @property
    def is_river(self):
        return CellLabel.is_river(self.label)
