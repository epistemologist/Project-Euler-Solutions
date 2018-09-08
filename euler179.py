def euler179():
    from sympy.ntheory.factor_ import divisor_count
    out = 0
    for i in xrange(1,10**7+1):
        if divisor_count(i)==divisor_count(i+1): out+=1
        if i%1000==0: print i
    return out
print euler179()    