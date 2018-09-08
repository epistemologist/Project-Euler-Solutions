def euler323():
    import random

    def monte_carlo(n):
        x = 0
        out = 0
        while x != 2**n-1:
            x = x | random.getrandbits(n)
            out += 1
        return out

    def avg(arr):
        return float(sum(arr))/len(arr)
    # return avg([monte_carlo(3) for _ in xrange(10000000)])

    def choose(n, k):
        from math import factorial
        return factorial(n)/factorial(k)/factorial(n-k)

    from fractions import Fraction

    E = [Fraction(0), Fraction(2)]
    for n in range(2, 35):
        E.append((sum([Fraction(choose(n, k), 2**n)*(1+E[k])
                       for k in range(n)])+Fraction(1, 2**n))/(Fraction(2**n-1, 2**n)))
    return float(E[32])


def euler323_oneliner():
    from fractions import Fraction
    from math import factorial

    E = lambda n: [Fraction(0), Fraction(2)][n] if n in (0, 1) else (sum([Fraction(factorial(n)/factorial(k)/factorial(n-k), 2**n)*(1+E(k)) for k in range(n)])+Fraction(1, 2**n))/(Fraction(2**n-1, 2**n))
    return float(E(32))


print euler323_oneliner()
