def euler303():
    import itertools
    import time
    start = time.time()
    temp = sorted([int("".join(i)) for i in itertools.product("012",repeat=16)])
    end = time.time()
    print end-start
    def f(x):
        if x==9999: return 11112222222222222222
        for i in temp:
             if i!=0 and i%x==0:
                return i
    return sum([f(i)/i for i in range(1,10001)])
print euler303()
