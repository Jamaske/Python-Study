


def BFS_lazy(start, target, adjacent_func):
    """
    Broad First Search
    takes id's of start and target vertices - start, target
    and function witch returns all adjacent vertices to a given one
    """
    cur_front = [start]
    next_front = [] 
    tree = {start: None} #dict with child, parent pairs
    for dist in range(1,5):
        print(f"search distance {dist}")
        for vert in cur_front:
            for adjacent in adjacent_func(vert):
                if adjacent in tree: continue
                next_front.append(adjacent)
                tree[adjacent] = vert
                if adjacent == target: break
            else: continue
            print("target reached")
            return tree, dist
        cur_front, next_front = next_front, []
    print("out of range")
    return tree, None

def BFS(start, target, adjacent_func):
    """
    Broad First Search
    takes id's of start and target vertices - start, target
    and function witch returns all adjacent vertices to a given one
    """
    cur_front = [start]
    next_front = [] 
    tree = {start: None} #dict with child, parent pairs
    for dist in range(1,5):
        print(f"search distance {dist}")
        for vert in cur_front:
            for adjacent in adjacent_func(vert):
                if adjacent in tree: continue
                next_front.append(adjacent)
                tree[adjacent] = vert
        
        if target in tree:
            print("target reached")
            return tree, dist
        else:
            cur_front, next_front = next_front, []  
    print("out of range")
    return tree, None

def TreeNodeToRootPath(tree, node):
    path = []
    while node != None:
        path.append(node)
        node = tree[node]
    return path



if __name__ == "__main__":

    def test_grapth(vert):
        return [
            [1,2],
            [2,4],
            [0,3],
            [0],
            [1],
        ][vert]

    start = 4
    target = 2
    ret, dist = BFS_lazy(start, target, test_grapth)
    path = TreeNodeToRootPath(ret, target)
    print(ret)
    print(dist, path)
