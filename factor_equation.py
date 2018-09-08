n=28880460844831016377906248380078949193482240000000
# solving equation n = ab(a+b)
"""
factorization of n:
2^25 * 3^10 * 5^7 * 7^4 * 11^4 * 13^6 * 17^4 * 19^6 * 23^4
"""
# STEP 1: loop over all possible values of i
import itertools
generator_factors = itertools.product(range(26),range(11),range(8),range(5),range(5),range(7),range(5),range(7),range(5))
primes = [2,3,5,7,11,13,17,19,23]
def is_square(n):
    return (n**0.5)%1.0==0
count = 0
solutions = []
for i in generator_factors:
    if count%10000==0: print count
    a = 1
    for j in range(len(primes)):
        a*=primes[j]**i[j]
    if is_square(a**4+4*a*n):
        sqrt = int((a**4+4*a*n)**0.5)
        b = (sqrt-a*a)/(2*a)
        if 2*a*b == sqrt-a*a:
            print (a,b)
            solutions.append((a,b))
    count+=1
print solutions