def euler421():
    def primeGenerate(limit): # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    import time
    start = time.time()
    primes = primeGenerate(10**8)
    print len(primes)
    end = time.time()
    print end-start
    def primRoots(theNum): # https://stackoverflow.com/a/48442076
        o = 1
        roots = []
        r = 2
        while r < theNum:
            if len(roots)>0:
                return roots
            k = pow(r, o, theNum)
            while (k > 1):
                o = o + 1
                k = (k * r) % theNum
            if o == (theNum - 1):
                roots.append(r)
            o = 1
            r = r + 1
    out = []
    start = time.time()
    for p in primes:
        out.append((p, primRoots(p)))
        if p%100==1: print p
    end = time.time()
    print end-start
print euler421()