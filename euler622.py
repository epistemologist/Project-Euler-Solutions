def euler622():
    def riffle(array):
        left_half = array[:len(array)/2]
        right_half = array[len(array)/2:]
        assert len(left_half)==len(right_half)
        out = []
        for i in range(len(left_half)):
            out.append(left_half[i])
            out.append(right_half[i])
        return out
    def s(n):
        deck = riffle(range(n))
        out = 1
        while deck!=range(n):
            deck = riffle(deck)
            out+=1
        return out
    # S(2n+2) = A002326(n)
    # question reduces to sum of values n s.t. A002326(n)==60
    from sympy import divisors
    f = lambda n: sum([i+1 for i in divisors(2**n-1) if i%2==1 and i<2**n])
    print divisors(60)
    #return f(60)-f(30)-f(20)-f(12)-f(10)-f(6)-f(4)-f(2)
    """
(23:41) gp > a(n)=if(n<0, 0, znorder(Mod(2, 2*n+1)))
%23 = (n)->if(n<0,0,znorder(Mod(2,2*n+1)))
(23:41) gp > out=0
%24 = 0
(23:41) gp > fordiv(2^60-1,i,;if(a((i-1)/2)==60,out+=i+1))
(23:42) gp > out
%26 = 3010983666182123972
(23:42) gp >
"""
print euler622()