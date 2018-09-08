def euler596():
    def A24916(z):
        s = z*z
        u = int(z**0.5)
        p = 0
        for d in range(1,u+1):
            n = z//d - z//(d+1)
            if n<=1:
                p = d
                break
            else:
                a = z%d
                s -= (2*a+(n-1)*d)*n/2
        if p==0:
            u = z//(u+1)
        else:
            u = z//p
        for d in range(2,u+1):
            s -= z%d
        return s
    def f(x):
        return (8*A24916(x)-32*A24916(x/4))%1000000007
    return f(0)+f(1)+f(2)
print euler596()
