n = int(input())
time_req = [None] * n
start_time = [0] * n
depend_list = [None] * n
cur_front = []
adjacency_list = [[] for i in range(n)]
for node in range(n):
    time, *dependencis = map(int, input().split())
    dependencis = list(map(lambda x: x- 1, dependencis))
    time_req[node] = time
    depend_list[node] = set(dependencis)
    if not dependencis:
        cur_front.append(node)
    for source in dependencis:
        adjacency_list[source].append(node)

max_time = 0
while cur_front:
    cur = cur_front.pop()
    end_time = start_time[cur] + time_req[cur]
    max_time = max(max_time, end_time)
    for node in adjacency_list[cur]:
        if start_time[node] < end_time: start_time[node] = end_time
        
        depend_list[node].remove(cur)
        if not depend_list[node]:
            cur_front.append(node)
        

print(max_time)
