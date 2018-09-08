def euler407():
    M = lambda n: max([a for a in range(n) if (a*a)%n==a%n])
    out = 0
    for i in xrange(1,10**7+1):
        out+=M(i)
        if i%10000==0: print i
    return out
print euler407()
