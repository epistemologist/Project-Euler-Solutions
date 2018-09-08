def euler231():
    global primes

    def prime_generate(limit):  # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            print (n, int(limit**0.5+1.5))
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    primes = prime_generate(2*10**7)
    def legendre(n, p):
        out = 0
        i = 1
        while int(float(n)/(p**i)) > 0:
            out += int(float(n)/(p**i))
            i += 1
        return out

    def prime_factor_factorial(n):
        out = {}
        for p in primes:
            if p%100==11: print p
            out[p] = legendre(n, p)
        return out
    import time
    from collections import Counter
    start = time.time()
    a = prime_factor_factorial(2*10**7)
    b = prime_factor_factorial(15*10**6)
    c = prime_factor_factorial(5*10**6)
    for i in b:
        b[i]*=-1
    for i in c:
        c[i]*=-1
    d = Counter(a)+Counter(b)+Counter(c)
    out = 0
    for i in d:
        out+=i*d[i]
    print out
    end = time.time()
    return end-start


print euler231()
