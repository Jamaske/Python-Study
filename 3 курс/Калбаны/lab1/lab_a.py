from itertools import chain

def solve(graph):
    #init process at arbitrary vertex
    start = 0
    conected_vertex = set([start])
    result = [[] for i in range(len(graph))]
    weight_sum = 0
    edge_front = {} #{key:value} key - outside vert, value - minimal edge weight inside vert. 
    for vert, weight in graph[start].items():
        del graph[vert][start]
        edge_front[vert] = start

    while edge_front:
        #brut force min edge search
        min_weight = int(1e18)
        cur_vert = -1
        for ext_vert, in_vert  in edge_front.items():
            if graph[in_vert][ext_vert] < min_weight:
                min_weight = graph[in_vert][ext_vert]
                cur_vert = ext_vert

        #add edge to answer
        result[edge_front[cur_vert]].append(cur_vert)
        result[cur_vert].append(edge_front[cur_vert])
        weight_sum += min_weight

        #update structures state
        del edge_front[cur_vert]    
        conected_vertex.add(cur_vert)

        #add or update edges
        for adj_vert, new_weight in graph[cur_vert].items():
            del graph[adj_vert][cur_vert]
            if adj_vert not in edge_front or new_weight < graph[edge_front[adj_vert]][adj_vert]:
                edge_front[adj_vert] = cur_vert

    for adj in result:
        adj.sort()

    for i in graph: print(i)
    return result, weight_sum

def writer(adjacency_list):   
    res = ' 0\n'.join(map(lambda adj: ' '.join(map(lambda x: str(x + 1),adj)), adjacency_list))
    with open('out.txt', 'w') as file: file.write(res)    

def reader(file_path):
    with open(file_path, 'r') as file: lines = file.readlines()
    return list(chain(*map(lambda line: map(int, line.split()), lines[1:])))

def adjacency_list(all_values):
    graph, i = [], 0
    while (start := all_values[i]) != len(all_values):
        i += 1
        graph.append({all_values[j - 1] - 1: all_values[j] for j in range(start, all_values[i], 2)})
    return graph

def main():
    all_values = reader('in.txt')
    graph = adjacency_list(all_values)
    #for row in graph: print(row)
    res, weight_sum = solve(graph)
    #for row in res: print(row)
    writer(res + [[weight_sum-1]])

if __name__ == "__main__":
    main()


def make_matrix(graph):
    matrix = []
    for i, edges in enumerate(graph):
        matrix.append([-1] * (len(graph)))
        for j, weight in edges.items():
            matrix[i][j] = weight
    return matrix
