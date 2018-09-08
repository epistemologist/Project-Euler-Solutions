def euler435():
    # F(10^15,x) * (x^2+x+1) = f(10^15)*x^(10^15+2) + f(10^15+1)*x^(n+1) - x
    import gmpy2

    def fast_fib(n,m):
        def mat_mul(a,b,m):
            out = [[None,None],[None,None]]
            for i in range(2):
                for j in range(2):
                    out[i][j]=(a[i][0]*b[0][j]+a[i][1]*b[1][j])%m
            return out
        def mat_pow(a,n,m):
            out = [[1,0],[0,1]]
            while n>0:
                if n%2==1:
                    out = mat_mul(out,a,m)
                a = mat_mul(a,a,m)
                n = n/2
            return out
        return mat_pow([[1,1],[1,0]],n,m)[0][1]
    def F(n,x,m):
        modulo = m*(x*x+x-1)
        return ((fast_fib(n,modulo)*pow(x,n+2,modulo)+fast_fib(n+1,modulo)*pow(x,n+1,modulo)-x)%modulo)/(x*x+x-1)
    return sum([F(10**15,x,1307674368000) for x in range(0,101)])%1307674368000
print euler435()
