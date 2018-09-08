def euler504(m):
    from fractions import gcd
    def i(a,b,c,d):
        return 1+0.5*(a+c)*(b+d)-0.5*(gcd(a,b)+gcd(b,c)+gcd(c,d)+gcd(a,d))
    count = 0
    for a in range(1,m+1):
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    if (i(a,b,c,d)**0.5)%1.0==0: count+=1
                    print a,b,c,d
    return count
print euler504(100)
