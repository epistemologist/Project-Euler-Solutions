def euler322():
    from math import factorial
    def choose(n,k):
        return factorial(n)/factorial(k)/factorial(n-k)
    def T(m,n):
        return [choose(i,n) for i in range(n,m+1)]
    return T(12,8)
print euler322()