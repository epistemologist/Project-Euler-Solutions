def euler448():
    from fractions import gcd
    def lcm(a,b):
        return (a*b)/gcd(a,b)
    def A(n):
        return sum([lcm(n,i) for i in range(1,n+1)])
    for i in range(20):
        print i,A(i)
print euler448()