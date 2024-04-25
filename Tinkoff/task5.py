v1, v2, v3 = 0,0,0
max1, max2, max3 = 0,0,0
tile_val =lambda x: {'W':-1,'.':0, 'C':1}[x]
n = int(input())
total = 0
# O(n) - time
# O(1) - space
# result in single data read
for t1, t2, t3 in (map(tile_val, input()) for i in range(n)):
    v1, v2, v3 = t1 + max1 if t1 != -1 and max1 != -1 else -1,\
                 t2 + max2 if t2 != -1 and max2 != -1 else -1,\
                 t3 + max3 if t3 != -1 and max3 != -1 else -1
    max1 = max(v1,v2)
    max2 = max(v1,v2,v3)
    max3 = max(v2,v3)
    total = max(total, v1, v2, v3)
print(total)