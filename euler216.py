def euler216():
    from sympy import isprime
    from math import log

    def mod_filter(n):
        if n == 2 or n == 3:
            return True
        return not(n % 7 in [2, 5]) and not(n % 17 in [3, 14])

    def miller_rabin(n):
        if n < 2:
            return False
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        if n in small_primes:
            return True
        for i in small_primes:
            if n % i == 0:
                return False
        d = n-1
        s = 0
        while d % 2 == 0:
            d /= 2
            s += 1
        assert n-1 == 2**s*d
        for a in small_primes:
            if pow(a, d, n) != 1 and all([pow(a, 2**r*d, n) != -1 % n for r in range(s)]):
                return False
        return True

    out = 0
    for i in range(2,50000001):
        if i%1000==0: print i
        if mod_filter(i):
            if miller_rabin(2*i*i-1):
                out+=1
    print out

print euler216()
