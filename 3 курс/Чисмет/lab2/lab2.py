from math import log, sin, log10, log2, ceil

#your function
def f(x):
    #added log range error handling
    try:
        res = log10(x) - 0.13/x
    except Exception:
        print(f'error: log10({x})')
        res = 0
    finally:
        return res

#first derivetive
def f1(x):
    return 1 / (log(10) * x) + 0.13/(x*x)

#second derivetive
def f2(x):
    return -1 / (log(10) * x * x) - 0.065 / (x ** 3)


E = 0.5E-5
m = 0.04
M = 0.7
mE = m * E #exit condition
q = 0.45 #simple iteration bound

#Simple iteration method fi function
def fi(x):
    return 10 ** (0.13/x)


def Dihotomia(a,b):
    global E, m, M, mE, q
    f_a_sign = True if f(a) > 0 else False
    f_b_sign = True if f(b) > 0 else False
    if f_a_sign == f_b_sign:Exception("no root on the segment")

    #Spesial exit condition
    N = ceil(log2( (b - a) / E) - 1)

    #regular exit 
    n = 0
    while (b - a) >=  2 * E:
        c = (a + b) / 2
        f_c_pos = True if f(c) > 0 else False
        if f_a_sign == f_c_pos:
            a = c
        else:
            b = c
        n += 1
    
    c = (a + b) / 2
    return (c, n, N)

def immovable_chord(a, b):
    global E, m, M, mE, q
    f_a_sign = True if f(a) > 0 else False
    f_b_sign = True if f(b) > 0 else False
    f2_a_sign = True if f2(a) > 0 else False
    f2_b_sign = True if f2(b) > 0 else False


    if f_a_sign == f2_a_sign:
        x0 = a
        xn = b
    elif f_b_sign == f2_b_sign:
        x0 = b
        xn = a
    else:
        Exception("Do your research")
    
    n = 0
    while abs(f(xn)) >= mE:
        xn = xn - (f(xn) * (xn - x0)) / (f(xn) - f(x0))
        n += 1

    return (xn, n)

def movable_chord(a, b):
    global E, m, M, mE, q
    f_a_sign = True if f(a) > 0 else False
    f_b_sign = True if f(b) > 0 else False
    f2_a_sign = True if f2(a) > 0 else False
    f2_b_sign = True if f2(b) > 0 else False


    if f_a_sign == f2_a_sign:
        prev = a #trailing point
        cur = b #current point
    elif f_b_sign == f2_b_sign:
        prev = b
        cur = a
    else:
        Exception("Do your research")
    
    n = 0
    while abs(f(cur)) >= mE:
        #print(f'({prev:.4f}, {cur:.4f}) -> ',end = '')
        cur, prev = cur - (f(cur) * (cur - prev)) / (f(cur) - f(prev)), cur
        #print(f'{cur:.4f}')
        n += 1

    return (cur, n)

def Newton(a,b):
    global E, m, M, mE, q
    f_a_sign = True if f(a) > 0 else False
    f_b_sign = True if f(b) > 0 else False
    f2_a_sign = True if f2(a) > 0 else False
    f2_b_sign = True if f2(b) > 0 else False

    if f_a_sign == f2_a_sign:
        xn = a #trailing point
    elif f_b_sign == f2_b_sign:
        xn = b
    else:
        Exception("Do your research")

    #i've derived it from r_n < r_(n-1)^2 from the theory
    k = 0.5 * M / m
    #print(log(k * E), log(k * (b - a)))
    #N = ceil(log2(log(k * E) / log(k * (b - a))))

    n = 0
    while abs(f(xn)) >= mE:
        xn = xn - f(xn) / f1(xn)
        n += 1
    
    return  (xn, n)

def Parabola(a,b):
    global E, m, M, mE, q
    # i chose left side. cry about it
    xn = a
    n = 0
    while abs(f_xn := f(xn)) >= mE:
        f1_xn = f1(xn)
        if(f_xn > 0):
            root = (f1_xn**2 + 2 * M * f_xn)**0.5
            # xn = xn + (+f1_xn + root) / M
            xn = xn - 2 * f_xn / (f1_xn - root)
        else:
            root = (f1_xn**2 - 2 * M * f_xn)**0.5
            # xn = xn + (-f1_xn + root) / M
            xn = xn - 2 * f_xn / (f1_xn + root)
        n += 1
    
    return (xn, n)

def SimpleIteration(a,b):
    global E, m, M, mE, q
    #cheack your bounds
    # any point should do
    xn = (a + b) / 2
    N = ceil(log(E / (b - a)) / log(q))
    n = 0
    while abs(f(xn)) >= mE:
        xn = fi(xn)
        n += 1
    
    return (xn, n, N)

    


def main():
    #comon segment bounds
    a, b = 1, 10
    results = [
        Dihotomia(a, b),
        immovable_chord(a,b),
        movable_chord(a,8),
        Newton(a,b),
        Parabola(a,b),
        SimpleIteration(a,b)
    ]
    for i in results: print(i)

if __name__ == "__main__": main()
    



