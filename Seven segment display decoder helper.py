from itertools import permutations

def evaluate(arr):
    cost = 0
    for i, el in enumerate(arr):
        cost += el * i
    return cost

def orderedness(arr):
    x = evaluate(arr) / sum(arr)
    k = 6*(x+1)/(len(arr)+1)-3
    return k
        


def req_perm(variate_idx):
    global best_cost, best_var, end, arr, max_bits
    
    if variate_idx >= 3 and (arr[variate_idx - 1] | arr[variate_idx - 2] | arr[variate_idx - 3]) < max_bits:
        return # 3 репитора подряд
    elif variate_idx == len(arr):
        if (cur_cost := evaluate(arr)) < best_cost:
            best_cost = cur_cost
            best_var = arr.copy()
            print(best_cost)
            print(best_var, '\n')
        return #нашли норм варик
    elif variate_idx == 2 and (arr[0] | arr[1] < max_bits):
        return #выход по прихоти


    req_perm(variate_idx + 1)
    for i in range(variate_idx + 1, end):
        arr[variate_idx], arr[i] = arr[i], arr[variate_idx] #choose next el
        req_perm(variate_idx + 1)
        arr[variate_idx], arr[i] = arr[i], arr[variate_idx] #revert prev swap for undone any changes

arr = [0,2,3,4,5,6,7,8,9,10,11,12,1]
max_bits = 15
best_cost = 10**4
best_var = []

end = len(arr) - 1
req_perm(0)
soluton1 = [7, 0, 9, 6, 1, 10, 4, 3, 8, 5, 2, 11, 12, 13, 14, 15]# score 1119
soluton2 = [7, 8, 1, 6, 9, 2, 4, 11, 0, 5, 10, 3, 12, 13, 14, 15]# score 1087
soluton3 = [3, 12, 0, 7, 8, 1, 6, 9, 2, 4, 11, 5, 10, 13, 14, 15]# score 1096

print("final result:")
print(f'with score:{best_cost} ({orderedness(arr):.2f} oedered metric)')
print(best_var)
