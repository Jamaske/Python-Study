from time import time_ns
N = int(input())
cur = [0] * (N+1)
cur[0] = 1
new = [0] * (N+1)
cnt = 0

mod = 10**9+7

#precompute mods of powers of 2
pow2 = [None] * N 
val = 1
half_mod = mod >> 1
for p in range(N):
    pow2[p] = val
    val = val << 1 if val < half_mod else (val << 1)- mod



for n in range(1,N+1):
    #first column case (no element to the left)
    s = (cur[0] * (pow2[n-1] - 1))%mod
    #if s > mod:print(f"1:{s/mod}")
    for i in range(1, n):
        s = (s + cur[i] * pow2[n-1-i])%mod
        #if s > mod:print(f"2:{s}")
    new[0] = s

    #inner triangle filling
    time = -time_ns()
    operations = 1
    for k in range(1,n):
        C_k_i = 1
        s = cur[k-1] + cur[k] * (pow2[n-1-k] - 1)
        for i in range(k+1,n):
            operations += 1
            C_k_i = ((C_k_i * i)//(i-k)) % mod 
            s = (s + cur[i] * C_k_i * pow2[n - 1 - i]) % mod
            #if C_k_i > mod:print(f"3:{C_k_i}")
            #if s > mod:print(f"4:{s}")
        new[k] = s
    time += time_ns()
    #print(time/operations)
    #diagonal 
    new[n] = 1
    
  

    cur, new = new, [0] * (N+1)
    print(cur[1], end = ', ')
print(cur[1])