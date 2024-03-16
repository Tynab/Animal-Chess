import math
import random
from collections import deque
from scripts.common import PlayerSide
from scripts.mcts import MCTSNode

class Bot:
    '''
    Bot class.

    Attributes:
    - name: The name of the bot.
    - side: The side of the bot.
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
        
        # Check if the opponent's den is invaded
        if board.is_opponent_den_invaded(current_side):
            score += 900
        
        # Check if the current player's den is invaded by the opponent
        if board.is_opponent_den_invaded(PlayerSide.opponent_of(current_side)):
            score -= 900
        
        # Calculate the score based on the pieces on the board
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
        # Initialize the variables
        board_temp = board.copy()
        piece_temp = piece.copy()
        queue = deque([([start], 0)])
        visited = set()
        paths = []
        min_distance = float('inf')

        # Iterate through the queue
        while queue:
            # Dequeue the path and the distance
            path, distance = queue.popleft()
            current_position = path[-1]
            board_temp.get_cell(current_position).add_piece(piece_temp)

            # Check if the current position is in the ends
            if current_position in ends and distance <= min_distance:
                # Update the paths and the minimum distance
                if distance < min_distance:
                    paths.clear()
                    min_distance = distance
                
                # Add the path
                paths.append((distance, path))
                ends.remove(current_position)

                # Check if there are no ends
                if not ends:
                    break

            # Iterate through the available cells
            if current_position not in visited:
                # Add the current position to the visited set
                visited.add(current_position)

                # Add the available cells to the queue
                for cell in piece_temp.available_cells(board_temp):
                    # Add the cell to the queue
                    if cell.position not in visited:
                        queue.append((path + [cell.position], distance + 1))
        
        # Return the paths and the piece
        return paths or None, None

    @staticmethod
    def mcts_move(board, current_side, iterations=1000):
        '''
        Monte Carlo Tree Search move.
        
        Args:
            board (Board): The board.
            current_side (PlayerSide): The current side.
            iterations (int): The number of iterations.
            
        Returns:
            tuple: The best move.
        '''
        # Initialize the root node
        root = MCTSNode(board, side=current_side)

        # Iterate through the iterations
        for _ in range(iterations):
            node = Bot.select_node(root)
            winner = Bot.simulate_random_game(node.board, node.side)
            Bot.backpropagate(node, winner)
        
        # Return the best move
        return Bot.best_move(root)
    
    @staticmethod
    def expand_node(node):
        for move in node.board.get_valid_moves(node.side):
            temp_board = node.board.copy()
            temp_board.make_move(move)
            node.children.append(MCTSNode(temp_board, parent=node, move=move, side=PlayerSide.opponent_of(node.side)))

    @staticmethod
    def select_node(node):
        '''
        Select a node.
        
        Args:
            node (MCTSNode): The node.
        
        Returns:
            MCTSNode: The selected node.
        '''
        # Select the node with the highest UCB value
        while node.children:
            ucb_values = [child.wins / (child.visits + 1e-4) + math.sqrt(2) * math.sqrt(math.log(node.visits + 1e-4) / (child.visits + 1e-4)) for child in node.children]
            node = node.children[ucb_values.index(max(ucb_values))]

        # Check if the node has no children
        if not node.children:
            Bot.expand_node(node)

        # Expand the node
        return node

    @staticmethod
    def simulate_random_game(board, current_side):
        '''
        Simulate a random game.
        
        Args:
            board (Board): The board.
            current_side (PlayerSide): The current side.
        
        Returns:
            PlayerSide: The winner.
        '''
        # Initialize the variables
        temp_board = board.copy()
        player_side = current_side

        # Simulate the random game
        while not temp_board.is_game_over:
            # Get the valid moves
            valid_moves = temp_board.get_valid_moves(player_side)

            # Check if there are no valid moves
            if not valid_moves:
                break

            # Make the move
            temp_board.make_move(random.choice(valid_moves))
            player_side = PlayerSide.opponent_of(player_side)

        # Return the winner
        return PlayerSide.DARK if temp_board.is_opponent_den_invaded(PlayerSide.DARK) else PlayerSide.LIGHT if temp_board.is_opponent_den_invaded(PlayerSide.LIGHT) else None

    @staticmethod
    def backpropagate(node, winner):
        '''
        Backpropagate the winner.
        
        Args:
            node (MCTSNode): The node.
            winner (PlayerSide): The winner.
        '''
        while node:
            node.visits += 1
            node.wins += winner == node.side
            node = node.parent

    @staticmethod
    def best_move(root):
        '''
        Return the best move.
        
        Args:
            root (MCTSNode): The root node.
        
        Returns:
            tuple: The best move.
        '''
        return root.children and max(root.children, key=lambda child: child.visits).move or None
