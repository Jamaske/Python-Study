
with open("in.txt", "r") as file:
    N = int(file.readline())
    graph = [[] for i in range(N)] #ajaisent 
    weights = {} # map with key:value = edge:weight
    for i in range(N):
        line = map(int, file.readline().split())
        for j in line:
            if (j):#if j is a vertex rather then line terminating 0
                graph[j-1].append(i)
                weights[(j-1,i)] = next(line)

print(graph)
print(weights)

#with open("out.txt", "w") as file: file.write(out)