def euler70():
    from sympy.ntheory import totient
    n = 0
    n_over_phi_n = 100000
    for i in range(2,10**7):
        if i%10000==0: print i
        temp = totient(i)
        if sorted([int(j) for j in str(temp)])==sorted([int(j) for j in str(i)]):
            if float(i)/temp<n_over_phi_n:
                n = i
                n_over_phi_n = float(i)/temp
    return n
print euler70()