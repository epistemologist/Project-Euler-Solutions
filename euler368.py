def euler368():
    out = 0
    three_digits = ["111","222","333","444","555","666","777","888","999","000"]
    for i in range(1,2*10**6):
        if not(any([j in str(i) for j in three_digits])):
            out+=1./i
        if i%1000==0: print i
    return out
print euler368()