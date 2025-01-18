import heapq
from collections import namedtuple
from typing import NamedTuple


class Data(NamedTuple):
    n: int
    m: int
    start_room: int
    initial_chips: int
    rooms: list[list[int]]
    costs: list[int]


def solve():
    data = read()
    graph = ConstructAdjMat(data)
    result = dijkstra(graph, data.start_room)
    write(result)
    return 


def read() -> Data:
    with open("in.txt", "r") as f:
        n, m, start_room, initial_chips = map(int, f.readline().split())
        rooms = [list(map(lambda x: int(x) - 1, f.readline().split()))[1:] for _ in range(n)]
        costs = list(map(int, f.readline().split()))
    return Data(n, m, start_room, initial_chips, rooms, costs)


def ConstructAdjMat(data: Data) -> list[list[tuple[int,int]]]: 
    adj = [[] for _ in range(data.n + 1)]
    door_room = [-1] * (data.m)
    for room, doors in enumerate(data.rooms):
        for door in doors:#all doors iter
            other = door_room[door]
            if other == -1: #first encounter
                door_room[door] = room
            else:#second encounter - two room conect
                cost = data.costs[door]
                adj[room+1].append((other+1, cost))
                adj[other+1].append((room+1, cost))
                door_room[door] = -1
    
    for door, room in enumerate(door_room):
        if room != -1:#encountered once
            cost = data.costs[door]
            adj[room+1].append((0, cost))
            adj[0].append((room+1, cost))

    return adj


def dijkstra(graph,start: int) -> tuple[dict[int, float], dict[int, list[int]]]:
    dist = [1e9 for _ in range(len(graph))]
    dist[start] = 0
    parent = [0] * len(graph)
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue #outdated heap entry filter
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    cur = 0
    kek_path = []
    while cur := parent[cur]: kek_path.append(cur)
    kek_path.reverse()
    
    return namedtuple("Result", ["dist", "path"])(dist[0], kek_path)


def write(result) -> None:
    with open("out.txt", "w") as outfile:
        if result[1]:
            outfile.write(f"Y\n{result.dist}\n{' '.join(map(str, result.path))}")
        else:
            outfile.write("N")


solve()