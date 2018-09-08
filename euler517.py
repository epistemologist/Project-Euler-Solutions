def euler517():
    import math
    def g(a,x):
        if x<a: return 1
        else: return g(a,x-1)+g(a,x-a)
    def G(n):
        return g(math.sqrt(n),n)
    for i in range(2,100):
        print i,G(i)
print euler517()