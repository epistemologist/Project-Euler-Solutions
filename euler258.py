def euler258():
    out = [1]*10000
    for i in range(2000,10000):
        out[i]=out[i-2000]+out[i-1999]
    return out
def euler258_2():
    import numpy as np
    import time
    start = time.time()
    M = np.zeros((2000,2000),dtype = int)
    M[0][-1] = 1
    M[0][-2] = 1
    for i in range(1,2000):
        M[i][i-1] = 1
    temp = [M]
    for i in range(len(bin(10**18))-2):
        print i
        temp.append(np.matmul(temp[-1],temp[-1]))
    temp = temp[::-1]
    N = temp[0]
    for i in [i for i in range(1,len(bin(10**18))-2) if bin(10**18)[2:][i]=="1"]:
        N = np.matmul(N,temp[i])
        print i
    print N
    P = np.matmul(N,np.reshape([1 for _ in range(2000)],(2000,1)))
    print P
    end = time.time()
    return end-start
print euler258_2()