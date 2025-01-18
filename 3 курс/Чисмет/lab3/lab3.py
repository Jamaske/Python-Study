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

FP2 = FP.Template(2)
FP4 = FP.Template(4)
FP6 = FP.Template(6)

data_FP2 = list(map(lambda row: list(map(FP2, row)), data))
data_FP4 = list(map(lambda row: list(map(FP4, row)), data))
data_FP6 = list(map(lambda row: list(map(FP6, row)), data))

# Convert each element to an Expression
data_FP2 = list(map(lambda row: list(map(EXP, row)), data_FP2))
data_FP4 = list(map(lambda row: list(map(EXP, row)), data_FP4))
data_FP6 = list(map(lambda row: list(map(EXP, row)), data_FP6))
print("===Gaus with out chose===")
print("\n2 digits\n")
Gaus(3, 4, source=copy(data_FP2), correct=correct_ans, chose=False).solve()
print("\n4 digits\n")
Gaus(3, 4, source=copy(data_FP4), correct=correct_ans, chose=False).solve()
print("\n6 digits\n")
Gaus(3, 4, source=copy(data_FP6), correct=correct_ans, chose=False).solve()


print("===Gaus with chose===")
print("\n2 digits\n")
Gaus(3, 4, source=data_FP2, correct=correct_ans, chose=True).solve()
print("\n4 digits\n")
Gaus(3, 4, source=data_FP4, correct=correct_ans, chose=True).solve()
print("\n6 digits\n")
Gaus(3, 4, source=data_FP6, correct=correct_ans, chose=True).solve()

