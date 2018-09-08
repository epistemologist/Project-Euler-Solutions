def euler267():
    """
    if w is the number of wins, then
    money earned = (1+2f)^w*(1-f)^(1000-w)
    therefore 10^9>=(1+2f)^w*(1-f)^(1000-w)
    solving for w:
    (9*ln(10)-1000*ln(1-f))/(ln(1+2f)-ln(1-f))<=w
    taking the derivative of the LHS and setting equal to 0 (using WolframAlpha), we find
    f = 0.146883922440940676575582401469092721310098796598462
    h = 431.5 => at least 432 flips
    """
    from math import log, factorial
    #f = 0.146883922440941
    #return (9*log(10)-1000*log(1-f))/(log(1+2*f)-log(1-f))
    choose = lambda n,k: factorial(n)/factorial(k)/factorial(n-k)
    return float(sum([choose(1000,i) for i in range(432,1001)]))/(2**1000)
print euler267()

