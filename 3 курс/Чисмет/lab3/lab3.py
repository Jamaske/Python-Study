import FixPoint as FP
from Expression import Expression as EXP
from pprint import pprint

def sub(iterable, start=0):
    for val in iterable:
        start -= val
    return start

class Gaus:

    def __init__(self, hight, width, source = None):
        self.h = hight
        self.w = width
        self.m = min(hight, width)
        self.M = max(hight, width)
        self.data = [[None] * width for i in range(hight)]
        if source is not None:
            k = 0
            for i in range(hight):
                for j in range(width):
                    self.data[i][j] = source[k]
                    k += 1
    
    def __getitem__(self, index):
        return self.data[index] #return whole row for second index resolving

    def forward(self):
        print("forward step")
        for diag in range(self.m):
            #column calculations b_ij
            j = diag
            for i in range(diag, self.h):
                exp = sub((self.data[i][k] * self.data[k][j] for k in range(j)), start = self.data[i][j])
                print(f'b_{i}{j} = {exp.steps()}')
                exp.flush()
                self.data[i][j] = exp

            #row calculations c_ij
            i = diag
            for j in range(diag + 1, self.w):
                exp = sub((self.data[i][k] * self.data[k][j] for k in range(i)), start = self.data[i][j]) / self.data[i][i]
                print(f'c_{i}{j} = {exp.steps()}')
                exp.flush()
                self.data[i][j] = exp
    
    def backward(self):
        print("backward step")
        last_col = self.w - 1
        for i in range(self.h-1, -1, -1):
            exp = sub((self.data[i][j] * self.data[j][last_col] for j in range(self.h-1, i,-1)) , start=self.data[i][last_col])
            print(f'x_{i} = {exp.steps()}')
            exp.flush()
            self.data[i][last_col] = exp




FP2 = FP.Template(6)
data = [1.2345, 3.1415, 1, 11.6175, 2.3456, 5.9690, 0, 14.2836, 3.4567, 2.1828, 3, 20.1223]
solution = Gaus(3,4, source=list(map(EXP, map(FP2, data))))
solution.forward()
pprint(solution.data)
solution.backward()
pprint(solution.data)

