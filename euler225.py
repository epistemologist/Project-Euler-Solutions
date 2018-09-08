def euler225():
    def test_n(n):
        t = [1,1,1,3]
        while t[-3:]!=[1,1,1]:
            t.append(int((t[-1]+t[-2]+t[-3])%n))
        return t.count(0)==0
    out = []
    for n in range(3,10000,2):
        print n
        if test_n(n):
            out.append(n)
        if len(out)>124:
            break
    return out
print euler225()