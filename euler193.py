def euler193():
    from math import floor, sqrt

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
        for i in xrange(2, n+1):
            if mu[i] == i:
                mu[i] = 1
            elif mu[i] == -i:
                mu[i] = -1
            elif mu[i] < 0:
                mu[i] = 1
            elif mu[i] > 0:
                mu[i] = -1
        return mu
    mu = mobius(2**25)
    out = 0
    for d in xrange(1,2**25+1):
        if d%1000==0: print (d,100*float(d)/(2**25))
        out+=mu[d]*int(float(2**50)/d/d)
        if int(float(2**50)/d/d)==0:
            break
    return out
print euler193()
