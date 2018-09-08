def euler191():
    """
    3**30 - # of strings with 2 or more L's
          - # of strings with no Ls and runs of 3 or more A's
          - # of strings with 1 L and runs of 3 or more A's
    """
    import itertools
    def f(n):
        out = 0
        for i in itertools.product("AO",repeat=n):
            if "AAA" in "".join(i): out+=1
        return out
    def g(n):
        out = 0
        for i in itertools.product("AOL",repeat=n):
            i = "".join(i)
            if "AAA" in i and i.count("L")==1:
                out+=1
        return out
    for i in range(15):
        print f(i)
print euler191()