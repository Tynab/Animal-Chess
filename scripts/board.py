import scripts.cell as cell
import scripts.common as common
import scripts.pieces.rat as rat
import scripts.pieces.cat as cat
import scripts.pieces.dog as dog
import scripts.pieces.wolf as wolf
import scripts.pieces.leopard as leopard
import scripts.pieces.tiger as tiger
import scripts.pieces.lion as lion
import scripts.pieces.elephant as elephant
from scripts.common import *

class Board:
    '''
    Board class.
    
    Attributes:
    - cells (list): The cells of the board.
    - pieces (list): The pieces on the board.
    - pieces_of (dict): The pieces of each player.
    - captured_pieces (list): The captured pieces.
    - move_history (list): The move history.
    - forbidden_move (tuple): The forbidden move.
    
    Methods:
    - __init__: Constructor of the class.
    - copy: Return a copy of the board.
    - get_cell: Get the cell at the given position.
    - get_valid_moves: Get the valid moves for the given side.
    - get_forbidden: Get the forbidden move.
    - make_move: Make a move on the board.
    - undo_move: Undo a move on the board.
    - update_pieces: Update the pieces on the board.
    - is_opponent_pieceless: Check if the opponent has no pieces left.
    - is_opponent_den_invaded: Check if the opponent's den is invaded.
    - is_dark_win: Check if the dark side wins.
    - is_light_win: Check if the light side wins.
    - is_game_over: Check if the game is over.
    - winner: Get the winner of the game.
    '''
    
    def __init__(self, with_pieces=True, is_copy=False):
        '''
        Constructor of the class.
        
        Args:
            with_pieces (bool): True if the board should have pieces, False otherwise.
            is_copy (bool): True if the board is a copy, False otherwise.
            
        Returns:
            Board: A new Board instance.
        '''
        # Initialize the cells of the board
        self.cells = [[cell.Cell(CellLabel.EMPTY, (x, y)) for y in range(common.H)] for x in range(common.W)]
        
        # Set the labels for the river cells
        self.cells[CellPosition.RIVER_1_1[0]][CellPosition.RIVER_1_1[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_1_2[0]][CellPosition.RIVER_1_2[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_1_3[0]][CellPosition.RIVER_1_3[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_1_4[0]][CellPosition.RIVER_1_4[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_1_5[0]][CellPosition.RIVER_1_5[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_1_6[0]][CellPosition.RIVER_1_6[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_1[0]][CellPosition.RIVER_2_1[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_2[0]][CellPosition.RIVER_2_2[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_3[0]][CellPosition.RIVER_2_3[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_4[0]][CellPosition.RIVER_2_4[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_5[0]][CellPosition.RIVER_2_5[1]].label = CellLabel.RIVER
        self.cells[CellPosition.RIVER_2_6[0]][CellPosition.RIVER_2_6[1]].label = CellLabel.RIVER
        
        # Set the labels for the trap cells
        self.cells[CellPosition.DARK_TRAP_1[0]][CellPosition.DARK_TRAP_1[1]].label = CellLabel.DARK_TRAP
        self.cells[CellPosition.DARK_TRAP_2[0]][CellPosition.DARK_TRAP_2[1]].label = CellLabel.DARK_TRAP
        self.cells[CellPosition.DARK_TRAP_3[0]][CellPosition.DARK_TRAP_3[1]].label = CellLabel.DARK_TRAP
        self.cells[CellPosition.LIGHT_TRAP_1[0]][CellPosition.LIGHT_TRAP_1[1]].label = CellLabel.LIGHT_TRAP
        self.cells[CellPosition.LIGHT_TRAP_2[0]][CellPosition.LIGHT_TRAP_2[1]].label = CellLabel.LIGHT_TRAP
        self.cells[CellPosition.LIGHT_TRAP_3[0]][CellPosition.LIGHT_TRAP_3[1]].label = CellLabel.LIGHT_TRAP
        
        # Set the labels for the den cells
        self.cells[CellPosition.DARK_DEN[0]][CellPosition.DARK_DEN[1]].label = CellLabel.DARK_DEN
        self.cells[CellPosition.LIGHT_DEN[0]][CellPosition.LIGHT_DEN[1]].label = CellLabel.LIGHT_DEN
        
        # Set the images for the river cells
        if not is_copy:
            # Set the images for the river cells
            self.cells[CellPosition.RIVER_1_1[0]][CellPosition.RIVER_1_1[1]].set_image(CellImage.RIVER_1)
            self.cells[CellPosition.RIVER_1_2[0]][CellPosition.RIVER_1_2[1]].set_image(CellImage.RIVER_2)
            self.cells[CellPosition.RIVER_1_3[0]][CellPosition.RIVER_1_3[1]].set_image(CellImage.RIVER_3)
            self.cells[CellPosition.RIVER_1_4[0]][CellPosition.RIVER_1_4[1]].set_image(CellImage.RIVER_4)
            self.cells[CellPosition.RIVER_1_5[0]][CellPosition.RIVER_1_5[1]].set_image(CellImage.RIVER_5)
            self.cells[CellPosition.RIVER_1_6[0]][CellPosition.RIVER_1_6[1]].set_image(CellImage.RIVER_6)
            self.cells[CellPosition.RIVER_2_1[0]][CellPosition.RIVER_2_1[1]].set_image(CellImage.RIVER_1)
            self.cells[CellPosition.RIVER_2_2[0]][CellPosition.RIVER_2_2[1]].set_image(CellImage.RIVER_2)
            self.cells[CellPosition.RIVER_2_3[0]][CellPosition.RIVER_2_3[1]].set_image(CellImage.RIVER_3)
            self.cells[CellPosition.RIVER_2_4[0]][CellPosition.RIVER_2_4[1]].set_image(CellImage.RIVER_4)
            self.cells[CellPosition.RIVER_2_5[0]][CellPosition.RIVER_2_5[1]].set_image(CellImage.RIVER_5)
            self.cells[CellPosition.RIVER_2_6[0]][CellPosition.RIVER_2_6[1]].set_image(CellImage.RIVER_6)
            
            # Set the images for the trap cells
            self.cells[CellPosition.DARK_TRAP_1[0]][CellPosition.DARK_TRAP_1[1]].set_image(CellImage.TRAP)
            self.cells[CellPosition.DARK_TRAP_2[0]][CellPosition.DARK_TRAP_2[1]].set_image(CellImage.TRAP)
            self.cells[CellPosition.DARK_TRAP_3[0]][CellPosition.DARK_TRAP_3[1]].set_image(CellImage.TRAP)
            self.cells[CellPosition.LIGHT_TRAP_1[0]][CellPosition.LIGHT_TRAP_1[1]].set_image(CellImage.TRAP)
            self.cells[CellPosition.LIGHT_TRAP_2[0]][CellPosition.LIGHT_TRAP_2[1]].set_image(CellImage.TRAP)
            self.cells[CellPosition.LIGHT_TRAP_3[0]][CellPosition.LIGHT_TRAP_3[1]].set_image(CellImage.TRAP)
            
            # Set the images for the den cells
            self.cells[CellPosition.DARK_DEN[0]][CellPosition.DARK_DEN[1]].set_image(CellImage.DEN)
            self.cells[CellPosition.LIGHT_DEN[0]][CellPosition.LIGHT_DEN[1]].set_image(CellImage.DEN)
        
        # Add the pieces to the board
        if with_pieces:
            # Add the dark pieces to the board
            self.cells[CellPosition.DARK_RAT[0]][CellPosition.DARK_RAT[1]].add_piece(rat.Rat(PlayerSide.DARK))
            self.cells[CellPosition.DARK_CAT[0]][CellPosition.DARK_CAT[1]].add_piece(cat.Cat(PlayerSide.DARK))
            self.cells[CellPosition.DARK_DOG[0]][CellPosition.DARK_DOG[1]].add_piece(dog.Dog(PlayerSide.DARK))
            self.cells[CellPosition.DARK_WOLF[0]][CellPosition.DARK_WOLF[1]].add_piece(wolf.Wolf(PlayerSide.DARK))
            self.cells[CellPosition.DARK_LEOPARD[0]][CellPosition.DARK_LEOPARD[1]].add_piece(leopard.Leopard(PlayerSide.DARK))
            self.cells[CellPosition.DARK_TIGER[0]][CellPosition.DARK_TIGER[1]].add_piece(tiger.Tiger(PlayerSide.DARK))
            self.cells[CellPosition.DARK_LION[0]][CellPosition.DARK_LION[1]].add_piece(lion.Lion(PlayerSide.DARK))
            self.cells[CellPosition.DARK_ELEPHANT[0]][CellPosition.DARK_ELEPHANT[1]].add_piece(elephant.Elephant(PlayerSide.DARK))

            # Add the light pieces to the board
            self.cells[CellPosition.LIGHT_RAT[0]][CellPosition.LIGHT_RAT[1]].add_piece(rat.Rat(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_CAT[0]][CellPosition.LIGHT_CAT[1]].add_piece(cat.Cat(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_DOG[0]][CellPosition.LIGHT_DOG[1]].add_piece(dog.Dog(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_WOLF[0]][CellPosition.LIGHT_WOLF[1]].add_piece(wolf.Wolf(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_LEOPARD[0]][CellPosition.LIGHT_LEOPARD[1]].add_piece(leopard.Leopard(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_TIGER[0]][CellPosition.LIGHT_TIGER[1]].add_piece(tiger.Tiger(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_LION[0]][CellPosition.LIGHT_LION[1]].add_piece(lion.Lion(PlayerSide.LIGHT))
            self.cells[CellPosition.LIGHT_ELEPHANT[0]][CellPosition.LIGHT_ELEPHANT[1]].add_piece(elephant.Elephant(PlayerSide.LIGHT))
        
        # Update the pieces on the board
        self.move_history = []
        self.captured_pieces = []
        self.forbidden_move = None
        self.update_pieces()

    def copy(self):
        '''
        Return a copy of the board.
        
        Returns:
            Board: A new Board instance.
        '''
        # Create a new board
        result = Board(False, True)
        result.cells = [[cell.copy() for cell in row] for row in self.cells]
        result.move_history = self.move_history.copy()
        result.update_pieces()

        # Copy the captured pieces
        return result
    
    def get_cell(self, position):
        '''
        Get the cell at the given position.
        
        Args:
            position (tuple): The position of the cell.
        
        Returns:
            Cell: The cell at the given position.
        '''
        return self.cells[position[0]][position[1]]

    def get_valid_moves(self, side):
        '''
        Get the valid moves for the given side.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            list: A list of valid moves for the given side.
        '''
        return [(pin.position, cell.position) for pin in self.pieces_of[side] for cell in pin.available_cells(self) if (pin.position, cell.position) != self.forbidden_move]

    def get_forbidden(self):
        '''
        Get the forbidden move.
        
        Returns:
            tuple: The forbidden move.
        '''
        # Get the last 3 moves
        moves = [move for move in self.move_history[-4:-13:-4]]

        # Check if the last 3 moves are the same
        return moves[0] if len(moves) == 3 and len(set(moves)) == 1 else None
    
    def make_move(self, move):
        '''
        Make a move on the board.
        
        Args:
            move (tuple): The move to make.
        '''
        # Get the source and target cells
        source_cell = self.get_cell(move[0])
        target_cell = self.get_cell(move[1])
        
        # Check if the target cell is in the available cells of the selected piece
        if target_cell.piece:
            self.captured_pieces.append((target_cell.piece, move[1]))
            target_cell.remove_piece()
        
        # Move the piece from the source cell to the target cell
        target_cell.add_piece(source_cell.piece)
        source_cell.remove_piece()
        
        # Update the move history
        self.move_history.append(move)
        self.forbidden_move = self.get_forbidden()
        self.update_pieces()

    def undo_move(self, move):
        '''
        Undo a move on the board.
        
        Args:
            move (tuple): The move to undo.
        '''
        # Get the source and target cells
        source_cell = self.get_cell(move[0])
        target_cell = self.get_cell(move[1])
        
        # Move the piece from the target cell to the source cell
        source_cell.add_piece(target_cell.piece)
        target_cell.remove_piece()
        
        # Restore the captured piece if it exists
        if self.captured_pieces and self.captured_pieces[-1][1] == move[1]:
            captured_piece, _ = self.captured_pieces.pop()
            target_cell.add_piece(captured_piece)
        
        # Update the move history
        self.move_history.remove(move)
        self.update_pieces()

    def update_pieces(self):
        '''
        Update the pieces on the board.
        '''
        # Get the pieces on the board
        self.pieces = [cell.piece for row in self.cells for cell in row if cell.piece]
        self.pieces_of = {
            PlayerSide.DARK: [],
            PlayerSide.LIGHT: []
        }
        
        # Update the pieces of each player
        for piece in self.pieces:
            self.pieces_of[piece.side].append(piece)

    def is_opponent_pieceless(self, side):
        '''
        Check if the opponent has no pieces left.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: Whether the opponent has no pieces left.
        '''
        return not self.pieces_of[side]

    def is_opponent_den_invaded(self, side):
        '''
        Check if the opponent's den is invaded.
        
        Args:
            side (PlayerSide): The side of the player.
        
        Returns:
            bool: Whether the opponent's den is invaded.
        '''
        return self.get_cell(PlayerSide.opponent_den_position(side)).is_occupied_own(side)
    
    @property
    def forbidden_cell(self):
        '''
        Get the forbidden cell.
        
        Returns:
            Cell: The forbidden cell.
        '''
        return self.forbidden_move and self.get_cell(self.forbidden_move[1]) or None

    @property
    def is_dark_win(self):
        '''
        Check if the dark side wins.
        
        Returns:
            bool: Whether the dark side wins.
        '''
        # Get the available moves for the light side
        available_moves = self.get_valid_moves(PlayerSide.LIGHT)

        # Remove the forbidden move if it exists
        if self.forbidden_move and self.forbidden_move in available_moves:
            available_moves.remove(self.forbidden_move)
        
        # Check if the dark side wins
        return self.is_opponent_den_invaded(PlayerSide.DARK) or self.is_opponent_pieceless(PlayerSide.LIGHT) or len(available_moves) == 0
    
    @property
    def is_light_win(self):
        '''
        Check if the light side wins.
        
        Returns:
            bool: Whether the light side wins.
        '''
        # Get the available moves for the dark side
        available_moves = self.get_valid_moves(PlayerSide.DARK)

        # Remove the forbidden move if it exists
        if self.forbidden_move and self.forbidden_move in available_moves:
            available_moves.remove(self.forbidden_move)
        
        # Check if the light side wins
        return self.is_opponent_den_invaded(PlayerSide.LIGHT) or self.is_opponent_pieceless(PlayerSide.DARK) or len(available_moves) == 0
    
    @property
    def is_game_over(self):
        '''
        Check if the game is over.
        
        Returns:
            bool: Whether the game is over.
        '''
        return self.is_dark_win or self.is_light_win
    
    @property
    def winner(self):
        '''
        Get the winner of the game.
        
        Returns:
            PlayerSide: The winner of the game.
        '''
        return PlayerSide.DARK if self.is_dark_win else PlayerSide.LIGHT if self.is_light_win else None
