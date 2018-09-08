def euler211():
    import time
    start = time.time()
    def sigma2(n):
        out = []
        for i in range(1,8000):
            if n%i==0: out.append(i);out.append(n/i)
        return sum([i*i for i in set(out)])
    out = 0
    for i in range(1,64000000):
        if i%5000==0: print i, str(100*i/64000000.)+"%", str(time.time()-start)+" seconds elapsed"
        if (sigma2(i)**0.5)%1==0: out+=i
    return out
print euler211()