def euler307():
    import time
    def monte_carlo():
        from random import randint
        from collections import Counter
        errors = []
        for i in range(20000):
            #if i%1000==0: print i
            errors.append(randint(0,999999))
        return max(Counter(errors).values())>2
    p = 0
    q = 0
    start = time.time()
    for i in xrange(1000000):
        if i%100==0: print i,p,q,time.time()-start
        q+=1
        if monte_carlo():
            p+=1
    return (p,q,time.time()-start)
print euler307()