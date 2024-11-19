def find_deviation(targets, hits):
    targets.sort()
    hits.sort()

    n = len(targets)
    u, v = targets[0][0] - hits[0][0], targets[0][1] - hits[0][1]

    for i in range(1, n):
        if (targets[i][0] - hits[i][0], targets[i][1] - hits[i][1]) != (u, v):
            return None

    return u, v

# Чтение входных данных
n = int(input())
targets = []
hits = []
for _ in range(n):
    x, y = map(int, input().split())
    targets.append((x, y))
for _ in range(n):
    x, y = map(int, input().split())
    hits.append((x, y))

# Вычисление и вывод результата
result = find_deviation(targets, hits)
if result:
    print(*result)
else:
    print("No solution")