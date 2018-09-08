def euler199():
    from math import sqrt, pi

    def area(r): return pi*r*r

    def cover(k1, k2, k3, depth):
        k4 = k1+k2+k3+2*sqrt(k1*k2+k1*k3+k2*k3)
        r4 = 1/k4
        if depth == 1:
            return area(r4)
        else:
            return area(r4)+cover(k1, k2, k4, depth-1)+cover(k1, k3, k4, depth-1)+cover(k2, k3, k4, depth-1)

    return 1-(3*area(1)+3*cover(1, 1, 3-2*sqrt(3), 10)+cover(1, 1, 1, 10))/(area(1+2/sqrt(3)))


print euler199()
