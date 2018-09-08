def euler357():
    from sympy import divisors
    def primeGenerate(limit): # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    def is_prime(p):
        if p<2: return False
        if p==2: return True
        for i in range(2,int(p**0.5)+2):
            if p%i==0:
                return False
        return True
    def check(n):
        for d in divisors(n):
            if not(is_prime(d+n/d)):
                return False
        return True
    primes = primeGenerate(100000000)
    out = []
    for p in primes:
        if p%1000==1: print p
        if check(p-1):
            out.append(p-1)
    return sum(out)
print euler357()