'''
given n b-bit numbers
what is probability of k unique values?
formaly
static parameter b
find P(n,k)
'''

b = 3
base = 1 << b
prev = [0] * base
prev[0] = 1
table = [prev]

for n in range(2, 20+1):
    next = [None] * base
    next[0] = 1
    for k in range(1, base):
        next[k] = (prev[k] - prev[k-1])*(k+1) + prev[k-1] * (base + 1)
    table.append(next)
    prev = next

for n, row in enumerate(table):
    k = 1 / (base ** n)
    for el in row:
        print(f"{el * k: 0.3f}", end='\t')
    print()