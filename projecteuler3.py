def primeGenerate(limit): # from rosettacode
	is_prime = [False] * 2 + [True] * (limit - 1)
	for n in range(int(limit**0.5 + 1.5)):
		if is_prime[n]:
			for i in range(n*n, limit+1, n):
				is_prime[i] = False
	return [i for i, prime in enumerate(is_prime) if prime]
def isPrime(p):
	for i in range(2,int(p**0.5)+2):
		if p%i==0: return False
	return p>3
def euler91():
	def check_triangle(x1,y1,x2,y2):
		d1=x1**2+y1**2
		d2=x2**2+y2**2
		d3=(x2-x1)**2+(y2-y1)**2
		t=sorted([d1,d2,d3])
		return t[2]==t[1]+t[0] and t.count(0)==0
	out=[]
	for x1 in range(51):
		for x2 in range(51):
			print x1,x2
			for y1 in range(51):
				for y2 in range(51):
					if check_triangle(x1,y1,x2,y2)==True and (([x1,y1,x2,y2]) not in out) and ([x2,y2,x1,y1] not in out): out.append([x1,y1,x2,y2])
	print len(out)
def euler92():
	def check(n):
		while True:
			if n==1 or n==89: break
			else: n=sum([int(i)**2 for i in str(n)])
		return n
	count=0
	for i in range(1,10000001):
		if check(i)==89: count+=1
		if i%10000==0: print i
	print count
def euler97():
	return int((28433*pow(2,7830457,10000000000)+1)%1e10)
def euler99():
	import urllib2
	import math
	a=([math.log(l[0])*l[1] for l in [[int(k) for k in j] for j in [i.split(",") for i in urllib2.urlopen("https://projecteuler.net/project/resources/p099_base_exp.txt").read().split("\n")]]])
	maximum=max(a)
	for i in range(len(a)):
		if a[i]==maximum: print i+1
def euler100():
	# b(b-1)/c(c-1) = 1/2
	# 2b^2-2b=c^2-c
	# b^2-b-d=0 where d = (c^2-c)/2
	# b = ((sqrt(2*n^(2)-2*n+1)+1)/(2)) = 1/2*(sqrt(2*c*c-2*c+1)-1)
	# 2c^2-2*c+1 = k^2 where k=2*b+1
	# c->x, k->y, 2x^2-2x+1=y^2
	# x(n+1)=3*x(n)+2*y(n)-1, y(n+1)=4*x(n)+3*y(n)-2
	c=1000000000000
	x=[1]
	y=[1]
	while x[-1]<1000000000000:
		xtemp=3*x[-1]+2*y[-1]-1
		ytemp=4*x[-1]+3*y[-1]-2
		x.append(xtemp)
		y.append(ytemp)
	print (y[-1]+1)/2
def euler101():
	import fractions
	f=fractions.Fraction
	def LagrangePolynomial(x,xi,yi):
		k=len(yi)-1
		def LagrangeBasis(j,x2):
			num=1
			den=1
			for m in range(k+1):
				if m!=j:
					num*=x2-xi[m]
					den*=xi[j]-xi[m]
			return f(num,den)
		total=0
		for i in range(k+1):
			total+=yi[i]*LagrangeBasis(i,x)
		return total
	#print LagrangePolynomial(11,[1,2,3],[1,4,9])
	def u(n):
		return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
	a=range(1,21)
	b=[u(i) for i in range(1,21)]
	total=0
	for i in range(1,11):
		j=1
		while LagrangePolynomial(j,a[:i],b[:i])==u(j):
			print i,u(j),LagrangePolynomial(j,a[:i],b[:i]),u(j+1),LagrangePolynomial(j+1,a[:i],b[:i])
			j+=1
		print "+",LagrangePolynomial(j,a[:i],b[:i])
		total+=LagrangePolynomial(j,a[:i],b[:i])
	print total
