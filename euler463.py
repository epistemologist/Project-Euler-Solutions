def euler463():
    f = [0,1,1,3,1]
    for i in range(5,1001):
        if i%4==0:
            f.append(f[i/2])
        elif i%4==1:
            n = (i-1)/4
            f.append(2*f[2*n+1]-f[n])
        elif i%4==2:
            f.append(f[i/2])
        else:
            n = (i-3)/4
            f.append(3*f[2*n+1]-2*f[n])
    g = lambda x: int(bin(x)[2:][::-1],2)
    S = lambda n: sum(f[1:n+1])
    for i in range(100):
        print i, S(i)
#print euler463()
A = {0:0, 1:1, 2:2, 3:5}
def a(n):
    a_n = A.get(n)
    if a_n is not None:
        return a_n
    q,r = divmod(n,4)
    if r == 0:
        a_n = a(q*2)*6 - a(q)*5 - a(q - 1)*3 - 1
    elif r == 1:
        a_n = a(q*2 + 1)*2 + a(q*2)*4 - a(q)*6 - a(q - 1)*2 - 1
    elif r == 2:
        a_n = a(q*2 + 1)*3 + a(q*2)*3 - a(q)*6 - a(q - 1)*2 - 1
    else:
        a_n = a(q*2 + 1)*6 - a(q)*8 - 1
    A[n] = a_n
    return a_n
print a(3**37)%10**9