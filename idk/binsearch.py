from visual import preaty

@preaty
def search_hi(arr:list, value:int, logger = None) -> int:
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
def search_lo(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2

        logger((l,r,m))

        if arr[m] <= value:
            l = m
        else:
            r = m - 1
    return l


a = [1,1,1,1,1,1,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

search_hi(a, 2)
search_lo(a, 2)


