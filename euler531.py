def solve_modular_equation_system(a,b,m,n):
    # sovles system x = a mod m, x = b mod n
    """
    CREDITS:
    https://codegolf.stackexchange.com/a/26753/45407
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python
    https://math.stackexchange.com/a/1644698/367373
    """
    from fractions import gcd
    if (a-b)%gcd(m,n)!=0: return 0
    else:
        def xgcd(b, a):
            x0, x1, y0, y1 = 1, 0, 0, 1
            while a != 0:
                q, b, a = b // a, a, b % a
                x0, x1 = x1, x0 - q * x1
                y0, y1 = y1, y0 - q * y1
            return  b, x0, y0
        g,u,v = xgcd(n,m)
        l = (a-b)/gcd(m,n)
        out = b+n*l*v
        out%=(n*m/gcd(m,n))
        if out<0: out+=(m*n/gcd(m,n))
        return out
def g(a,n,b,m):
    return solve_modular_equation_system(a,b,n,m)
print g(2,4,4,6)
print g(3,4,4,6)
def totient(n):
    phi = [0 for _ in range(n)]
    s = 0

    phi[1] = 1

    i = 2
    while i < n:
        if phi[i] == 0:
            phi[i] = i - 1

            j = 2

            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1

                    while q % i == 0:
                        f *= i
                        q //= i

                    phi[i * j] = f * phi[q]
                j += 1
        s += phi[i]
        i += 1
    return phi
def euler531():
    out = 0
    phi = totient(1005000)
    for m in range(1000000,1005000):
        print m
        for n in range(1000000,1005000):
            if n<m: 
                temp = g(phi[n],n,phi[m],m)
                if temp<0: raise ValueError
                out+=temp
    return out
print euler531()
