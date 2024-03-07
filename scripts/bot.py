import random
from collections import deque
from scripts.common import PlayerSide

class Bot:

    @staticmethod
    def evaluate_position(board):
        return sum((piece.is_dark and piece.atk * 10 or -piece.atk * 10) for piece in board.pieces)

    @staticmethod
    def minimax(board, depth, alpha, beta, maximizing_player):
        best_move = None
        if depth == 0 or board.is_game_over:
            return Bot.evaluate_position(board), best_move
        if maximizing_player:
            best_eval = float('-inf')
            player_side = PlayerSide.DARK
        else:
            best_eval = float('inf')
            player_side = PlayerSide.LIGHT
        for move in board.get_valid_cells(player_side):
            board.make_move(move)
            eval, _ = Bot.minimax(board, depth - 1, alpha, beta, not maximizing_player)
            board.undo_move(move)
            if maximizing_player:
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_move = move
                beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_eval, best_move

    @staticmethod
    def random_move(board, side):
        return random.choice(board.get_valid_cells(side))

    @staticmethod
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
                for cell in piece.available_cells(board):
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
