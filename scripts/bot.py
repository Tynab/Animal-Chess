from collections import deque
from scripts.common import PlayerSide

class Bot:

    @staticmethod
    def evaluate_position(board, current_side):
        score = 0
        if board.is_opponent_den_invaded(current_side):
            score += 900
        if board.is_opponent_den_invaded(PlayerSide.opponent_of(current_side)):
            score -= 900
        return score + sum((piece.side == current_side and piece.atk * 10 or -piece.atk * 10) for piece in board.pieces)

    @staticmethod
    def minimax_alpha_beta_pruning(board, current_side, depth, alpha, beta, maximizing_player):
        best_moves = []
        if depth == 0 or board.is_game_over:
            return Bot.evaluate_position(board, current_side), best_moves
        if maximizing_player:
            best_eval = float('-inf')
            player_side = current_side
        else:
            best_eval = float('inf')
            player_side = PlayerSide.opponent_of(current_side)
        for move in board.get_valid_moves(player_side):
            board.make_move(move)
            eval, _ = Bot.minimax_alpha_beta_pruning(board, current_side, depth - 1, alpha, beta, not maximizing_player)
            board.undo_move(move)
            if maximizing_player:
                if eval > best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)
                alpha = max(alpha, eval)
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_moves = [move]
                elif eval == best_eval:
                    best_moves.append(move)
                beta = min(beta, eval)
            if beta < alpha:
                break
        return best_eval, best_moves

    @staticmethod
    def breadth_first_search(board, piece, start, ends):
        board_temp = board.copy()
        piece_temp = piece.copy()
        queue = deque([([start], 0)])
        visited = set()
        paths = []
        min_distance = float('inf')
        while queue:
            path, distance = queue.popleft()
            current_position = path[-1]
            board_temp.get_cell(current_position).add_piece(piece_temp)
            if current_position in ends and distance <= min_distance:
                if distance < min_distance:
                    paths.clear()
                    min_distance = distance
                paths.append((distance, path))
                ends.remove(current_position)
                if not ends:
                    break
            if current_position not in visited:
                visited.add(current_position)
                for cell in piece_temp.available_cells(board_temp):
                    if cell.position not in visited:
                        queue.append((path + [cell.position], distance + 1))
        return paths or None, None
