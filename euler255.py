def euler255():
    from math import ceil
    def avg(n):
        return sum(n)/float(len(n))
    def int_sqrt(n):
        x = []
        d = len(str(n))
        if d%2==1:
            x.append(2*10**((d-1)/2))
        else:
            x.append(7*10**((d-2)/2))
        x.append(int((x[-1]+ceil(float(n)/x[-1]))/2))
        while x[-1]!=x[-2]:
            x.append(int((x[-1]+ceil(float(n)/x[-1]))/2))
        return len(x)-1
    for i in range(1,100):
        print i, int_sqrt(i)
print euler255()
