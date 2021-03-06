def euler381():
    def S(p):
        a,b,c,d = pow(p-1,p-2,p),pow(p-2,p-2,p),pow(p-3,p-2,p),pow(p-4,p-2,p)
        return -(1+a+a*b+a*b*c+a*b*c*d)%p
    def primeGenerate(limit): # from rosettacode
	    is_prime = [False] * 2 + [True] * (limit - 1)
	    for n in range(int(limit**0.5 + 1.5)):
		    if is_prime[n]:
			    for i in range(n*n, limit+1, n):
				    is_prime[i] = False
	    return [i for i, prime in enumerate(is_prime) if prime]
    out = 0
    for i in primeGenerate(10**8):
        if i>=5: out+=S(i)
        print i
    return out
print euler381()

