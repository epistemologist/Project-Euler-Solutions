def euler173():
    def factors(n):
        out = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                out.append((i,n/i))
                out.append((n/i,i))
        return out
    def solve(X): # returns number of solutions to Diophantine equation m^2-n^2=X
        out = []
        for p,q in factors(X):
            m,n = (p+q)/2., (p-q)/2.
            if m>0 and n>0 and int(m)==m and int(n)==n and m%2==n%2:
                out.append((int(m),int(n)))
        return len(out)
    out = 0
    for i in range(1,10**6+1):
        out+=solve(i)
        if i%1000==0: print i
    return out
def euler174():
    def factors(n):
        out = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                out.append((i,n/i))
                out.append((n/i,i))
        return out
    def solve(X): # returns number of solutions to Diophantine equation m^2-n^2=X
        out = []
        for p,q in factors(X):
            m,n = (p+q)/2., (p-q)/2.
            if m>0 and n>0 and int(m)==m and int(n)==n and m%2==n%2:
                out.append((int(m),int(n)))
        return len(out)
    out = [0]*11
    for i in range(1,10**6+1):
        temp = solve(i)
        if temp<=10: out[temp]+=1
        if i%1000==0: print i
    return sum(out)-out[0]
print euler174()