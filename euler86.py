def euler86():
    issquare = lambda x: int((x**0.5)%1==0)
    A143714 = lambda M: sum([sum([issquare((a+b)**2+M*M) for b in range(a,M+1)]) for a in range(1,M+1)])
    out = 0
    for i in range(10000):
        print i, out
        out+=A143714(i)
        if out>10**6: break
    return i
print euler86()