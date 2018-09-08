def euler332():
    from math import sqrt, acos, pi, tan, atan

    def Z(r):
        n = int(sqrt(r))+1
        out = []
        for i in range(-n, n+1):
            for j in range(-n, n+1):
                for k in range(-n, n+1):
                    if i*i+j*j+k*k == r:
                        out.append((i, j, k))
        return out

    def dot(u, v):
        return sum([u[i]*v[i] for i in range(3)])

    def cross(u, v):
        return (u[1]*v[2]-u[2]*v[1], u[0]*v[2]-u[2]*v[0], u[0]*v[1]-u[1]*v[0])

    def norm(u):
        return dot(u, u)

    def area(a, b, c, r):
        def ang(a, b):
            return acos(dot(a, b)/sqrt(norm(a)*norm(b)))

        def excess(A, B, C):
            a = ang(B, C)
            b = ang(C, A)
            c = ang(A, B)
            s = 0.5*(a+b+c)
            return sqrt(tan(0.5*s)*tan(0.5*(s-a))*tan(0.5*(s-b)*tan(0.5*(s-c))))
        return atan(excess(a,b,c))*4*r*r

    def A(r):
        areas = []
        points = Z(r)
        for i in points:
            for j in points:
                for k in points:
                    i = [float(_) for _ in i]
                    j = [float(_) for _ in j]
                    k = [float(_) for _ in k]
                    try:
                        print i, j, k, area(i, j, k, r)
                        areas.append(area(i, j, k, r))
                    except:
                        print i, j, k, -1
                        areas.append(-1)
        return sorted(set(([i for i in areas if i > 0])))
    return A(14)


print euler332()
