a = [1]
from fractions import Fraction
for i in range(1,100):
    a.append(a[-1]*2*(2*i+1)/(i+1))
print [int(i) for i in a]