def euler512():
    from sympy.ntheory import totient
    def f(n):
        if n==1: return 1
        return (totient(n)*(pow(n,n)-1)/(n-1))%(n+1)
    out = 0
    for i in xrange(1,500000001):
        if i%100==0: print i
        out+=f(i)
    return out
print euler512()