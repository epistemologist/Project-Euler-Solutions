def euler204():
    p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    out = 1
    for i in xrange(2,10**9+1):
        if [i%q for q in p].count(0)!=0: out+=1
        if i%1000000==0: print i, out
    return out
print euler204()
#879680356