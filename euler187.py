def euler187():
    def prime_factors(n):
        out = []
        while n % 2 == 0:
            out.append(2)
            n /= 2
        for i in xrange(3, int(n**0.5+3)):
            while n % i == 0:
                out.append(i)
                n /= i
        if n > 2:
            out.append(n)
        return out
    count = 0
    for i in xrange(2, 10**8):
        if i % 5000 == 0:
            print i
        if len(prime_factors(i)) == 2:
            count += 1
    return count

import time
start = time.time()
print euler187()
end = time.time()
print end-start