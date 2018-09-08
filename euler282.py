def euler282():
    class Memoize:
        # source: https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
        def __init__(self, f):
            self.f = f
            self.memo = {}

        def __call__(self, *args):
            if not args in self.memo:
                self.memo[args] = self.f(*args)
            return self.memo[args]
    
    def knuth_up_arrow(args):
        a,n,b,m = args[0],args[1],args[2],args[3]
        if n==1: return pow(a,b,m)
        elif n>=1 and b==0: return 1
        else: return knuth_up_arrow((a,n-1,knuth_up_arrow((a,n,b-1,m)),m))
    knuth_up_arrow = Memoize(knuth_up_arrow)
    return knuth_up_arrow((3,3,3,10**200))

print euler282()
