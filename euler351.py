def euler351():
    # generating values by hand
    # 0,6,12,24,30,54 for x=1,2,3,4,5,6
    # OEIS A216453: formula is 6*(choose(n+1,2)-sum(i=1 to n of phi(i)))
    # sum of phi(i) from i=1 to n equals 1/2*(1+sum from k=1 to n of mobius(k)*(floor(n/k))^2)
    def mobius(n):
        mu = [None]*(n+1)
        for i in xrange(1, n+1):
            mu[i] = 1
        for i in xrange(2, int(n**0.5)+1):
            if mu[i] == 1:
                for j in xrange(i, n+1, i):
                    mu[j] *= -i
                for j in xrange(i*i, n+1, i*i):
                    mu[j] = 0
        for i in xrange(2,n+1):
            if mu[i]==i:
                mu[i]=1
            elif mu[i]==-i:
                mu[i]=-1
            elif mu[i]<0:
                mu[i]=1
            elif mu[i]>0:
                mu[i]=-1
        return mu
    from math import factorial

    import time
    start = time.time()
    n = 100000000
    mu = mobius(n)
    total = 0
    for i in xrange(1, n+1):
        end = time.time()
        if i % 5000 == 0:
            print (i, n+1, float(i)/(n+1), end-start, (end-start)*float(n+1)/i)
        total += mu[i]*int(float(n)/i)**2
        if int(float(n)/i) == 0:
            break
    total += 1
    total /= 2
    return 6*((n*(n+1))/2-total)
    import time
    def timeit(n):
        start = time.time()
        a = mobius(10**n)
        end = time.time()
        return end-start
    print timeit(8)
print euler351()
