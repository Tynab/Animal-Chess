import random
from scripts.common import CellPosition, PlayerSide

# def evaluate_position(board):
#     """
#     Evaluates the position of a game state.

#     Args:
#         board: The current game state.

#     Returns:
#         The score of the game state.
#     """
#     score = 0
#     for piece in board.pieces:
#         if piece is not None:
#             score += piece.atk * 10
#             if board.get_cell(piece.position).label == CellLabel.DEN:
#                 score += 900
#     return score

def evaluate_position(board):
    score = 0
    for piece in board.pieces:
        if piece:
            score += piece.atk * 10
            if board.is_chessmate(piece):
                score += 900
            # else:
            #     shortest_distance = shortest_path(board, piece.position, piece.side == PlayerSide.DARK and CellPosition.LIGHT_DEN or CellPosition.DARK_DEN)
            #     if shortest_distance is not None:
            #         score -= shortest_distance
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.get_valid_moves(PlayerSide.DARK):
            board.make_move(move)
            print('Move 0:', move)
            eval = minimax(board, depth - 1, alpha, beta, False)[0]
            print('Eval 0:', eval)
            board.undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
                print('Best move 0:', best_move)
                print('Max eval 0:', max_eval)
            alpha = max(alpha, eval)
            print('Alpha 0:', alpha)
            print('Beta 0:', beta)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in board.get_valid_moves(PlayerSide.DARK):
            board.make_move(move)
            print('Move 1:', move)
            eval = minimax(board, depth - 1, alpha, beta, True)[0]
            print('Eval 1:', eval)
            board.undo_move(move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
                print('Best move 1:', best_move)
                print('Min eval 1:', min_eval)
            beta = min(beta, eval)
            print('Alpha 1:', alpha)
            print('Beta 1:', beta)
            if beta <= alpha:
                break
        return min_eval, best_move
    
def random_move(board):
    valid_moves = board.get_valid_moves()
    return random.choice(valid_moves)

def shortest_path(board, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        cell, distance = queue.pop(0)
        if cell == end:
            return distance
        visited.add(cell)
        for neighbor in board.get_cell(cell).neighbors:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
    return None
