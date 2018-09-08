def euler243():
    from sympy.ntheory import totient
    d = 10
    while True:
        if d%100==0: print d
        if totient(d)*94744<15499*(d-1):
            print d
            break
        d+=1
print euler243()