import collections


def BFS(graph, root):
    visited = set()
    front = collections.deque([root])
    prev_vert = list(range(len(graph)))
    while front:
        vertex = front.pop()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                prev_vert[neighbour] = vertex
                visited.add(neighbour)
                front.append(neighbour)
    return prev_vert

def path(BFS_result,root ,  target):
    path = [target]
    vert = target
    while vert != root:
        vert = BFS_result[vert]
        path.append(vert)
    return path

def Read_text("path"):
    try:
        text = open(path)
    graph = {}

    for word, next in zip(text, text[1:]):
        if word not in graph:
            graph[word] = {}
        graph[word][next] = graph[word].get(next, 0)
    return graph


result = BFS(a, 0)
path = path(result, 0, 4)
print(result)
print(path)
