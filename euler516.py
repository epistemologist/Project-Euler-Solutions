temp = [2**i*3**j*5**k for i in range(41) for j in range(41) for k in range(41)]
temp = [i for i in temp if i<10**12]
print len(temp)
from sympy.ntheory import totient
for i in range(1,1000):
    print i, totient(i)