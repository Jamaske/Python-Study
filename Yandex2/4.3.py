import sys
sys.set_int_max_str_digits(0)
n = int(input())
S = 1

B = 1 #B(0), B(1)
if (n & 1):#perform first iteration k=0, k=1
    A = n - 1 #A-1
    C = n #C(1)
    P = 2 #B(2)

else:#perform half iteration k = 0
    A = 1 #A0
    C = 1 #C(0)
    P = 1 #P(1)

for k in range((n & 1) + 1, n + 1, 2):
    A += - (C := C * (n-k+1) //  k   ) * (B := B *  P)\
         + (C := C * (n-k)   // (k+1)) * (B := B * (P := P << 1))
    P = P << 1


    #print(S * C * B)
print(f"\n{A}")


