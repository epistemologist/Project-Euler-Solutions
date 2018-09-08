def euler401():
    # https://kaygun.tumblr.com/post/61281353038/euler-project-401
    m = 10**7
    n = 10**15
    f = lambda x: (x*(x+1)*(2*x+1))/6
    out = 0
    for q in xrange(1,m):
        if q%100==0: print (q,m)
        out+=q*q*int(float(n)/q)
    for k in xrange(1,n/m+1):
        if k%100==0: print (k,n/m)
        out+=f(int(float(n)/k))
    return out - n/m*f(int(float(n)/(n/(m-1))))
def euler401_1liner(n=10**15,m=10**7):
    return sum((q*q*int(float(n)/q) for q in xrange(1,m)))+sum((((int(float(n)/k))*((int(float(n)/k))+1)*(2*((int(float(n)/k)))+1))/6 for k in xrange(1,n/m+1)))-n/m*((int(float(n)/(n/(m-1)))))*((int(float(n)/(n/(m-1))))+1)*(2*(int(float(n)/(n/(m-1))))+1)/6
import time
start = time.time()
print euler401_1liner()
end = time.time()
print end-start