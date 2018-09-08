def euler389():
    import itertools
    import collections
    import numpy
    def roll(n,sides):
        return collections.Counter([sum(i) for i in itertools.product(range(1,sides+1),repeat=n)])
    temp = roll(10,20)
    for i in temp:
        print i, temp[i]
print euler389()
