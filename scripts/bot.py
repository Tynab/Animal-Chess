from collections import *
from queue import *
from scripts.common import *

class Bot:
    '''
    The bot.

    Methods:
    - get_move(self, board): Get the move.
    - evaluate_position(board, current_side): Evaluate the position of the board.
    - minimax(board, current_side, depth, maximizing_player): Minimax algorithm.
    - minimax_alpha_beta_pruning(board, current_side, depth, alpha, beta, maximizing_player): Minimax algorithm with alpha-beta pruning.
    - breadth_first_search(board, piece, start, ends): Breadth-first search algorithm.
    - a_star_search(board, piece, start, ends): A* search algorithm.
    '''

    @staticmethod
    def evaluate_position(board, current_side):
        '''
        Evaluate the position of the board.
        
        Args:
            board (Board): The board.
            current_side (PlayerSide): The current side.
        
        Returns:
            int: The score.
        '''
        # Initialize the score
        score = 0
        
        # Check if the current player's den is invaded by the opponent
        if board.is_opponent_den_invaded(current_side):
            score += 900
        
        # Check if the opponent's den is invaded by the current player
        if board.is_opponent_den_invaded(PlayerSide.opponent_of(current_side)):
            score -= 900
        
        # Iterate through the pieces
        return score + sum((piece.side == current_side and piece.atk * 10 or -piece.atk * 10) for piece in board.pieces)
    
    @staticmethod
    def minimax(board, current_side, depth, maximizing_player):
        '''
        Minimax algorithm.
        
        Args:
            board (Board): The board.
            current_side (PlayerSide): The current side.
            depth (int): The depth.
            maximizing_player (bool): The maximizing player.
        
        Returns:
            tuple: The best evaluation and the best moves.
        '''
        # Initialize the best moves
        best_moves = []

        # Base case
        if depth == 0 or board.is_game_over:
            return Bot.evaluate_position(board, current_side), best_moves
        
        # Recursive case
        if maximizing_player:
            best_eval = float('-inf')
            player_side = current_side
        else:
            best_eval = float('inf')
            player_side = PlayerSide.opponent_of(current_side)

        # Iterate through the valid moves
        for move in board.get_valid_moves(player_side):
            # Make the move
            board.make_move(move)
            eval, _ = Bot.minimax(board, current_side, depth - 1, not maximizing_player)
            board.undo_move(move)

            # Update the best evaluation and the best moves
            if maximizing_player:
                if eval > best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)

        # Return the best evaluation and the best moves
        return best_eval, best_moves

    @staticmethod
    def minimax_alpha_beta_pruning(board, current_side, depth, alpha, beta, maximizing_player):
        '''
        Minimax algorithm with alpha-beta pruning.
        
        Args:
            board (Board): The board.
            current_side (PlayerSide): The current side.
            depth (int): The depth.
            alpha (int): The alpha value.
            beta (int): The beta value.
            maximizing_player (bool): The maximizing player.
        
        Returns:
            tuple: The best evaluation and the best moves.
        '''
        # Initialize the best moves
        best_moves = []

        # Base case
        if depth == 0 or board.is_game_over:
            return Bot.evaluate_position(board, current_side), best_moves
        
        # Recursive case
        if maximizing_player:
            best_eval = float('-inf')
            player_side = current_side
        else:
            best_eval = float('inf')
            player_side = PlayerSide.opponent_of(current_side)

        # Iterate through the valid moves
        for move in board.get_valid_moves(player_side):
            # Make the move
            board.make_move(move)
            eval, _ = Bot.minimax_alpha_beta_pruning(board, current_side, depth - 1, alpha, beta, not maximizing_player)
            board.undo_move(move)

            # Update the best evaluation and the best moves
            if maximizing_player:
                # Update the best evaluation
                if eval > best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)

                # Update alpha
                alpha = max(alpha, eval)
            else:
                # Update the best evaluation
                if eval < best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)

                # Update beta
                beta = min(beta, eval)

            # Prune the tree
            if beta < alpha:
                break

        # Return the best evaluation and the best moves
        return best_eval, best_moves

    @staticmethod
    def breadth_first_search(board, piece, start, ends):
        '''
        Breadth-first search algorithm.
        
        Args:
            board (Board): The board.
            piece (Piece): The piece.
            start (tuple): The start position.
            ends (list): The end positions.
        
        Returns:
            tuple: The paths and the piece.
        '''
        # Initialize the current board, the current piece, the queue, the visited set, the paths, and the minimum distance
        current_board = board.copy()
        current_piece = piece.copy()
        q = deque([([start], 0)])
        visited = set()
        paths = []
        min_distance = float('inf')

        # Iterate through the queue
        while q:
            # Get the path and the distance
            path, distance = q.popleft()
            current_position = path[-1]
            current_board.get_cell(current_position).add_piece(current_piece)

            # Check if the current position is in the ends
            if current_position in ends and distance <= min_distance:
                # Update the minimum distance
                if distance < min_distance:
                    paths.clear()
                    min_distance = distance
                
                # Add the path to the paths
                paths.append((distance, path))
                ends.remove(current_position)

                # Check if there are no more ends
                if not ends:
                    break

            # Iterate through the available cells
            if current_position not in visited:
                # Add the current position to the visited set
                visited.add(current_position)

                # Iterate through the available cells
                for cell in current_piece.available_cells(current_board):
                    if cell.position not in visited:
                        q.append((path + [cell.position], distance + 1))
        
        # Return the paths and the piece
        return paths or None, None

    @staticmethod
    def a_star_search(board, piece, start, ends):
        '''
        A* search algorithm.

        Args:
            board (Board): The board.
            piece (Piece): The piece.
            start (tuple): The start position.
            ends (list): List of end positions, assumed to be objects with `position` and `piece` attributes.

        Returns:
            tuple: The list of paths sorted by their cost, and the piece.
        '''
        # Initialize the current board, the current piece, the priority queue, the visited set, and the paths list
        current_board = board.copy()
        current_piece = piece.copy()
        pq = PriorityQueue()
        visited = set()
        paths = []
        
        # Function to calculate heuristic based on the piece attack value at the end position
        def heuristic(pos):
            for end in ends:
                if end == pos:
                    cell = current_board.get_cell(pos)
                    return cell.piece and -cell.piece.atk / 10 or -1
            return float('inf')
        
        # Initialize priority queue with the start position and initial cost
        pq.put((heuristic(start), 0, [start]))
        
        while not pq.empty():
            # Get the estimated total cost, path cost, and path
            estimated_total_cost, path_cost, path = pq.get()
            current_position = path[-1]
            current_board.get_cell(current_position).add_piece(current_piece)
            
            # Check if the current position is an end position
            if any(end == current_position for end in ends):
                paths.append((estimated_total_cost, path))
                ends.remove(next(end for end in ends if end == current_position))
                if not ends:
                    break
            # Iterate through the available cells
            if current_position not in visited:
                visited.add(current_position)
                for cell in current_piece.available_cells(current_board):
                    if cell.position not in visited:
                        new_path_cost = path_cost + 1
                        estimated_cost = new_path_cost + heuristic(cell.position)
                        pq.put((estimated_cost, new_path_cost, path + [cell.position]))
        
        return paths or None, None
