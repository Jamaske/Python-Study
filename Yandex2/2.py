n = int(input())
teams = [None] * n
indexes = [None] * n
cur_distrebuted = 0
derive = [None] * 200
for i in range(n):
    size, *team = map(int, input().split())
    mid = size >> 1
    teams[i] = sorted(team)
    indexes[i] = mid

    cur_distrebuted += team[size >> 1]
    for j , el in teams[i]:
        derive[j - mid] += el
T = int(input())


print(cur_distrebuted)