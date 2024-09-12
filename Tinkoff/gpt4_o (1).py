from collections import deque

# Ходы коня
knight_moves = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# Ходы короля
king_moves = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(board, n, start, end):
    queue = deque([(start[0], start[1], 'K', 0)])  # (x, y, piece_type, steps)
    visited = set([(start[0], start[1], 'K')])
    
    while queue:
        x, y, piece_type, steps = queue.popleft()

        if (x, y) == end:
            return steps

        if piece_type == 'K':
            moves = knight_moves
        else:
            moves = king_moves

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n) and (nx, ny, piece_type) not in visited:
                if board[nx][ny] == '.':
                    queue.append((nx, ny, piece_type, steps + 1))
                    visited.add((nx, ny, piece_type))
                elif board[nx][ny] == 'K':
                    queue.append((nx, ny, 'K', steps + 1))
                    visited.add((nx, ny, 'K'))
                elif board[nx][ny] == 'G':
                    queue.append((nx, ny, 'G', steps + 1))
                    visited.add((nx, ny, 'G'))
    
    return -1

# Чтение входных данных
n = int(input().strip())
board = [input().strip() for _ in range(n)]

start = None
end = None

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start = (i, j)
        elif board[i][j] == 'F':
            end = (i, j)

# Вызов функции и вывод результата
result = bfs(board, n, start, end)
print(result)