day_n = int(input())
depth_seq = map(int, input().split())

cur_depth = 0
result_delatas = []
for measurement in depth_seq:
    if measurement == -1: #skip carupted value and print "1" delta 
        cur_depth += 1
        result_delatas.append(1)
    elif  cur_depth < measurement: 
        result_delatas.append(measurement - cur_depth)
        cur_depth = measurement
    else: #Data is rigged. Big lie if reveald.
        print("NO")
        break
else:
    print("YES")
    print(" ".join(map(str, result_delatas)))