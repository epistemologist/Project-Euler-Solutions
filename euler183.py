def euler183():
    from math import e
    import fractions
    def f(n,x):
        return (fractions.Fraction(n,x))**x
    def M(n):
        return max(f(n,int(n/e)),f(n,int(n/e)+1))
    def D(n):
        temp = fractions.Fraction(M(n)).denominator
        while temp%2==0: 
            temp/=2
        while temp%5==0:
            temp/=5
        if temp==1: return -n
        else: return n
    return sum([D(n) for n in range(5,10001)])
print euler183()