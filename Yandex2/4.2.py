from time import time_ns
N = 5000
cnt = 0
S = 0
mod = 10**9 + 7
for n in range(1,N+1):
    time = -time_ns()
    operations = 1
    for k in range(1,n):
        for i in range(k+1,n):
            operations += 1
            S = (S  + i)
    time += time_ns()
    cnt += operations
    print(time/operations)
print(cnt, S)
