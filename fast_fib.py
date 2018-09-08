"""
from math import factorial
import time
global splitting_factor
class Memoize:
    # source: https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def f(n):
    #print n
    if 0<=n<=5: return [0,1,1,2,3,5,8][n]
    else:
        if n%2==0:
            m=n/2
            return f(m)*f(m+1)+f(m)*f(m-1)
        else:
            m=(n-1)/2
            return f(m+1)**2+f(m)**2
def choose(n,k):
    return factorial(n)/factorial(k)/factorial(n-k)
def f2(n):
    k = splitting_factor
    if -8<=n<=8: return [-21,13,-8,5,-3,2,-1,1,0,1,1,2,3,5,8,13,21][n+8]
    else:
        m=n//k
        c=n%k
        f_n = f2(m)
        f_n_plus_one = f2(m+1)
        out = 0
        for i in range(k+1):
            out += choose(k,i)*f2(c-i)*pow(f_n,i)*pow(f_n_plus_one,(k-i))
        return out

f = Memoize(f)
f2 = Memoize(f2)
start = time.time()
a = f(10**7)
end = time.time()
print end-start,"self made function",len(f.memo)

# 
# Fast doubling Fibonacci algorithm (Python)
# 
# Copyright (c) 2015 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
# 


# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
_fib = Memoize(_fib)
start = time.time()
a = fibonacci(10**7)
end = time.time()
print end-start,"nayuki function",len(_fib.memo)

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

start = time.time()
a = fib(10**7)
end = time.time()
print end-start,"stack overflow function"
a2 = fib(10**6)
splitting_factor = 8

start = time.time()
a = f2(10**7)
end = time.time()
print end-start, "splitting factor of 8"
"""
import time
import gmpy2
def f3(n):
    return gmpy2.fib(n)
def fibonacci(n):
    f_n, f_n_plus_1 = 0, 1
    for i in range(n.bit_length() - 1, -1, -1):
        f_n_squared = f_n * f_n
        f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
        f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
        f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
        if n >> i & 1:
            f_n, f_n_plus_1 = f_2n_plus_1, f_2n + f_2n_plus_1
        else:
            f_n, f_n_plus_1 = f_2n, f_2n_plus_1
    return f_n
start = time.time()
a = fibonacci(10**8)
end = time.time()
print end-start,"gmpy"