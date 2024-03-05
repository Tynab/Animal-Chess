import random
from collections import deque
from scripts.common import PlayerSide

def evaluate_position(board):
    score = 0
    for piece in board.pieces:
        if piece.side == PlayerSide.DARK:
            score += piece.atk * 10
        else:
            score -= piece.atk * 10
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.get_valid_moves(PlayerSide.DARK):
            board.make_move(move)
            eval = minimax(board, depth - 1, alpha, beta, False)[0]
            board.undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in board.get_valid_moves(PlayerSide.LIGHT):
            board.make_move(move)
            eval = minimax(board, depth - 1, alpha, beta, True)[0]
            board.undo_move(move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def random_move(board, side):
    valid_moves = board.get_valid_moves(side)
    return random.choice(valid_moves)

def shortest_paths(board, piece, start, ends):
    queue = deque([([start], 0)])
    visited = set()
    shortest_paths = [] # Lưu trữ các đường đi ngắn nhất tới tất cả các điểm đích
    
    while queue:
        path, distance = queue.popleft()
        current_position = path[-1]
        board.get_cell(current_position).add_piece(piece)
        if current_position in ends:
            shortest_paths.append((distance, path))
            ends.remove(current_position) # Loại bỏ điểm đích đã tìm được từ danh sách
            if not ends: # Nếu không còn điểm kết thúc nào, kết thúc tìm kiếm
                break
        if current_position not in visited:
            visited.add(current_position)
            for cell in piece.available_moves(board):
                if cell.position not in visited:
                    new_path = path + [cell.position]
                    queue.append((new_path, distance + 1))
    
    if shortest_paths:
        # Tìm đường đi có khoảng cách ngắn nhất trong tất cả các đường đi ngắn nhất
        shortest_path = min(shortest_paths, key=lambda x: x[0])
        print(f"Đường đi ngắn nhất trong số các đường đi ngắn nhất: {shortest_path[1]} với khoảng cách {shortest_path[0]}")
        return shortest_path
    else:
        print(f"Không tìm thấy đường đi từ {start} đến bất kỳ điểm kết thúc nào.")
        return -1, None