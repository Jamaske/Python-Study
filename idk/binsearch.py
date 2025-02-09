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


#Driver Code

#a = [1,1,1,1,1,1,1,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
a = sorted([randint(0, 1e4) for _ in range(32)])
a.sort()

idx = randint(0, len(a) - 1)
find = a[idx]
print(f"\nfind {find} at index {idx}\n")

search_ac(a, find)
#search_lo(a, 3)
interp(a, find)


