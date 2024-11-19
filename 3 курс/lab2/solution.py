from itertools import repeat

def reader(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    sx, sy = map(int, lines[0].split())
    drain = sx + sy + 1
    graph = [None] * (drain + 1)

    graph[0] = set(range(1,sx + 1))
    for x in range(1, sx + 1):
        graph[x] = set(map(lambda x: int(x) + sx, lines[x].split()[:-1]))
    for y in range(sx + 1, drain):
        graph[y] = set([drain])
    graph[drain] = set()

    return graph, sx

def writer(file_path, flow, size_x):
    res = [None] * size_x
    for x in range(1, size_x + 1):
        for y in flow[x]:
            res[x - 1] = str(y - size_x)
            break
        else:
            res[x -1] = '0'
    
    with open(file_path, 'w') as file:
        file.write(' '.join(res))


def custom_bfs(succs, pred, flow):
    trace = list(enumerate([None] * len(succs)))
    drain = len(succs) - 1

    next_front = []
    cur_front = [0]
    while cur_front:
        for cur in cur_front:
            for vert in succs[cur]:
                if vert == trace[vert][0] and vert not in flow[cur]:
                    trace[vert] = (cur, 1)
                    if vert == drain:return trace
                    next_front.append(vert)

                    
            for vert in pred[cur]:
                if vert == trace[vert][0] and vert in flow[cur]:
                    trace[vert] = (cur, -1)
                    if vert == drain:return trace
                    next_front.append(vert)
            
        cur_front, next_front = next_front, []
    raise Exception("No path") 
    return False

def max_flow(succs, pred):
    drain = len(succs) - 1
    #list of sets - if flow  (u, v) is present then (v in flow[u])
    flow = [set() for adj in succs]
    #no need in f-chain deltas. becouse they are always equal to 1
    #trace contains (parent, mode) pairs.abs
    #parent of a vertex is a vertex it were reached from.
    #if parent[x] = x, then this vertex is untouched yet
    #if parent is initialized then mode is ether 1 or -1 for direct and reversed edge traversing

    while trace:= custom_bfs(succs, pred, flow):
        cur = drain
        while cur:
            prev, mode = trace[cur]
            if mode == 1:
                flow[prev].add(cur)
            else:
                del flow[cur][prev]
            cur = prev
    
    return flow       

def predicates(graph):
    result = [[] for i in range(len(graph))]
    for x, adj in enumerate(graph):
        for y in adj:
            result[y].append(x)
    return result



def main():
    succsessor, size_x = reader('in.txt')
    predecessor = predicates(succsessor)
    flow = max_flow(succsessor, predecessor)
    writer('out.txt', flow, size_x)


if __name__ == "__main__":
    main()