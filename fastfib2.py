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


print fast_fib(10**6, 10**6)
