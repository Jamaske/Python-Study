
N = int(input())
graph = []
for i in range(N):
    row = []
    for j, conected in enumerate(map(int, input().split())):
        if conected:
            row.append(j)
    graph.append(row)



colors = [-1] * N #-1 for unvisited, 0,1 for colors
notbipart = False

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

colors[0] = 0
DFS(0)

if(notbipart):
    print("N")
else:
    print("Y")
    SecondPart = []
    for i, color in enumerate(colors):
        if(not color):print(i+1, end=' ')
        else:SecondPart.append(i+1)
    print('\n'+' '.join(map(str, SecondPart)))
