from visual import preaty
from random import randint

@preaty
def search_ac(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2

        # Чтобы логирывать каждую итерацию необходимо выполнять код изнутри поиска
        # Его можно было бы скрыть в классе масива или классе чисел, но я не стал пееусложнять.
        logger((l, r, m))

        if arr[m] < value:
            l = m + 1
        else:
            r = m
    return l

@preaty
def search_dc(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r + 1) // 2

        logger((l,r,m))

        if arr[m] <= value:
            l = m
        else:
            r = m - 1
    return l

@preaty
def interp(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        lv = arr[l]
        hv = arr[r]
        dif = hv -lv
        
        if dif:
            #base linear aproximation
            m = l + (r - l) * (value - lv) // (hv - lv)
            #stricter formula for infinete loop prevention
            #C = 1.05
            #m = int(((l+r) + (2*value - (hv + lv)) * (r - l) / (C * dif))/2)
        else:
            m = (l + r) // 2

        logger((l, r, m))

        mv = arr[m]
        if mv == value:
            return m
        elif  mv < value:
            l = m + 1
        else:
            r = m - 1
    return l

@preaty
def interp2(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    lv = arr[l]
    rv = arr[r]
    arr.extend([1e4, -1e4])

    while l <= r:
        dif = rv -lv
        if dif: 
            p = l + ((r - l) * (value - lv) + dif >> 1) // dif
            if p < l or r < p:
                arr.pop()
                arr.pop()
                return l if p < l else r
        else:
            p = (l + r) // 2

        print(p)
        logger((l, r, p))

        pv = arr[p]
        if pv == value:
            arr.pop()
            arr.pop()
            return p
        elif  pv < value:
            l = p + 1
            lv = arr[l]
            #if value < lv:
            #     return l
        else:
            r = p - 1
            rv = arr[r]
            # if rv < value:
            #     return r
    arr.pop()
    arr.pop()
    if value - rv <= lv - value:
        return r
    else:
        return l 


#Driver Code

#a = [1,1,1,1,1,1,1,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
a = sorted([randint(0, 1e2) for _ in range(32)])
a.sort()

idx = randint(0, len(a) - 1)
find = a[idx]
print(f"========= data generated ===========\n\nfind {find} at index {idx}\n")

#find = randint(0, 1e3)
#print(f"========= data generated ===========\n\nfind {find} \n")


search_ac(a, find)
interp2(a, find)


