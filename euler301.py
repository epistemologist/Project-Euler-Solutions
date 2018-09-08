def euler301():
    fib = lambda n: 1 if n<1 else fib(n-1)+fib(n-2); return fib(30)
print euler301()