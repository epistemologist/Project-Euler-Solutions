from sympy import factorint
from fractions import gcd
def A003415(n):
    return sum([int(n*e/p) for p, e in factorint(n).items()]) if n > 1 else 0
for i in range(100):
    print i, A003415(i), gcd(A003415(i),i)