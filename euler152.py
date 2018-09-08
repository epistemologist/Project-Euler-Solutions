def euler152():
    arr = [i*i for i in reversed(range(2,81))]
    from fractions import gcd
    lcm = reduce(lambda x,y: x*y/gcd(x,y),arr)
    return lcm
    return arr
    """
    sums = [0]*(sum(arr)+10)
    sums[0] = 1
    sp = 0
    for p in arr:
        print p
        for i in reversed(range((sp+1))):
            sums[p+i] += sums[i]
        sp+=p
    out = 0
    for i in range(len(sums)):
        if i%1000==0: print i
        if is_prime(i):
            out+=sums[i]
            #print sums[i]
    return out
    """
print euler152()