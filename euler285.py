def euler285():
    from math import asin, sqrt, pi
    def A1(k):
        if k==1: return 0*(9*asin(sqrt(5)/3)-9*asin(2./3)-4*sqrt(5)+8)/8
        return ((-4*k**2+4*k-1)*asin(2/abs(2*k-1))+(4*k**2+4*k+1)*asin(2/(2*k+1))+2*sqrt(4*k**2+4*k-3)-2*sqrt(4*k**2-4*k-3))/(8*k**2)
    def A(k):
        return pi/(2*k)-2*A1(k)
    return sum([k*A(float(k)) for k in range(1,10001)])
print euler285()

((math.pi/4)*((k+.5)**2-(k-.5)**2)-((((k+.5)**2-1)**.5+math.asin(1/(k+.5))*(k+.5)**2)-(((k-.5)**2-1)**.5+math.asin(1/(k-.5))*(k-.5)**2)))/(k*k)