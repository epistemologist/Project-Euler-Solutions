def euler347():
    from math import log
    def primeGenerate(limit): # from rosettacode
        is_prime = [False] * 2 + [True] * (limit - 1)
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    primes = primeGenerate(10000)
    out = 0
    for m in range(len(primes)):
        for n in range(m,len(primes)):
            p = primes[m]
            q = primes[n]
            if q%10000==1: print p,q
            if p>q:
                flag = False
            max_p_exp = int(log(10**7,p))+1
            for i in range(1,max_p_exp):
                j = int(log(10**7/pow(p,i),q))
                temp = pow(p,i)*pow(q,j)
                if temp<10**7 and temp>out:
                    out = temp
    return out
            
print euler347()