def euler102():
	from math import sqrt
	import urllib2
	text = urllib2.urlopen("https://projecteuler.net/project/resources/p102_triangles.txt")
	triangles = [[int(j) for j in i.strip("\n").split(",")] for i in text.readlines()]
	def d(x,y):
		return sqrt((y[0]-x[0])**2+(y[1]-x[1])**2)
	def hero(a,b,c):
		side1=d(a,b)
		side2=d(b,c)
		side3=d(a,c)
		s=(side1+side2+side3)*0.5
		return sqrt(s*(s-side1)*(s-side2)*(s-side3))
	def checkTriangle(inp):
		a=[inp[0],inp[1]]
		b=[inp[2],inp[3]]
		c=[inp[4],inp[5]]
		o=[0,0]
		return abs(hero(a,b,c) - (hero(o,b,c)+hero(a,o,c)+hero(a,b,o)))<1
	# A(-340,495), B(-153,-910), C(835,-947)
	# X(-175,41), Y(-421,-714), Z(574,-645)
	print [checkTriangle(i) for i in triangles].count(True)
def euler104():
	from decimal import Decimal as d
	fib=[0,1]
	flag=True
	phi=(1+5**d(0.5))/2
	while flag:
		fib.append((fib[-1]+fib[-2])%10000000000)
		if sorted(str(fib[-1])[-9:])==list("123456789"):
			if sorted(str(int(phi**(len(fib)-1)/(5**d(0.5))))[::-1][-9:])==list("123456789"):
				print len(fib)-1; flag=False
		if len(fib)%10000==0: print len(fib)
	print len(fib)-1
def euler108():
	# 1/(n+x)+1/(n+y)=1/n <=> n^2=xy
	# number of factors of n^2 is number of solutions
	def factor(n): # from dreamshire
		f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
		if n < 1:
			return []
		while True:
			for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
				f += gap
				if f * f > n:  # If f > sqrt(n)
					if n == 1:
						return factors
					else:
						return factors + [(n, 1)]
				if not n % f:
					e = 1
					n //= f
					while not n % f:
						n //= f
						e += 1
					factors.append((f, e))
	def numOfSolutions(n):
		return (reduce(lambda x,y: x*y, [i[1]+1 for i in factor(n*n)])+1)/2
	i=4
	while True:
		if numOfSolutions(i)>1000: print i; break
		if i%1000==0: print i
		i+=1
def euler109():
	darts=[(x,y) for x in [25,50] for y in ["single","double"]]+[(x,"single") for x in range(1,21)]+[(x,"double") for x in range(2,42,2)]+[(x,"triple") for x in range(3,63,3)]
	count=0
	out=[]
	for dart1 in darts+[(0,0)]:
		for dart2 in darts+[(0,0)]:
			for dart3 in darts:
				if dart1<=dart2 and dart3[1]=="double" and (dart1[0]+dart2[0]+dart3[0]<100):
					if count%1000==0: print dart1,dart2,dart3
					count+=1
					out.append((dart1,dart2,dart3))
	count2=0
	for i in out:
		if out.count(i)>1: print "AH"; count2+=1
	print count2
def euler112():
	def isBouncy(n):
		return not(list(str(n))==sorted(str(n))) and not(list(str(n))==sorted(str(n))[::-1])
	i=100
	j=0
	while 99*i!=100*j:
		if isBouncy(i): j+=1
		i+=1
		if i%100==0: print i,j,100*j-99*i
	print i
def euler113():
	def isBouncy(n):
		return not(list(str(n))==sorted(str(n))) and not(list(str(n))==sorted(str(n))[::-1])
	print "1000",len([i for i in range(1,1000) if isBouncy(i)==False])
	print "10000",len([i for i in range(1,10000) if isBouncy(i)==False])
	print "100000",len([i for i in range(1,100000) if isBouncy(i)==False])
	print "1000000",len([i for i in range(1,1000000) if isBouncy(i)==False])
	print "10000000",len([i for i in range(1,10000000) if isBouncy(i)==False])
def euler114():
	import itertools
	# 0,0,2,4,7,11,17,27,
	def factorial(n):
		if n==0: return 1
		else: return reduce(lambda x,y: x*y, range(1,n+1))
	def binomial(n,k):
		return factorial(n)/factorial(k)/factorial(n-k)
	print sum([binomial(51-2*k,2*k) for k in range(int(51/4)+1)])
