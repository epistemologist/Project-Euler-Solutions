def euler358():
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
    # p is in interval [729927007,724637681], is prime, and is congruent to 9891 mod 10^5
    candidates = []
    for i in xrange(724609891, 729909891, 100000):
        if miller_rabin(i):
            candidates.append(i)
    n = [(pow(10, i-1)-1)/i for i in candidates]
    n = [len(str(i)) for i in n]
    return n

print euler358()
