def euler308():
    from sympy.ntheory import divisors
    def primeGenerate(limit): # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    prime = primeGenerate(150000)
    def f(n):
        l = divisors(n)
        b = l[-2]
        return n-1+(6*n+2)*(n-b)+2*sum([int(float(n)/d) for d in range(b,n)])
    for i in range(2,20):
        print i,f(i)
    a = [None,f(2)]
    n = 2
    while len(a)<10002:
        if len(a)%10==0: print len(a)
        a.append(a[n-1]+sum([f(i) for i in range(prime[n-1]+1,prime[n]+1)]))
        n+=1
    return a[-1]
print euler308()