def euler545():
    global primes
    def prime_generate(limit):  # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            print (n,int(limit**0.5+1.5))
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    primes = prime_generate(10000000)
    def denom_bernoulli(n):
        assert n%2==0
        out = 1
        for p in primes:
            if n%(p-1)==0: out*=p
            if p>n: break
        return out
    for n in range(2,1000000,2):
        if denom_bernoulli(n)==20010: print n,n/308
print euler545()