def euler115():
	def f(m,n):
		def factorial(n):
			if n==0: return 1
			else: return reduce(lambda x,y: x*y, range(1,n+1))
		def binomial(n,k):
			return factorial(n)/factorial(k)/factorial(n-k)
		return sum([binomial(n+1-(m-1)*k,(m-1)*k) for k in range(int((n+1)/(m+1))+1)])
	print f(10,56)
def euler115():
	# f(m,n+1)=f(m,n)+f(m,n-m)+f(m,n-m-1)+...+f(m,1)+2
	# f(m,n)=1 if 1<=n<m
	def f(m,n):
		out=[0]*1000
		out[0]=1
		solutions=1
		for n in range(1,100):
			if n>m: out[n]==0
		return out
	print f(10,100)[56]
def euler116():
	def red(n):
		out=[0]*(n+2)
		out[1]=1
		out[2]=2
		for i in range(3,n+2):
			out[i]=out[i-1]+out[i-2]
		return out[n]
	def green(n):
		out=[0]*(n+2)
		out[1]=1
		out[2]=1
		out[3]=2
		for i in range(4,n+2):
			out[i]=out[i-1]+out[i-3]
		return out[n]
	def blue(n):
		out=[0]*(n+2)
		out[1]=1
		out[2]=1
		out[3]=1
		out[4]=2
		for i in range(5,n+2):
			out[i]=out[i-1]+out[i-4]
		return out[n]
	print red(50)+blue(50)+green(50)-3
def euler117():
	out=[1,2,4,8]
	while len(out)<50:
		out.append(sum(out[-4:]))
	print out[49]
def euler118():
	import itertools
	def isPrime(p):
		for i in range(2,int(p**0.5)+2):
			if p%i==0: return False
		return (p>1)
	def sublists(lst): # from stack exchange
		for doslice in itertools.product([True, False], repeat=len(lst) - 1):
			slices = []
			start = 0
			for i, slicehere in enumerate(doslice, 1):
				if slicehere:
					slices.append(lst[start:i])
					start = i
			slices.append(lst[start:])
			yield slices
	print len(list(sublists([1,2,3,4,5,6,7,8,9])))
	count=0
	pp=0
	for i in itertools.permutations([1,2,3,4,5,6,7,8,9]):
		print i,pp
		pp+=1
		for j in sublists(i):
			temp=sorted([int("".join([str(l) for l in k])) for k in j])
			if all([isPrime(i) for i in temp])==True: count+=1
	
	print count
def euler119():
	out=[]
	for b in range(2,100):
		for e in range(100):
			if sum([int(i) for i in str(b**e)])==b: out.append(b**e)
	print [i for i in sorted(list(set(out))) if i>9][29]
def euler120():
	# expanding with binomial theorem and throwing any terms not constant or linear in a leads to
	def r(a):
		return max([(1+a*n+(-1)**n+a*n*(-1)**(n-1))%(a*a) for n in range(a*a)])
	total=0
	for i in range(3,1001):
		total+=r(i)
		print i
	print total
def euler122():
	possibleExponentiations=[[1,2],[1,2,4],[1,2,4,8],[1,2,4,8,16],[1,2,4,8,16,32],[1,2,4,8,16,32,64],[1,2,4,8,16,32,64,128]]
	testedExponents=[1,2]
	count=0
	while True:
		for i in possibleExponentiations:
			if type(i)==type([2]):
				for j in [x+y for x in i for y in i]:
					newExponentiation=i+[j]
					if sorted(list(set(newExponentiation)))==newExponentiation and newExponentiation not in possibleExponentiations and len(newExponentiation)<11:
						possibleExponentiations.append(newExponentiation)
						testedExponents.append(j)
					count+=1
					if count%5000==0: print count, len([k for k in list(set(testedExponents)) if 1<=k<=200]),"len(out)", len(possibleExponentiations[-1]), possibleExponentiations[-1]
