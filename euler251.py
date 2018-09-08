def euler251(max_sum = 1000):
    from sympy.ntheory import divisors
    from numpy import sqrt
    import time
    start = time.time()
    out = 0
    for k in xrange((max_sum-2)/3+1):
        if k%2000==0: print k, str(float(k)/((max_sum-2)/3+1))+"%", time.time()-start
        a = 3*k+2
        b2c = (k+1)*(k+1)*(8*k+5)
        for i in divisors(k+1,True):
            c = b2c / i / i
            if a+i+c<=max_sum: out+=1
    return out
print euler251()
def euler251_2():
    from numpy import sqrt, cbrt
    out = 0
    for a in range(1001):
        print a
        for b in range(1001-a):
            for c in range(1001-a-b):
                if cbrt(a+b*sqrt(c))+cbrt(a-b*sqrt(c))==1:
                    out+=1
    return out
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# x = [0]
# y = [0]
# for i in [j*1000 for j in range(1,11)]:
#     x.append(i)
#     start = time.time()
#     print euler251(i)
#     end = time.time()
#     y.append(end-start)
# print x,y
# print np.polyfit(x,y,1)
# plt.scatter(x,y)
# plt.show()
