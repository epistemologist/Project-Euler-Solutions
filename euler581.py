def euler581():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    def is_smooth(n):
        for p in primes:
            while n%p==0:
                n/=p
        return n==1
    cache = dict()
    smooth_numbers = [1]
    sum = 0
    sum2 = 0
    for p in primes:
        print p, len(smooth_numbers)
        for n in smooth_numbers:
            if n not in cache and is_smooth(n+1):
                cache[n] = True
                sum += n
                sum2 += (n*(n+1))/2
            if n*p <= 10**13:
                smooth_numbers += [n*p]
    print sum2
    print len(smooth_numbers)
    return sum
print euler581()