def euler122():
	possibleExponentiations=[[1,2],[1,2,4],[1,2,4,8],[1,2,4,8,16],[1,2,4,8,16,32],[1,2,4,8,16,32,64],[1,2,4,8,16,32,64,128]]
	testedExponents=[1,2]
	count=0
	while len(possibleExponentiations)!=11843:
		for i in possibleExponentiations:
			if type(i)==type([2]):
				for j in [x+y for x in i for y in i]:
					newExponentiation=i+[j]
					if len(newExponentiation)<8 and newExponentiation not in possibleExponentiations:
						possibleExponentiations.append(newExponentiation)
						testedExponents.append(j)
					count+=1
					if count%5000==0: print count, len([k for k in list(set(testedExponents)) if 1<=k<=200]),"len(out)", len(possibleExponentiations[-1]), possibleExponentiations[-1], len(possibleExponentiations), [1,2,4,8] in possibleExponentiations
		out=[]
		for i in list(set(testedExponents)):
			if i>2: out.append([j for j in possibleExponentiations if j[-1]==i and len(j)==min([len(k) for k in possibleExponentiations if k[-1]==i])][0])
			print out
	possibleExponentiations=out
	testedExponents=[i[-1] for i in possibleExponentiations]
	count=0
	while True:
		for i in possibleExponentiations:
			if type(i)==type([2]):
				for j in [x+y for x in i for y in i]:
					newExponentiation=i+[j]
					if sorted(list(set(newExponentiation)))==newExponentiation and newExponentiation not in possibleExponentiations:
						possibleExponentiations.append(newExponentiation)
						testedExponents.append(j)
					count+=1
					if count%5000==0: print count, len([k for k in list(set(testedExponents)) if 1<=k<=200]),"len(out)", len(possibleExponentiations[-1]), possibleExponentiations[-1], len(possibleExponentiations)
def euler122():
	possibleExponentiations = [[1,2],[1,2,4],[1,2,4,8],[1,2,4,8,16],[1,2,4,8,16,32],[1,2,4,8,16,32,64],[1,2,4,8,16,32,64,128]]
	count = 0
	while True:
		for i in possibleExponentiations:
			for j in [x+y for x in i for y in i]:
				if sorted(list(set(i+[j])))==i+[j] and len(i+[j])<15:
					possibleExponentiations.append(i+[j])
				def m(a):
					temp=[len(k) for k in possibleExponentiations if k[-1]==a]
					if len(temp)!=0: return min(temp)
					else: pass
				if count%10000==0:
					print len(possibleExponentiations), len(sorted(list(set([k[-1] for k in possibleExponentiations if 1<=k[-1]<=200]))))
					if count%1500000==0 and len(sorted(list(set([k[-1] for k in possibleExponentiations if 1<=k[-1]<=200]))))>170:
						print [l for l in range(1,201) if l not in (list(set([k[-1] for k in possibleExponentiations if 1<=k[-1]<=200])))]
				count+=1
def euler123():
	primes=primeGenerate(10000000)
	print primes[0:10]
	print len(primes)
	def r(n):
		a=primes[n]
		return (1+a*n+(-1)**n+a*n*(-1)**(n-1))%(a*a)
	for i in range(len(primes)):
		if r(i)>1e10: print i+2, r(i); break
def euler124():
	def primeFactor(k):
		primes=primeGenerate(1000)
		out=[]
		for p in primes:
			while k%p==0:
				out.append(p)
				k/=p
		if k!=1: out.append(k)
		k=1
		for i in set(out):
			k*=i
		return k
	out2=[]
	for i in range(1,100001):
		out2.append((i,primeFactor(i)))
		if i%100==0: print i
	out3=[]
	print len(set([j[1] for j in out2]))
	for i in sorted(set([j[1] for j in out2])):
		if i%100==0: print i
		temp=[]
		for j in [k for k in out2 if k[1]==i]:
			temp.append(j[0])
		for k in sorted(temp):
			out3.append([k,i])
		if len(out3)>10000: print out3[9999]
