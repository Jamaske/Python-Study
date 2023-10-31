def simples():
    i = 2
    while True:
        for j in range(2, i):
            if i % j == 0: break
        else: yield i
        i += 1


iter = simples()
for i in range(10):
    print(next(iter))
