def euler487():
    from fractions import Fraction
    from math import factorial
    import time
    global B_plus
    global factorial
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
    # STEP 1: primes between 2e9 and 2e9+2000

    primes = []
    for i in xrange(2000000000, 2000002000):
        if miller_rabin(i):
            primes.append(i)

    # STEP 2: calculate tangent numbers

    def tangent(n):
        # https://maths-people.anu.edu.au/~brent/pd/tangent.pdf
        T = [None]*(n+1)
        T[1] = 1
        for k in range(2, n+1):
            T[k] = (k-1)*T[k-1]
        for k in range(2, n+1):
            print "T",(k,n+1)
            for j in range(k, n+1):
                T[j] = (j-k)*T[j-1]+(j-k+2)*T[j]
        return T

    # STEP 3: calculate Bernoulli numbers

    def bernoulli(n):
        B = [None]*(n+1)
        T = tangent(n)
        for i in range(1, len(T)):
            B[i] = Fraction(2*i*T[i], ((-1)**(i-1))*(2**(2*i))*(2**(2*i)-1))
        out = [1, Fraction(1, 2)]
        for i in B:
            if i!=None:
                out.append(i)
                out.append(0)
        return out
    start = time.time()
    B_plus = bernoulli(5000)
    end = time.time()
    print end-start,"bernoulli generated"

    # STEP 4: calculate factorials
    factorial = [1]
    start = time.time()
    for i in range(1,15000):
        if i%100==0: print "f",(i,15000)
        factorial.append(i*factorial[-1])
    end = time.time()
    print end-start,"factorials generated"

    def choose(n,k):
        return factorial[n]/factorial[k]/factorial[n-k]
    
    def f(m,n):
        out = Fraction(0,1)
        for k in range(m+1):
            if k%100==0: print "F",(k,m)
            out+=choose(m+1,k)*B_plus[k]*n**(m+1-k)
        return out/(m+1)
    
    def S(k,n):
        return (n+1)*f(k,n)-f(k+1,n)
    
    out = 0
    s = S(10000,10**12)
    for p in primes:
        out+=(s%p)
    return out

print euler487()
