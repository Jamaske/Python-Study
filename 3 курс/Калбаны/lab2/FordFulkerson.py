
def custom_bfs(succs: list[dict[int, int]], pred: list[dict[int, int]], flow: list[dict[int, int]], src: int, drain: int):
    # same as parents but with direction second
    trace = [(None, 0) for _ in range(len(succs))]
    # use not None trance as visited mark

    cur_front = [src]
    front = []
    while cur_front:
        for cur in cur_front:

            for vert, throughput in succs[cur].items():
                #  проверка на не посещёность  и  проверка на запас по пропускной способности
                if trace[vert][0] is not None and flow[cur][vert] < throughput:
                    trace[vert] = (cur, 1)
                    if vert == drain:
                        return trace
                    front.append(vert)
                    
            for vert in pred[cur]:
                if vert == trace[vert][0] and vert in flow[cur]:
                    trace[vert] = (cur, -1)
                    if vert == drain:return trace
                    front.append(vert)
            
        cur_front, front = front, []
    raise Exception("No path") 
    return False

def max_flow(succs, pred, src ,drain):
    flow = [dict() for adj in succs]

    while trace:= custom_bfs(succs, pred, flow, src, drain):
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
    pred = [dict() for i in range(len(graph))]
    for From, adj in enumerate(graph):
        for To, Weight in adj.items():
            pred[To][From] = Weight
    return pred

# weighted edges from source vert to destinactions verts
# succs[source] = {destinations : weignts}
# wighted edges from sources verts to destination vert
# pred[destination] = {sources : weights}
graph : list[dict[int, int]] = [
    {1: 10, 2: 10},
    {4: 10},
    {3: 10, 5: 5},
    {5: 10},
    {6: 10},
    {},
    {6: 10},
    ]

s = 0
t = 6
succs = graph
pred = predicates(graph)

flow = max_flow(succs, pred, s, t)

print(flow)