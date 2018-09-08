def euler363():
    from sympy import *
    v = 2 - sqrt((22+5*pi)/3)
    t = symbols("t")
    return integrate(sqrt((-3+6*t*v-9*t*t*v)**2+(9*t*t*v-12*t*v+3*v+6*t-6*t*t)**2),(t,0,1)).evalf()
print euler363()