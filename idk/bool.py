def nand(a, b):
    return ~(a & b) & mask

def nor(a,b):
    return ~(a | b) & mask


def e_wraper(a, b):
    return f"({a}{b})"


n = 2
size = 2 ** n
mask = 2 ** size - 1

#next_page = [(0b1100, "a"), (0b1010, "b")]
#next_page = [(0b1100, "a"), (0b1010, "b"), (0b0111,"[!ab]"), (0b1000, "[ab]")] # nand sum setup
next_page = [(0b0011, "!a"),  (0b1010, "b")] # nor sum setup

#next_page = [(0b11110000, "a"), (0b11001100, "b"), (0b10101010, "c")]
#next_page = [(0b1111111100000000, "a"), (0b1111000011110000, "b"), (0b1100110011001100, "c"), (0b1010101010101010, "d")]
unique = [next_page]
storage_limit = 4
visited: list[list[str]] = [[] for _ in range(mask + 1)]
for val, exp in next_page: visited[val].append(exp)

func_found = len(next_page)
body_execut = 0

pairs_left:set[int] = set()
for i in range(mask + 1):
    for j in range(i + 1):
        c = j << size | i
        pairs_left.add(c)


def innerBody(arg1, arg2):
    global body_execut, func_found
    body_execut += 1

    val1, exp1 = arg1
    val2, exp2 = arg2

    c1 = val1 << size | val2
    c2 = val2 << size | val1
    if c1 in pairs_left: pairs_left.remove(c1)
    if c2 in pairs_left: pairs_left.remove(c2)

    val = nor(val1, val2)
    
    store:list[str] = visited[val]
    if len(store) < storage_limit:
        exp = e_wraper(exp1, exp2)
        res = (val, exp)
        if not store:
            func_found += 1
            next_page.append(res)
        store.append(exp)

        
    #visited.setdefault(val, []).append(exp)
    
    

    


generation = 0
while func_found <= mask:
    print(f"==== generation {generation} ====  {func_found}/{mask + 1} function found. {body_execut} function explored")

    next_page = []
    for page in unique[:-1]:#cross level expresions
        for arg1 in page:
            for arg2 in unique[-1]:
                innerBody(arg1, arg2)
    for i, arg1 in enumerate(unique[-1]):#new level expresions
        for arg2 in unique[-1][i:]:
            innerBody(arg1, arg2)
    unique.append(next_page)
    generation += 1
print(f"======== Done ========  {func_found} function found. {body_execut} function explored")

# # все функции в хронологическом порядке
# for i, gen in enumerate(unique):
#     print(f"==== generation {i} ====")
#     for val, exp in gen:
#         print(f"{val:0{size}b} - {exp}")

# # последние (сложные) функции
# for val, _ in unique[-1]:
#     print(f"{val:0{size}b}")
#     for exp in visited[val]: print(exp)

# Список всех функций в разных вырожениях
for val, exps in enumerate(visited):
    print(f"{val:0{size}b}")
    #print(exps[0])
    for exp in exps: print(exp)

# for c in pairs_left:
#     a = c & mask
#     b = c >> size
#     print(f"{a} + {b}")