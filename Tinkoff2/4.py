powers = [2, 4, 6, 10, 12, 16, 18, 22, 28, 30, 36, 40, 42, 46]
pow_diff = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4]

l,r = map(int, input().split())
counter = 0

def prime_seq():
    yield 2
    yield 3
    prime = 3
    for half_diff in half_prime_diffs:
        prime += half_diff << 1
        yield prime
        
for power in powers:
    primes = prime_seq()
    for prime in primes:
        n = prime ** power
        if r<n:break
        #print(n)
        counter += (l<=n)
print(counter)