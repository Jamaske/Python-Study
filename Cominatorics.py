from multiset import FrozenMultiset as fms

#initial_signals, mask = [0b100001111, 0b100110011, 0b101010101], 0b11111111
initial_signals, mask = [0b10011, 0b10101], 0b1111
N = len(initial_signals)
D = 1 << N
S = 1 << D
def nand(a, b):
    return mask ^ (a & b)


def binary(a):
    return bin(a)[3:]




stack = initial_signals
set = set(stack)
pairs = {}
a = 0

i = 0
while i < len(stack):
    x = stack[i]

    print(binary(x), end=' ')
    b = 0

    j = 0
    while j <= i:
        y = stack[j]

        z = nand(x, y)
        pairs[fms((x, y))] = pairs.get(fms((x, y)), 0) + 1
        b += 1
        if z not in set:
            stack.append(z)
            set.add(z)
        j += 1
    i += 1
    print(b)
    a += b


print(f'all pairs and their counts:')
counts = [0] * 5
for pair, count in pairs.items():
    counts[count] += 1

    print(f"{' '.join([binary(i) for i in pair])}  {count}")

print(f'counts total: {sum(counts)}\npairs total: {len(pairs)}\npairs possible: {S*(S+1)//2}')
counts[0] = S*(S+1)//2 - len(pairs)
print(f'amount of pairs with the counts:\n{counts}')
