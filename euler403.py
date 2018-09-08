def euler403():
    from math import sqrt, floor, ceil
    from fractions import gcd
    def L(a,b):
        A = (3*a*(a*a+2*b)-2*sqrt(a*a+4*b)*(a*a+b))/6.
        l = sqrt(a*a+4*b)+1
        x1 = 0.5*(a+sqrt(a*a+4*b))
        x2 = 0.5*(a-sqrt(a*a+4*b))
        P = floor(sqrt(floor(abs(x2)))) + 1 + floor(sqrt(floor(abs(x1)))) 
        b = l+P-2*int(x1%1.==0 and x2%1.==0)
        return A+1-0.5*b
    print L(1,2)
    print L(2,-1)
print euler403()