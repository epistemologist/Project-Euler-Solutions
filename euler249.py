def euler249():
    def is_prime(n):
        if n<2: return False
        if n==2: return True
        if n%2==0: return False
        for i in range(2,int(n**0.5)+2):
            if n%i==0:
                return False
        return True
    primes = [i for i in range(5000) if is_prime(i)]
    sums = [0]*(sum(primes)+10)
    sums[0] = 1
    sp = 0
    for p in primes:
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
print euler249()
