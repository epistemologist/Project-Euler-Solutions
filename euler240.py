def euler240(n=3,s=5,T=15):
    from math import factorial
    f = lambda n: factorial(n) if n>=0 else 0
    choose = lambda n,k: f(n)/f(k)/f(n-k) if n>=k else 0
    return sum([(-1)**a*choose(n,a)*choose(T-a*s-1,n-1) for a in range(n)])
print euler240()