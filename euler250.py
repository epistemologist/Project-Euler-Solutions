def euler250():
    sets = [0]*250
    sets[0] = 1
    for i in range(1,250251):
        if i%1000==0: print i
        sets = [sets[j]+sets[j-pow(i,i,250)] for j in range(len(sets))]
    return (sets[0]-1)%(10**16)
print euler250()
