N = int(input())
points = [None] * (N)
for i in range(N):
    ai, bi = input().split()
    points[i]=(int(ai),int(bi))

B = list(map(lambda x: x[1] ,sorted(points, key = lambda x: x[0])))

x = 0
left_max = [None] * (N+1) 
left_max[N] = x  #не забудь втавить 0 на idx = -1
for i in range(N):
    x = max(x, B[i])
    left_max[i] = x

count = 0

x = 2 * N + 1 # равносилно +inf
for i in range(N - 1, -1, -1):
    
    if left_max[i-1] < B[i] < x:
        count += 1

    x = min(x, B[i])

print(count)
