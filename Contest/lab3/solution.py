




def Dijkstra(graph, start, finish)->(list[int], int):
    inf = 10 ** 10

    dist = [graph[start].get(i, inf) for i in range(len(graph))]
    dist[start] = 0

    parents = [start for i in range(len(graph))]
    parents[start] = None

    front = set(graph[start])
    visited = set((start,))

    while front and finish not in front:
        
        cur, cur_dist = None, inf
        for i in front:
            if dist[i] < cur_dist:
                cur = i
                cur_dist = dist[i]
        front.remove(cur)
        visited.add(cur)
        front.update(graph[cur].keys() - visited)

        for adj in graph[cur]:
            if dist[adj] > cur_dist + graph[cur][adj]:
                dist[adj] = cur_dist + graph[cur][adj]
                parents[adj] = cur
    
    if not front: return None, None

    path = []
    cur = finish
    while cur != None:
        path.append(str(cur + 1))
        cur = parents[cur]
    return path, dist[finish]




with open("in.txt", "r") as file:
    N = int(file.readline())
    graph = [{} for i in range(N)] #list of maps (dicts). 
    # list index - edge source
    # map key - edge dest
    # map value - edge weight
    # проверка существования ребра, создание ребра и получение веса ребра O(1)
    # итерация по всем исходящим из вершины рёбрам O(колличество изходящих рёбер)

    for i in range(N):
        line = map(int, file.readline().split())
        for j in line:
            if (j):
                graph[j-1][i] = next(line)
    
    start, dest = map(int, file.readlines(2))

path, dist = Dijkstra(graph, start - 1, dest - 1)

with open("out.txt", "w") as file:
    if path:
        file.write(f"Y\n{' '.join(reversed(path))}\n{dist}")
    else:
        file.write("N")