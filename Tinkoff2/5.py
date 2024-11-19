def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

start_time = input()
start_sec = time_to_sec(start_time)

def time_diff(time):
    sec = time_to_sec(time)
    return sec - start_sec + 86400 * (sec < start_sec) 


#{team : {server : [(sec, succes)]}}

data = {}
n = int(input())
for i in range(n):
    team, time, server, result = input().split(' ')
    if result == "PONG":continue
    succes = (result == "ACCESSED")
    data.setdefault(team, {}).setdefault(server, []).append((time_diff(time), succes))


scores = []
for team, team_data in data.items():
    hacked_servers = 0
    penalty = 0
    for server, requests in team_data.items():
        errors = 0
        requests.sort(key = lambda x: x[0])
        for sec, succes in requests:
            if succes:
                hacked_servers += 1
                penalty = errors * 20 + sec // 60
                break
            else:
                errors += 1
    scores.append((team, hacked_servers, penalty))

#сортировка в питоне обладает свойством стабильности
#после нескольких сортировок основной порядок задаётся последней из них
#но благодоря стабильности остаточная упорядоченность от прошлых всё ещё останется
scores.sort(key = lambda x:x[0]) # третий
scores.sort(key = lambda x:x[2]) # второй
scores.sort(reverse = True,key = lambda x:x[1]) # первый приоритет

place = 1
print(place, *scores[0])
old = scores[0][1:]

for i, score in enumerate(scores[1:]):
    if old != score[1:]:place = i + 2
    old = score[1:]
    print(place, *score)