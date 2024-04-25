n = int(input())
# 1 for to king vonversion, -1 for knight konversion, 0 for no tokens
tokens = []
# each cell contains two number - distance to get there as a knight and as a king
unvisited = []

for x in range(n):
    unvisited.append([])
    tokens.append([])
    for y, cell in enumerate(input()):
        unvisited[x].append([True,True]) # default mark unvisited
        tokens[x].append(-1) # default no tokens
        match cell:
            case 'S':
                start = (x,y, 0)
                unvisited[x][y] = (False,True)
            case 'F':
                fin_x, fin_y = x,y
            case 'K':
                tokens[x][y] = 0
            case 'G':
                tokens[x][y] = 1
            

# font consists of 3d coorinates (x, y, pice)
front, next_front, dist = [start], [], 0
undone = True
while front and undone:

    for x, y, pice in front:
        
        if pice: # King pice moves
            move_table = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1, -1))
        else: # Knight  pice moves
            move_table = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))

        for mx, my in move_table:
                nx = x + mx
                if nx < 0 or n <= nx: continue
                ny = y + my
                if ny < 0 or n <= ny: continue
                if nx == fin_x and ny == fin_y:
                    undone = False
                    break
                if tokens[nx][ny] == -1:# not 0
                    npice = pice
                else:
                    npice = tokens[nx][ny]
                    
                if unvisited[nx][ny][npice]:
                    unvisited[nx][ny][npice] = False
                    next_front.append((nx, ny, npice))
        else:
            continue
        break

    front, next_front, dist = next_front, [], dist + 1

if undone:
    print(-1)
else:
    print(dist)

