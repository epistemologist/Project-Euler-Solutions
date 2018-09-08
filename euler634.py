def euler634(lim=9*(10**18)):
    out=0
    sqrt = lambda x: int(x**0.5)
    cbrt = lambda x: int(x**(1./3))
    for b in xrange(2,(cbrt(int(lim/4)))+1):
        #print b
        for a in xrange(2,sqrt(int(lim/(b**3)))+1):
            #if a%1000000==0: print b,a
            # = a*a*b*b*b
            out+=1
    return (out)
for i in range(10,1000):
    print i,euler634(i)