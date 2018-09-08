def euler226():
    import matplotlib.pyplot as plt
    import numpy as np
    from math import sin, cos, sqrt, pi, log, asin
    EPSILON = 1e-12

    def s(x):
        return min([abs(x-i) for i in [int(x)-1, int(x), int(x)+1]])

    def blanc(x):
        out = 0
        n = 0
        while True:
            if 1./(2**n) < EPSILON:
                break
            out += s(2.**n*x)/2**n
            n += 1
        return out

    for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]:
        print i, s(i)

    def plot():
        x = np.arange(0, 1, 0.0001)
        y = [blanc(i) for i in x]
        u = np.arange(0, 2*pi, 0.0001)
        a = 0.25
        b = 0.5
        r = 0.25
        xt = [a+r*cos(t) for t in u]
        yt = [b+r*sin(t) for t in u]
        plt.scatter(x, y, s=0.1, c="green")
        plt.scatter(xt, yt, s=0.1, c="blue")
        plt.show()

    def find_intersections():
        # using bottom half of circle
        # cartesian equation: y = f(x) = 1/2 - sqrt(1/16-(x-1/4)^2)
        # we want root of 0 = f(x) - blanc(x) on x = [0,0.5]
        def f(x):
            return 0.5 - sqrt(0.0625-(x-0.25)**2) - blanc(x)
        a = 0
        b = 0.5
        n = 1
        while n <= 1000:
            c = (a+b)/2
            if f(c) == 0 or (b-a)/2 < EPSILON:
                return c
            n += 1
            if f(c)*f(a) > 0:
                a = c
            else:
                b = c
        return "fail"
    intersection1 = find_intersections()
    intersection2 = 0.5

    def I(x):
        # from WIKIPEDIA
        if x < EPSILON:
            return 0.
        elif EPSILON <= x <= 0.5:
            return I(2*x)/4+x*x/2
        elif 0.5 <= x <= 1:
            return 0.5-I(1.-x)
        else:
            n = int(x)
            return 0.5*n*I(x-n)

    def F(a):
        # returns the area under a circle from x=a to x=0.5 
        # assumed that 0<a<0.5
        return -a/2-pi/64+0.25+(a-0.25)*sqrt(-16*(a-0.25)**2+1)/8+asin(4*a-1)/32

    area_under_blancmange = I(intersection2) - I(intersection1)
    area_under_circle = F(intersection1)

    return area_under_blancmange - area_under_circle 
print euler226()
