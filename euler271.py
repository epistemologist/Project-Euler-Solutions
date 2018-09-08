def euler271():
    import itertools
    def xgcd(a,b):
        # returns tuple (g,x,y) such that a*x+b*y=g=gcd(x,y)
        a,b=b,a
        x0, x1, y0, y1 = 1, 0, 0, 1
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0, y0
    def crt(a1,a2,n1,n2):
        """
        solves system
        x = a1 mod n1
        x = a2 mod n2
        """
        # Calculate Bezout coefficients
        _,m1,m2 = xgcd(n1,n2)
        return a1*m2*n2+a2*m1*n1
    def crt2(a,n):
        """
        solves system
        x = a_i mod n_i for all i
        """
        temp_a = crt(a[0],a[1],n[0],n[1])
        temp_n = n[0]*n[1]
        for i in range(2,len(a)):
            temp_a = crt(temp_a,a[i],temp_n,n[i])
            temp_n *= n[i]
        return temp_a
    count = -1
    for i in itertools.product(*[[i for i in range(m) if i**3%m==1] for m in [2,3,5,7,11,13,17,19,23,29,31,37,41,43]]):
        count+=crt2(i,[2,3,5,7,11,13,17,19,23,29,31,37,41,43])%13082761331670030
    return count
print euler271()