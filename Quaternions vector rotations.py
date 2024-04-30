x, y, z = 1,2,3
print("  X       Y        Z   ")
print(f'{x:+.1f}  {y:+.1f}  {z:+.1f}')

side_names= ['0','+a','+b','+c','-c','-b', '-a']

#print("  X       Y        Z   ")
print(f'{x:+.1f}  {y:+.1f}  {z:+.1f}')
#print(" X  Y  Z")
print(f'{side_names[x]}  {side_names[y]}  {side_names[z]}')
def rotate(a, b, c):
    """
    rotate vectore (x,y,z) by 90 degrees by (a,b,c) axis
    condition |a,b,c| = 1
    """
    global x,y,z
    x, y, z = (
    ((x+a*a*x-b*b*x-c*c*x)+(2*a*b*y-2*c*y)+(2*a*c*z+2*b*z))/2,
    ((2*a*b*x+2*c*x)+(y-a*a*y+b*b*y-c*c*y)+(2*b*c*z-2*a*z))/2,
    ((2*a*c*x-2*b*x)+(2*b*c*y+2*a*y)+(z-a*a*z-b*b*z+c*c*z))/2
    )

def rotate2(a, b, c):
    """
    rotate vectore (x,y,z) by 90 degrees by (a,b,c) axis
    conditions
    |a,b,c| = 1
    ab=ac=bc=0
    (only one of the a,b,c triple is not zerro)
    """
    global x,y,z
    x, y, z = (
        (x*(1+abs(a)-abs(b)-abs(c)) + 2*b*z - 2*c*y)/2,
        (y*(1-abs(a)+abs(b)-abs(c)) - 2*a*z + 2*c*x)/2,
        (z*(1-abs(a)-abs(b)+abs(c)) + 2*a*y - 2*b*x)/2
        )

def rotate3(a, b):
    """
    rotate vectore (x,y,z) by 90 degrees by (a,b,c) axis
    conditions
    |a,b| = 1
    ab=0; c = 0
    (only one of the a,b pair is not zerro)
    """
    global x,y,z
    x, y, z = (
        (abs(a)*x + b*z),
        (abs(b)*y - a*z),
        (a*y - b*x)
        )
    
while True:
    rotate3(*map(int, input().split()))
    #print(f'{x:+.1f}  {y:+.1f}  {z:+.1f}')
    print(f'{side_names[x]}  {side_names[y]}  {side_names[z]}')
    
    
