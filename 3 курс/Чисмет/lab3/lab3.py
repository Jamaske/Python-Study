import FixPoint as FP
from Expression import Expression as EXP


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
        for diag in range(self.m):
            #column calculations b_ij
            j = diag
            for i in range(diag, self.h):
                #BUG sum and generator inside do not work preperly. Just return int(0). So exp is a_ij - 0
                exp = self.data[i][j] - sum((self.data[i][k] * self.data[k][j] for k in range(j)))
                exp.steps()
                exp.flush()
                self.data[i][j] = exp

            #row calculations c_ij
            i = diag
            for j in range(diag + 1, self.w):
                exp = (self.data[i][j] - sum((self.data[i][k] * self.data[k][j] for k in range(i)))) / self.data[i][i]
                exp.steps()
                exp.flush()
                self.data[i][j] = exp
    


FP2 = FP.Template(2)
data = [1.2345, 3.1415, 1, 11.6175, 2.3456, 5.9690, 0, 14.2836, 3.4567, 2.1828, 3, 20.1223]
solution = Gaus(3,4, source=list(map(EXP, map(FP2, data))))
solution.forward()