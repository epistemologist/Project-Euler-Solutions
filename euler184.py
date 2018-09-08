def euler184(n):
    def det(u, v):
        return float(u[0]*v[1]-u[1]*v[0])
    points = [(i, j) for i in range(-n, n)
              for j in range(-n, n) if i*i+j*j < n*n]
    out = 0
    for x1, y1 in points:
        for x2, y2 in points:
            for x3, y3 in points:
                if abs((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)) != 0:
                    v = (0, 0)
                    v0 = (x1, y1)
                    v1 = (x2-x1, y2-y1)
                    v2 = (x3-x1, y3-y1)
                    a = (det(v, v2)-det(v0, v2))/det(v1, v2)
                    b = (det(v0, v1)-det(v, v1))/det(v1, v2)
                    if a > 0 and b > 0 and a+b < 1:
                        out += 1
    return out/6


print euler184(105)