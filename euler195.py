def euler195():
    from fractions import gcd
    from math import sqrt
    out = []
    for m in range(10000):
        print m
        for n in range(m):
            if gcd(m,n)==1:
                a = m*m-m*n+n*n
                b = 2*m*n-n*n
                c = m*m-n*n
                r = sqrt(3)/2*n*(m-n)
                if r<100:
                    for k in range(1,101):
                        if [k*a,k*b,k*c] not in out:
                            out.append([k*a,k*b,k*c])
    return len(out)
print euler195()