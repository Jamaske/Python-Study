class Prime:
    @staticmethod
    def generate():
        composite_dict = {}
        candidate = 2

        while True:
            if candidate not in composite_dict:
                yield candidate
                composite_dict[candidate * candidate] = [candidate]
            else:
                for prime in composite_dict[candidate]:
                    composite_dict.setdefault(prime + candidate, []).append(prime)
                del composite_dict[candidate]
            candidate += 1    
    gen = generate()

    primes = []
    def get():
        for prime in Prime.primes:
            yield prime
        while(True):
            prime = next(Prime.gen)
            Prime.primes.append(prime)
            yield prime


def factorize(n:int)->dict:
    fatorization = dict()
    prime = Prime.get()
    factor = next(prime)
    while n > 1:
        if factor ** 2 > n:
            fatorization[n] = 1
            break

        power = 0
        while not n%factor:
            n //= factor
            power += 1
        if power: fatorization[factor] = power
        factor = next(prime)
    return fatorization

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a_fact = factorize(a)
    b_fact = factorize(b)
    nod = 1
    bigest_diff = 1
    for fact in a_fact | b_fact:
        pow1 = a_fact.get(fact,0)
        pow2 = b_fact.get(fact,0)
        nod *= fact ** min(pow1, pow2)
        if pow1 - pow2 != 0: bigest_diff = max(bigest_diff, fact)
    print(nod * bigest_diff)