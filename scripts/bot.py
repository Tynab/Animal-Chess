from collections import deque
from scripts.common import PlayerSide

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
