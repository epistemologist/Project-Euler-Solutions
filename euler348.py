def euler348():
    from collections import Counter
    out = []
    for i in xrange(30000):
        print i
        for j in xrange(2000):
            out.append(i*i+j*j*j)
    out2 = Counter(out)
    candidates = []
    for i in out2:
        if out2[i] == 4 and str(i)==str(i)[::-1]:
            candidates.append(i)
            print i
    print candidates,len(candidates)


print euler348()
