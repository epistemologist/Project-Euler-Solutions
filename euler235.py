import sympy
r = sympy.symbols("r")
fx = 599999995000 - 1199999989103*r + 599999994100*r**2 + 14103*r**5001 - 14100*r**5002
fx = sympy.poly(fx).div(sympy.poly(r-1))[0].div(sympy.poly(r-1))[0]
print fx.all_coeffs()
"""
fprimex = sympy.diff(fx,r)
coefficients = sympy.poly(fx).all_coeffs()[::-1]
coefficients2 = sympy.poly(fprimex).all_coeffs()[::-1]
f = lambda x: sum([float(coefficients[i])*x**i for i in range(len(coefficients))])
fprime = lambda x: sum([float(coefficients2[i])*x**i for i in range(len(coefficients2))])
x0 = 1.0
tolerance = 10.**-12
epsilon = 10.**-14
maxIterations = 200
haveWeFoundSolution = False
for i in range(1,maxIterations):
    print i
    y = f(x0)
    yprime = fprime(x0)
    if abs(yprime)<epsilon:
        print "epsilon"
        break
    x1 = x0 - y/yprime
    if abs(x1-x0)<=tolerance*abs(x1):
        haveWeFoundSolution = True
        break
    x0 = x1
print x0,haveWeFoundSolution
"""
