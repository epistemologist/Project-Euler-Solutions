def euler138():
    # using geometry, we get quadratic diophantine equation 5x^2+8x+4-4y^2=0 and 5x^2-8x+4-4y^2=0 where x=b and y=L
    x1=[0]
    x2=[0]
    x3=[0]
    x4=[0]
    y1=[1]
    y2=[1]
    y3=[-1]
    y4=[-1]
    for _ in range(24):
        i,j=-9*x1[-1]-8*y1[-1]-8,-10*x1[-1]-9*y1[-1]-8
        x1.append(i)
        y1.append(j)
        i,j=-9*x2[-1]+8*y2[-1]-8,10*x2[-1]-9*y2[-1]+8
        x2.append(i)
        y2.append(j)
        i,j=-9*x3[-1]-8*y3[-1]+8,-10*x3[-1]-9*y3[-1]+8
        x3.append(i)
        y3.append(j)
        i,j=-9*x4[-1]+8*y4[-1]+8,10*x4[-1]-9*y4[-1]-8
        x4.append(i)
        y4.append(j)
    return sum(sorted(list(set([i for i in y1+y2+y3+y4 if i>0])))[1:13])
print euler138()