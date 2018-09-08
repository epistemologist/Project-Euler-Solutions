def euler221():
    from sympy.ntheory import divisors
    def A147811(p):
        return set([p*(p+d)*(p+(p*p+1)/d) for d in divisors(p*p+1)])
    alexandrian_ints = set()
    i=0
    while len(alexandrian_ints)<150001:
        if i%100==0: print i, len(alexandrian_ints)
        alexandrian_ints = alexandrian_ints.union(A147811(i))
        i+=1
    print len(alexandrian_ints)
    alexandrian_ints = sorted(alexandrian_ints)
    print alexandrian_ints[0:100]
    print alexandrian_ints[149990:]
print euler221()