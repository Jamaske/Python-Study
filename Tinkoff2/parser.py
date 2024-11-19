primes = []
with open("P-1000000.txt") as file:
    for line in file:
        _, prime, diff = map(int,line.split(", "))
        if prime > 10**7:break
        primes.append(str(diff // 2))


with open("half_diffs_from5.txt", "w") as file:
    file.write('['+",".join(primes)+']')
