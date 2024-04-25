n = int(input())
FS = {}

for i in range(n):
    global path
    path = input().split('/')
    Dir = FS
    for folder in path[1:]:
        Dir = Dir.setdefault(folder, {})

root = path[0]

depth = 0
def tree_treverse(Dir):
        global depth
        if not Dir:return
        depth += 1
        for folder_name, sub_folders in sorted(Dir.items(),key = lambda x: x[0]):
            print('  '*depth, folder_name, sep="")
            tree_treverse(sub_folders)
        depth -=1
print(root)
tree_treverse(FS)