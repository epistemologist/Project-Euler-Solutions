def euler365():
    from math import factorial
    import itertools
    def is_prime(p):
        for i in range(2,int(p**0.5)+2):
            if p%i==0: return False
        return True
    def base_b_expansion(n,b):
        out = []
        while n>0:
            out.append(n%b)
            n/=b
        return out[::-1]
    def ncr(n,k):
        if n<k: return 0
        else: return factorial(n)/factorial(k)/factorial(n-k)
    def ncr_mod_p(n,k,p):
        n_ = base_b_expansion(n,p)
        k_ = base_b_expansion(k,p)
        while len(n_)<len(k_):
            n_ = [0] + n_
        while len(k_)<len(n_):
            k_ = [0] + k_
        out = 1
        for i in range(len(n_)):
            out*=ncr(n_[i],k_[i])
        return out
    def xgcd(a,b):
        # returns tuple (g,x,y) such that a*x+b*y=g=gcd(x,y)
        a,b=b,a
        x0, x1, y0, y1 = 1, 0, 0, 1
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0, y0
    def crt(a1,a2,n1,n2):
        """
        solves system
        x = a1 mod n1
        x = a2 mod n2
        """
        # Calculate Bezout coefficients
        _,m1,m2 = xgcd(n1,n2)
        return a1*m2*n2+a2*m1*n1
    def crt2(a,n):
        """
        solves system
        x = a_i mod n_i for all i
        """
        temp_a = crt(a[0],a[1],n[0],n[1])
        temp_n = n[0]*n[1]
        for i in range(2,len(a)):
            temp_a = crt(temp_a,a[i],temp_n,n[i])
            temp_n *= n[i]
        return temp_a%temp_n
    primes = [i for i in range(1000,5000) if is_prime(i)]
    primes_mod = {}
    for p in primes:
        primes_mod[p] = ncr_mod_p(10**18,10**9,p)
    out = 0
    for i in itertools.combinations(primes,3):
        print i
        p = i[0]
        q = i[1]
        r = i[2]
        out+=crt2([primes_mod[p],primes_mod[q],primes_mod[r]],[p,q,r])
    return out
print euler365()