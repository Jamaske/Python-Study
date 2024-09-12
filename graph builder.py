
class Work:
    def __init__(self, time, cost, STime, SCost, workers):
        self.time = time
        self.cost = cost
        self.STime = STime
        self.SCost = SCost
        self.workers = workers
        self.costTimeSlope = (SCost - cost) / (time - STime)
    
    def __repr__(self):
        return f"Time {self.time}, Cost {self.cost}, Short time {self.STime}, Short cost {self.SCost}, Worker count {self.workers}"


workList = {
    "A":Work(3,9,2,10,5),
    "B":Work(5,16,1,23,4),
    "C":Work(6,7,4,9,9),
    "D":Work(9,20,6,22,4),
    "E":Work(7,10,2,11,2),
    "F":Work(2,10,1,12,1),
    "G":Work(6,18,3,19,2),
    "H":Work(9,21,3,24,4),
    "I":Work(4,12,1,14,1),
    "J":Work(6,14,2,16,1),
    "K":Work(7,9,1,13,5),
}

WorkerLimit = 11
Budget = 17000
DaylySpendings = 65

#без строки исоднывми работами
INP='''\
F:H B
A:J
G:I
H:E
B I J:C K
E C:D\
'''

statments = [statment.split(":") for statment in INP.split("\n")]

Tasks = dict()#  {work_lable:[start_event, end_event]}
for i, statment in enumerate(statments):
    left, right = map(lambda x: x.split(), statment)
    for lable in left:
        Tasks.setdefault(lable, [0, -1])[1] = i + 1
    for lable in right:
        Tasks.setdefault(lable, [0, -1])[0] = i + 1
    size = i + 2

succeser  = [{} for i in range(size)]
predicesser = [{} for i in range(size)]
for lable, events in Tasks.items():
    succeser [events[0]][events[1]] = workList[lable]
    predicesser[events[1]][events[0]] = workList[lable]

for i in range(size):
    print(succeser[i])







    
