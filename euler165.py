def euler165():
    from fractions import Fraction
    s = [290797]
    while len(s)<20001:
        s.append((s[-1]*s[-1])%50515093)
    s.pop(0)
    t = [i%500 for i in s]
    lines = []
    for i in range(len(t)):
        if i%4==0: lines.append(t[i:i+4])
    def intersection(x1,x2,x3,x4,y1,y2,y3,y4):
        try:
            t = Fraction((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4),(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
            u = Fraction(-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)),(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
            if 0<t<1 and 0<u<1:
                return ((x1+t*(x2-x1),y1+t*(y2-y1)),(x3+u*(x4-x3),y3+u*(y4-y3)))
            else:
                return 0
        except ZeroDivisionError:
            return 0
    points = []
    for i in range(len(lines)):
        print i
        for j in range(len(lines)):
            l = lines[i]
            m = lines[j]
            if intersection(l[0],l[2],m[0],m[2],l[1],l[3],m[1],m[3])!=0:
                points.append(intersection(l[0],l[2],m[0],m[2],l[1],l[3],m[1],m[3]))
    print len(set(points))
print euler165()