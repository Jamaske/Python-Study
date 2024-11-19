from itertools import combinations
N = 7
for n in range(N):
    edges = list(combinations(range(n),r=2))
    result = [0] * (N+1)
    for i in range(1 << len(edges)):
        counters = [0] * n
        for j in range(len(edges)):
            if i&(1<<j):
                counters[edges[j][0]] += 1
                counters[edges[j][1]] += 1
        full = 0
        for j in range(n):
            if counters[j] == n-1:full+=1
        result[full] += 1
    for val in result:print(f'{val:5}', end= ' ')
    print('')

    1, 0, 1, 4, 41, 768, 27449
    0, 1, 0, 3, 16, 205, 4608