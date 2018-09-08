def euler621():

    # let t(n)=G(n) given in the problem
    # then t(n) = r(8n+3) where r(n) = # of ways to write n as sum of 3 odd squares
    # t(17526*10^9)=r(140208000000003)=r(9^4*21369913123)
    # given recurrence in paper provided, since n=21369913123=19 mod 24
    # r(9^4*n)=(2*3^4-1)*r(n)
    # to find r(21369913123)
print euler621()
