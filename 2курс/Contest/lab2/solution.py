def BFS(adjacent, start):
    parent = [0]*len(graph)
    cur_front, next_front = [start], []
    parent[start-1] = -1
    while cur_front:
        for cur_node in cur_front:
            for next_node in adjacent[cur_node - 1]:
                if next_node == parent[cur_node - 1]: continue #ignore parent
                if parent[next_node-1]:
                    return (parent, cur_node, next_node, next_node in cur_front) #cycle found, needed info returned

                parent[next_node-1] = cur_node
                next_front.append(next_node)

        cur_front, next_front = next_front, []
    return ()


def find_cycle(parent, vert1, vert2, equal_len:bool):
    if not equal_len: #equalize distances to BFS's root
        yield vert2
        vert2 = parent[vert2 - 1]
    path1 = []
    #traverse through paths from given vertices to the root and mark first of them until they collide
    while vert1 != vert2:
        path1.append(vert1)
        yield vert2
        vert1 = parent[vert1 - 1]
        vert2 = parent[vert2 - 1]
    yield vert2 #mark paths common vertex
    for vert in reversed(path1): yield vert #mark second path backward to complete cycle


with open("in.txt", "r") as file: graph = [list(map(int, file.readline().split()))[:-1] for i in range(int(file.readline()))]

res = BFS(graph, 1)

if res: 
    cycle = find_cycle(*res)
    out = "N\n" + " ".join(map(str,sorted(cycle)))
else:
    out = "A"

with open("out.txt", "w") as file: file.write(out)