def euler125():
	def f(n,k): # returns sum of (n+i)^2 from i=0 to k
		return ((k+1)*(2*k*k+6*n*k+k+6*n*n))/6
	sums=[]
	for n in range(1,10000):
		print n
		for k in range(1,701):
			temp=f(n,k)
			if temp<100000000:
				sums.append(temp)
	print len(sums)
	palindromes=[]
	for i in range(len(sums)):
		if i%100==0: print i
		if str(sums[i])[::-1]==str(sums[i]):
			palindromes.append(sums[i])
	print sum(list(set(palindromes)))
def euler128():
	ring_indicies=[1]+[0]*999
	for n in range(1,len(ring_indicies)):
		ring_indicies[n]=ring_indicies[n-1]+6*n-6
	def nth_ring(k):
		k=k-1
		for i in range(len(ring_indicies)):
			if ring_indicies[i+1]>k: return i
	for i in range(1000):
		print i, nth_ring(i)
def euler129():
	def a(n): # as defined in problem
		if n%2==0 or n%5==0 or n<2: return 0
		else:
			x=1
			k=1
			while x!=0:
				x=(10*x+1)%n
				k+=1
			return k
	t=1000000
	while a(t)<1000000:
		t+=1
	print t
def euler130():
	def isPrime(p):
		if p<=1: return False
		out = True
		for i in range(2,int(p**0.5)+1):
			if p%i==0:
				out = False
				break
		return (out)
	def a(n): # as defined in problem
		if n%2==0 or n%5==0 or n<2: return 0
		else:
			x=1
			k=1
			while x!=0:
				x=(10*x+1)%n
				k+=1
			return k
	q=[]
	b=5
	while len(q)<25:
		if isPrime(b)==False and a(b)!=0 and (b-1)%a(b)==0: q.append(b)
		b+=1
		print b
	print sum(q)
def euler132():
	def isPrime(p):
		if p<=1: return False
		out = True
		for i in range(2,int(p**0.5)+1):
			if p%i==0:
				out = False
				break
		return (out)
	p=3
	out=[]
	while len(out)<40:
		if pow(10,1000000000,9*p)==1 and isPrime(p): out.append(p)
		p+=2
	print sum(out)
def euler133():
	def r(n,p):
		return (pow(9,p-2,p)*(pow(10,10**n,p)-1))%p
	def check(p):
		if all([p%j!=0 for j in range(2,int(p**0.5)+2)]):
			for i in range(2,p+1):
				if r(i,p)==0: return False; break
				if r(i,p)==r(i-1,p): return True; break
			return True
		return False
	print check(11),check(17),check(19),check(20)
	#print sum([i for i in range(11,100000) if all([(pow(9,p-2,p)*(pow(10,10**n,p)-1))%p!=0 for n in range(1,p+1)])and(all([p%j!=0 for j in range(2,int(p**0.5)+2)]))])
	total=0
	for i in range(11,100000):
		if check(i): total+=i
		if i%100==0: print i
	print total
def euler134():
	import time
	start=time.time()
	def s(p1,p2):
		for i in range(1,p2+1):
			if int(str(i)+str(p1))%p2==0: return int(str(i)+str(p1))
	primes=primeGenerate(1000000)
	print len(primes)-1
	total=0
	for i in range(2,len(primes)-1):
		if i%100==0: print str(i)+"/78500"
		total+=s(primes[i],primes[i+1])
	print total
	print time.time()-start
def euler137():
	"""
	k=x/(1-x-x^2)
	k-kx-kx^2=x
	kx^2+kx-k=-x
	x^2*k+x*(k+1)-k=0
	given k, find x
	x= (-(k+1) + sqrt(discriminant))/(2*k)
	where discriminant=(k+1)^2+4k^2=5k^2+2k+1
	"""
	from math import sqrt
	def f(k):
		k=float(k)
		return (sqrt(5*k*k+2*k+1)-(k+1))/(2*k)
	def isSquare(x):
		return int(x**0.5)**2==x
	
	for i in range(1,1000000): 
		if isSquare(5*i*i+2*i+1): print i
	# solutions to 5x^2+2x+1-y^2=0
	xx=[]
	def f(x0,y0):
		x=[0]*50
		y=[0]*50
		x[0]=x0
		y[0]=y0
		for i in range(len(x)-1):
			x[i+1]=-9*x[i]+-4*y[i]+-2
			y[i+1]=-20*x[i]+-9*y[i]+-4
		for element in [i for i in x if i>0]:
			xx.append(element)
	#f(-1,-2)
	f(-1,2)
	#f(0,-1)
	f(0,1)
	#f(2,-5)
	f(2,5)
	print sorted(xx)[14]
