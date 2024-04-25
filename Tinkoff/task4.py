#action seaquence to rotate matrix cycle by one
def right(x,y):
    global n
    print(f'{x} {y} {n-y} {x}\n{n-y} {x} {n-x} {n-y}\n{n-x} {n-y} {y} {n-x}')

def left(x,y):
    global n
    print(f'{x} {y} {y} {n-x}\n{y} {n-x} {n-x} {n-x}\n{n-x} {n-y} {n-y} {x}')


n,rotate = (lambda x: (int(x[0]) - 1, {"R":right, "L":left}[x[1]]) )(input().split())

#ignore matrix values
for i in range(n + 1):
    input()

#rotation algorithm for arbitrary matrix
print((n+1)**2//4*3)
for x in range((n+2)//2):
    for y in range((n+1)//2):
        rotate(x,y)