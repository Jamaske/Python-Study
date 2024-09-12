from collections import deque

# Ходы коня
knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                (2, 1), (1, 2), (-1, 2), (-2, 1)]
# Ходы короля
king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def bfs(board, start, end, n):
    # (x, y, тип фигуры, количество ходов)
    queue = deque([(start[0], start[1], 'K', 0)])
    # множество посещённых состояний (x, y, тип фигуры)
    visited = set([(start[0], start[1], 'K')])

    while queue:
        x, y, piece, moves = queue.popleft()

        if (x, y) == end:
            return moves

        next_moves = knight_moves if piece == 'K' else king_moves

        for dx, dy in next_moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n) and (nx, ny, piece) not in visited:
                if board[nx][ny] == 'K':
                    next_piece = 'K'
                elif board[nx][ny] == 'G':
                    next_piece = 'G'
                else:
                    next_piece = piece

                
                visited.add((nx, ny, next_piece))
                queue.append((nx, ny, next_piece, moves + 1))

    return -1


def main():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]

    start = end = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start = (i, j)
            elif board[i][j] == 'F':
                end = (i, j)

    print(bfs(board, start, end, n))


if __name__ == "__main__":
    main()
