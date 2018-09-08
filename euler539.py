def euler539():
    def eliminate(n):
        out = []
        for i in range(len(n)):
            if i%2==1:
                out.append(n[i])
        return out
    def p(k):
        a = range(1,k+1)
        while len(a)>1:
            a = eliminate(a)
            a = a[::-1]
        return a[0]
    for i in range(4,100):
        print i, p(i), p(i//4), i%4, p(i)-4*p(i//4)
print euler539()