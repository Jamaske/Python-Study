n = int(input())
seq = map(int, input().split())
first = next(seq)
prev = first
for el in seq:
    if prev > el:
        print(-1)
        break
    prev = el
else:
    print(prev - first)