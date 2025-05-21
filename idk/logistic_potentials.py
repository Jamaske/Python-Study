H = 4 # hight
W = 5 # width
a = [4,6,10,10]
b = [7,7,7,7,2]

c = [
    [16,30,17,10,16],
    [30,27,26, 9,23],
    [13, 4,22, 3, 1],
    [ 3, 1, 5, 4,24],
]

f = [[0] * W for _ in range(H)]

#under the hood realization
tree = [

]
# left-top edge flow initialization method
tp = [0] * W
rp = [0] * H
i = j = 0
rc = a[0]
tc = b[0]
if rc < tc:
    tp[0] = c[0][0]
else:
    rp[0] = c[0][0]

while True:
    if rc < tc:
        f[i][j] = rc
        tc -= rc
        i += 1
        rp[i] = c[i][j] - tp[j]
        rc = a[i]
    elif tc < rc:
        f[i][j] = tc
        rc -= tc
        j += 1
        tp[j] = c[i][j] - rp[i]
        tc = b[j]
    else:
        f[i][j] = rc#=y
        i += 1
        j += 1
        if i == H: break
        #if j == W: break
        rc = a[i]
        tc = b[j]

pad = 4
def print_mat(mat:list[list], rgh:list = None, top:list = None, bot:list = None, lft:list = None, name:str = None)->None:
    width = ((pad + 1) * (W + (lft is not None)) + (rgh is not None) * pad)
    if name is not None:
        half = width - len(name) - 2
        print(f"\n{'=' * (half // 2)} {name} {'=' * ((half + 1) // 2)}")
    else:
        print(f"\n{'=' * width}")
    if top is not None:
        if lft is not None:
            print(f"{' '*pad}", end = '|')
        for el in top: print(f"{el:{pad}}", end = '|')
        print(f"\n{'-' * width}")
    for i, row in enumerate(mat):
        if lft is not None:
            print(f"{lft[i]:{pad}}", end = '|')
        for el in row: print(f"{el:{pad}}", end = '|')
        if rgh is not None:
            print(f"{rgh[i]:{pad}}", end = '')
        print()
    if bot is not None:
        print(f"{'-' * width}")
        if lft is not None:
            print(f"{' '*pad}", end="|")
        for el in bot: print(f"{el:>{pad}}", end = '|')
        print()

print_mat(f, lft = a, top = b, name = "Flow")
print_mat(c, lft = rp, top = tp, name = "Potentials")


# use modified potentials to normalize costs
print("\nnormalize potentials and select smallest")

m = 0
im = jm = 0
for i, y in enumerate(rp):
    for j, x in enumerate(tp):
        c[i][j] -= y + x
        if c[i][j] < m:
            m = c[i][j]
            im = i
            jm = j

tp = [0] * W
rp = [0] * H


bot = [""]* W
bot[jm]= "^"
rgh = [""]* H
rgh[im] = "<"
print_mat(c, lft = rp, top = tp, name = "Potentials", bot = bot, rgh=rgh)



