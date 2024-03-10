from collections import deque
from scripts.common import PlayerSide

class Bot:

    @staticmethod
    def evaluate_position(board, current_side):
        score = 0
        for piece in board.pieces:
            if piece.side == PlayerSide.DARK:
                score += piece.atk * 10
            else:
                score -= piece.atk * 10
        if board.is_opponent_den_invaded(PlayerSide.DARK):
            score += 900
        if board.is_opponent_den_invaded(PlayerSide.LIGHT):
            score -= 900
        return score
        # return score + sum((piece.side == PlayerSide.DARK and piece.atk * 10 or -piece.atk * 10) for piece in board.pieces)

    @staticmethod
    def minimax_alpha_beta_pruning(board, current_side, depth, alpha, beta, maximizing_player):
        best_moves = []
        if depth == 0 or board.is_game_over:
            return Bot.evaluate_position(board, current_side), best_moves
        if maximizing_player:
            best_eval = float('-inf')
            player_side = PlayerSide.DARK
        else:
            best_eval = float('inf')
            player_side = PlayerSide.LIGHT
        for move in board.get_valid_moves(player_side):
            if move == ((2, 6), (1, 6)) and player_side == PlayerSide.LIGHT:
                pass
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

        # first_eval = True
        # same_eval = True
        # previous_eval = None
        # for move in board.get_valid_moves(player_side):
        #     board.make_move(move)
        #     eval, _ = Bot.minimax_alpha_beta_pruning(board, current_side, depth - 1, alpha, beta, not maximizing_player)
        #     board.undo_move(move)
        #     if first_eval:
        #         previous_eval = eval
        #         first_eval = False
        #     elif eval != previous_eval:
        #         same_eval = False
        #     if maximizing_player and eval > best_eval:
        #         best_eval = eval
        #         best_move = move
        #         alpha = max(alpha, eval)
        #     elif not maximizing_player and eval < best_eval:
        #         best_eval = eval
        #         best_move = move
        #         beta = min(beta, eval)
        #     if beta <= alpha:
        #         break
        # print(f"Eval: {best_eval}, Move: {best_move}")  # Add this line to print the evaluation and best move
        # return same_eval and (best_eval, None) or (best_eval, best_move)

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
                    paths = []
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
