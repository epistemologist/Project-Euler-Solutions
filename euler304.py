def euler304():
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
    primes = []
    i = 10**14-1
    while len(primes) < 100000:
        if i % 1000 == 1:
            print i
        if miller_rabin(i):
            primes.append(i)
        i += 2
    m = 1234567891011

    def fast_fib(n, m):
        def mat_mul(a, b, m):
            out = [[None, None], [None, None]]
            for i in range(2):
                for j in range(2):
                    out[i][j] = (a[i][0]*b[0][j]+a[i][1]*b[1][j]) % m
            return out

        def mat_pow(a, n, m):
            out = [[1, 0], [0, 1]]
            while n > 0:
                if n % 2 == 1:
                    out = mat_mul(out, a, m)
                a = mat_mul(a, a, m)
                n = n/2
            return out
        return mat_pow([[1, 1], [1, 0]], n, m)[0][1]

    out = 0
    for p in primes:
        print p
        out += fast_fib(p,m)
    return out%m

print euler304()
