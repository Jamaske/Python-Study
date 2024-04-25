N = int(input())
oper = input()
trailing_F = [None] * N
F_cnt = 0
# обратная проходка
for i in range(N-1, -1 ,-1):
    trailing_F[i] = F_cnt
    if oper[i] == 'F':F_cnt +=1
    else: F_cnt = 0


deltas = set()
Dir = 1

for i in range(N):
    tr = trailing_F[i]
    tr1 = tr + 1
    match(oper[i]):
        case 'R':
            deltas.add(Dir * tr1 - tr)
            deltas.add(-2*tr)
            Dir = 1
        case 'L':
            deltas.add(2 * tr)
            deltas.add(Dir * tr1 + tr)
            Dir = -1
        case 'F':
            deltas.add(tr - Dir * tr1)
            deltas.add(-tr - Dir * tr1)

print(len(deltas))