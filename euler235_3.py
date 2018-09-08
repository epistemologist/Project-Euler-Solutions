from decimal import *
getcontext().prec = 20
s = lambda r: sum([(900-3*k)*r**(k-1) for k in range(5001)])+(600000000000.)
sign = lambda x: 1 if x>=0 else -1
def bisect(f,a,b,tol,nmax):
    n=1
    while n<nmax:
        if n%1000==0: print n,b-a
        c=(a+b)/2
        if f(c)==0 or (b-a)/2<tol:
            return c
        n+=1
        if sign(f(c))==sign(f(a)):
            a = c
        else:
            b = c
    return "failure"
#print bisect(s,1.001,1.003,1e-15,10000)
print [s(float("1.00232210863"+str(i))) for i in range(10)]
