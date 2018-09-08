def euler94():
    z1,z2 = ([[-1,0]],[[1,0]]); for i in range(1,100):z1.append([-2*z1[i-1][0]-z1[i-1][1]-1,-3*z1[i-1][0]-2*z1[i-1][1]-1]);z2.append([-2*z2[i-1][0]-z2[i-1][1]+1,-3*z2[i-1][0]-2*z2[i-1][1]+1])
    return 3*sum([i[0] for i in z1+z2 if 1<i[0]<333333333])
print euler94()
