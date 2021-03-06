def euler500():
    import math
    def primeGenerate(limit): # from rosettacode
	        is_prime = [False] * 2 + [True] * (limit - 1)
	        for n in range(int(limit**0.5 + 1.5)):
		        if is_prime[n]:
			        for i in range(n*n, limit+1, n):
				        is_prime[i] = False
	        return [i for i, prime in enumerate(is_prime) if prime]
    primes = primeGenerate(20000000)
    print len(primes)
    print "stage 1 complete"
    candidates = []
    for i in range(20):
        j=0
        while pow(primes[j],2**i)<10000000:
            candidates.append(pow(primes[j],2**i))
            j+=1
    print "stage 2 complete"
    candidates = sorted(list(set(candidates)))
    print len(candidates)
    print "stage 3 complete"
    out = 1
    out2 = 1
    for i in range(500500):
        if i%100==0: print i
        out2*=candidates[i]
        out*=candidates[i]
        out%=500500507
    return (out,math.log10(out2))
print euler500()
"""
def euler500():
    def primeGenerate(limit): # from rosettacode
	    is_prime = [False] * 2 + [True] * (limit - 1)
	    for n in range(int(limit**0.5 + 1.5)):
		    if is_prime[n]:
			    for i in range(n*n, limit+1, n):
				    is_prime[i] = False
	    return [i for i, prime in enumerate(is_prime) if prime]
    nn=1000000
    t=[]
    k = 1
    lim = nn**(1./k)
    while (lim>2):
        lim = nn**(1./k)
        for i in ([p**k for p in primeGenerate(int(lim)+100)]):
            t.append(i)
        k*=2
    return len(sorted(set(t)))
print euler500()
"""

