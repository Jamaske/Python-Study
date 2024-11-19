from math import pi

#табличные ряды. B[p] = sum(1/n^p). разбиты на множители, для уменьшения ошибки.
B = [None, None, (pi/2)*(pi/3), 1.2020569032, (pi/2)*(pi/5)*(pi/3)*(pi/3)]

# заменить
# 1) чисо итераций
# 2) слагаемые изветных рядов
# 3) формулу члена ряда
def S_N():
    N = 2 * 10**7
    S = 0
    for n in range(1, N + 1):
        a_n = (n - 1) / (n**3 - 0.15)
        S += a_n
    print(f'{N = }\nS = sum(a_n) = {S:.20f}\n')

def S_M():
    S = B[2]
    M = 3163
    P = 0
    for n in range(1, M + 1):
        p_n = -(n**2 - 0.15) / n**2 / (n**3 - 0.15)
        P += p_n
    S += P
    print(f'{M = }\nP = sum(p_n) = {P:.20f}\nS = B1 + P = {S:.20f}\n')

def S_L():
    S = B[2] - B[3]
    L = 30
    Q = 0
    for n in range(1, L + 1):
        q_n = 0.15 * (n - 1) / n**3 / (n**3 - 0.15)
        Q += q_n
    S += Q
    print(f'{L = }\nQ = sum(q_n) = {Q:.20f}\nS = B1 + B2 + Q = {S:.20f}\n')


S_N()
S_M()
S_L()
input()