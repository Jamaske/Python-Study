from multiset import FrozenMultiset as fms
def nand(a, b):
    return 0b11111111 ^ (a & b)


def binary(a):
    return bin(a)[3:]

stack = [0b100001111, 0b100110011]
set = set(stack)
combinations = {}
i = 0
for x in stack:
    print(binary(x), end=' ')
    j = 0
    for y in stack:
        z = nand(x, y)
        combinations[fms((x, y))] = combinations.get(fms((x, y)), 0) + 1
        j += 1
        if z not in set:
            stack.append(z)
            set.add(z)
    i += j
    print(j)
print('total combinations', i)


sum = 0
counts = [0]
for pair in combinations.items():
    sum += pair[1]
    print(pair[0], pair[1])

print(len(combinations))
#print(len(stack))
