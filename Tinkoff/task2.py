n,m = map(int, input().split())

matrix = [map(int, input().split()) for i in range(n)]
rotated = zip(*(matrix[::-1]))
for i in rotated: print(*i)