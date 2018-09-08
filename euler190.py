def euler190():
    out = 0
    for m in range(2,16):
        x1 = 2./(m+1)
        P = [(i*x1)**i for i in range(1,m+1)]
        out2 = 1
        for p in P: out2*=p
        out+=int(out2)
    return out
        
print euler190()