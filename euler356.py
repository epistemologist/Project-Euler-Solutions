def euler356():
    from numpy.polynomial.polynomial import polyroots as root
    def f(n):
        return max(root([n,0,-2**n,1]))
    for n in range(1,31):
        print 2**n-f(n)
print euler356()