def euler140():
	"""
	k=(x+3x2)/(1-x-x2)
	k-k*x-k*x^2=x+3x^2
	-k+kx+kx2=-x-3x2
	-k+(k+1)x+(k+3)x2=0
	(k+3)x2+(k+1)x-k=0
	x=(1/(2k+6)) * (-k-1+sqrt(discriminant))
	where discriminant=(k+1)^2 + 4 * (k+3) * k = 5k^2+14k+1
	"""
	from math import sqrt
	def f(k):
		k=float(k)
		return (sqrt(5*k*k+14*k+1)-(k+1))/(2*k+6)
	def isSquare(x):
		return int(x**0.5)**2==x
	
	for i in range(1,1000000): 
		if isSquare(5*i*i+14*i+1): print i
	# solutions to 5x^2+14x+1-y^2=0
	xx=[]
	def f(x0,y0):
		x=[0]*50
		y=[0]*50
		x[0]=x0
		y[0]=y0
		for i in range(len(x)-1):
			x[i+1]=-9*x[i]+-4*y[i]+-14
			y[i+1]=-20*x[i]+-9*y[i]+-28
		for element in [i for i in x if i>0]:
			xx.append(element)
	temp=1000
	for x in range(-temp,temp+1):
		for y in range(-temp,temp+1):
			if 5*x*x+14*x+1-y*y==0: print x,y
	f(-4,5)
	f(-3,2)
	f(0,1)
	f(2,7)
	f(5,14)
	f(21,50)
	f(42,97)
	f(152,343)
	f(296,665)
	print sum(sorted(set(xx))[0:30])
def euler141():
    """
    n = d * q + r
    where d,q,r are geometric sequence
    q<r<d
    
    let common ratio be rational: a/b
    r = qa/b
    d = ra/b
    
    """
    def f(n,d):
        q=n//d
        r=n%d
        print "d=",d,"q=",q,"r=",r
    randomnumbers = [1,4,5,3,6,12]
    for i in randomnumbers:
        for j in randomnumbers:
            f(i,j)
euler141()
"""
def euler129(): # takes too long
        from fractions import gcd
        def repunit_mod(i,n):
                # returns R(i) mod n
                temp = pow(10,i,n)-1
                for i in range(1,n):
                        if (9*i)%n==1:
                                break
                temp*=i
                return temp%n
        def a(n):
                if gcd(n,10)!=1: return 1
                else:
                        i=max(1,len(str(n))-1)
                        count=1
                        while True:
                                if repunit_mod(i,n)==0:
                                        break
                                i+=1
                                if count%10==0: print count
                                count+=1
                        return
        i=999999
        while True:
                if a(i)>1000000:
                        print i,"***"; break
                print i,a(i)
                i+=1
        print a(99)
def euler130(): # also is too slow
        from fractions import gcd
        def repunit_mod(i,n):
                # returns R(i) mod n
                temp = pow(10,i,n)-1
                for i in range(1,n):
                        if (9*i)%n==1:
                                break
                temp*=i
                return temp%n
        def a(n):
                if gcd(n,10)!=1: return 1
                else:
                        i=max(1,len(str(n))-1)
                        count=1
                        while True:
                                if repunit_mod(i,n)==0:
                                        break
                                i+=1
                                count+=1
                        return i
        composites=[]
        for i in range(1000000):
                if isPrime(i)==False: composites.append(i)
                if i%1000==0: print i
        out=[]
        for i in composites:
                #print i
                if i>1 and (i-1)%a(i)==0 and i%2!=0 and i%5!=0:
                        print i,"*"; out.append(i)
                if len(out)==29: break
        print sum(out)-3-9-33-99
"""

