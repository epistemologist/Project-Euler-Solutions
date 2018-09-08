def euler461():
    from math import exp, pi
    import sys
    f = lambda k: exp(k/10000.)-1
    max_k = 0
    while f(max_k)<pi:
        max_k+=1
    memo = {}
    #return (max_k+1)**2
    for a in range(max_k+1):
        if a%100==0: print a,len(memo),sys.getsizeof(memo)
        for b in range(max_k+1):
            memo[f(a)+f(b)]=[a,b]
    return len(memo)
print euler461()