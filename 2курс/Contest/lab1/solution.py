





def DFS(node:int):
    global graph, colors, notbipart
    curColor = colors[node]
    for next in graph[node]:
        nextColor = colors[next]
        if nextColor == curColor or notbipart: 
            # первое условие для обноружения недвудольностьи второй для выхода из стека вызовов
            notbipart = True
            break
        elif nextColor == -1: #проверка на не посещённость вершины
            colors[next] = not curColor #покраска соседа в противоположный цвет
            DFS(next)
        else:
            continue 
    return 0



with open("in.txt", "r") as file:
    N = int(file.readline())
    graph = []
    for i in range(N):
        row = []
        for j, conected in enumerate(map(int, file.readline().split())):
            if conected:
                row.append(j)
        graph.append(row)


colors = [-1] * N #-1 for unvisited, 0,1 for colors
colors[0] = 0
notbipart = False #т.е. по умолчанию двудольный, пока не докажем обратного
DFS(0)

with open("out.txt", "w") as file:
    if(notbipart):
        file.write("N")
    else:
        file.write("Y\n")
        FirstPart = []
        SecondPart = []
        for i, color in enumerate(colors):
            if(not color):
                FirstPart.append(i+1)
            else:
                SecondPart.append(i+1)
        file.write(' '.join(map(str, FirstPart)) + '\n')
        file.write(' '.join(map(str, SecondPart)))
