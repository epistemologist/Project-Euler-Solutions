def euler166():
    import itertools
    out = []
    for x in xrange(10**9):
        if x % 100000 == 0:
            print x
        x = str(x)
        while len(x) < 9:
            x = "0"+x
        x = [int(_) for _ in x]
        a, b, c, e, f, g, i, j, k = x
        #print a, b, c, e, f, g, i, j, k
        d = a+e+i-g-j
        s = a+b+c+d
        h = s-e-f-g
        l = s-i-j-k
        p = s-a-f-k
        o = s-c-g-k
        n = s-b-f-j
        m = s-a-e-i
        if 3*s == 2*a+b+c+e+2*f+g+i+j+2*k and 2*s == -d+a+e+i+j+g+2*f+2*k and 0 <= d <= 9 and 0 <= h <= 9 and 0 <= l <= 9 and 0 <= p <= 9 and 0 <= o <= 9 and 0 <= n <= 9 and 0 <= m <= 9:
            out.append([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p])
    return len(out)

import time
start = time.time()
print euler166()
end = time.time()
print end-start