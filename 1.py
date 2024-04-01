def f(x,y,n, N):
    #print(" | "*n, x, y)
    if n == N: return 1
    s = 0

    for i in range(x + 1, y + 1):
        s += f(i, y, n+1, N)
    
    for j in range(y+1, n):
        for i in range(j + 1):
            s += f(i, j, n+1, N)
    return s


#print(f(0, -1, 2, 5))
for N in range(2, 12):print(N, f(0, -1, 2, N))