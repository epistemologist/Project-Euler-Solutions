def euler577():
    A000914 = lambda n: ((n+1)*(n+2)*(n+3)*(3*n+8))/8
    A228317 = lambda n: ((n+3)*(n+2)*(n+1)*(3*n+4))/8
    A236770 = lambda n: ((n+1)*(n+2)*(3*n*n+9*n+4))/8
    print sum([[A236770((i-3)/3),A228317((i-3)/3),A000914((i-3)/3)][i%3] for i in range(3,12346)])
print euler577()