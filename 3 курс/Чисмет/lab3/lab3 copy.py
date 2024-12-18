import FixPoint as FP
from Expression import Expression as EXP
from GaussianElimination import GaussianElimination as Gaus
from copy import deepcopy as copy

data = [
    [1.2345, 3.1415, 1, 11.6175,],
    [2.3456, 5.9690, 0, 14.2836,],
    [3.4567, 2.1828, 3, 20.1223,],
]


correct_ans = [
    [1, 2, 4.1],
]
n = 3
FP = FP.Template(n)
data_FP = list(map(lambda row: list(map(FP, row)), data))

# Convert each element to an Expression
data_FP = list(map(lambda row: list(map(EXP, row)), data_FP))

print(f"\n{n} digits\n")
#print("===Gaus with out chose===")
#Gaus(3, 4, source=copy(data_FP), correct=correct_ans, chose=False).solve()

print("===Gaus with chose===")

Gaus(3, 4, source=data_FP, correct=correct_ans, chose=True).solve()



