N = int(input())
x, y = 0, 0
X, Y = 0, 0
for i in range(N):
    dx, dy = map(int, input().split())
    x += dx
    y += dy
    
for i in range(N):
    dx, dy = map(int, input().split())
    X += dx
    Y += dy

print((X - x) // N, (Y - y) // N)
