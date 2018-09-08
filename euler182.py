def euler182():
    from fractions import gcd

    def miller_rabin(p):
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        else:
            d = p-1
            s = 0
            while d % 2 == 0:
                d /= 2
                s += 1
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
                temp = []
                for r in range(s):
                    temp.append(pow(a, d, p) != 1 and pow(
                        a, 2**r*d, p) != (p-1))
            return not(all(temp))
    from fractions import gcd

    def lcm(p, q): return abs(p*q)/gcd(p, q)

    def mul_inv(b, n):
        def xgcd(b, a):  # from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Iterative_algorithm_3
            x0, x1, y0, y1 = 1, 0, 0, 1
            while a != 0:
                q, b, a = b // a, a, b % a
                x0, x1 = x1, x0 - q * x1
                y0, y1 = y1, y0 - q * y1
            return b, x0, y0
        g, x, _ = xcd(b, n)
        if g == 1:
            return x % n
    p = 1009
    q = 3643
    n = p*q
    phi = (p-1)*(q-1)
    def unconcealed_msgs(e):
        if gcd(e,(p-1)*(q-1))!=1:
            return 10**100
        return (gcd(e-1,p-1)+1)*(gcd(e-1,q-1)+1)
    # out = {}
    # for e in range(1,phi):
    #     if e%1000==0: print e
    #     out[e] = unconcealed_msgs(e)
    # return min(out.values())
    # returns 9
    out = 0
    for e in range(1,phi):
        if e%1000==0: print e
        if unconcealed_msgs(e)==9:
            out+=e
    return out
print euler182()
