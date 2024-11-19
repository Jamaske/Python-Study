from collections import deque

N, M, q = map(int, input().split())

remain_parts = []
indexes = [[0] * M for i in range(N)]

grid = [input() for i in range(N)]

def dfs(x, y, grid):    
    if x < 0 or M <= x or y < 0 or N <= y or indexes[y][x] > 0: return
    if grid[y][x] == '.': return

    remain_parts[-1].add((x,y))
    indexes[y][x] = len(remain_parts)

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        dfs(x + dx, y + dy, grid)
    

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'X' and indexes[y][x] == 0:
            remain_parts.append(set())
            dfs(x,y, grid)


#for i in remain_parts:print(i)
#for i in indexes: print(i)


for i in range(q):
    y, x = map(int, input().split())
    
    ship_num = indexes[y-1][x-1]
    #print(x, y, ship_num)
    if ship_num:
        parts = remain_parts[ship_num-1]
        parts.remove((x-1,y-1))
        if(parts): print("HIT")
        else: print("DESTROY")
    else:
        print("MISS")

