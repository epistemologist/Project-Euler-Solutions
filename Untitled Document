def isPrime(p):
	if p<=1: return False
	out = True
	i=2
	while i<=int(p**0.5)+1:
		if p%i==0:
			out = False
			break
		i+=1
	return (out)
def primeGenerate(limit): # from rosettacode
	is_prime = [False] * 2 + [True] * (limit - 1)
	for n in range(int(limit**0.5 + 1.5)):
		if is_prime[n]:
			for i in range(n*n, limit+1, n):
				is_prime[i] = False
	return [i for i, prime in enumerate(is_prime) if prime]
def miller_rabin(p):
	if p==2: return True
	if p%2==0: return False
	else:
		d=p-1
		s=0
		while d%2==0:
			d/=2
			s+=1
		for a in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
			temp=[]
			for r in range(s):
				 temp.append(pow(a,d,p)!=1 and pow(a,2**r*d,p)!=(p-1))
		return not(all(temp))

def euler141():
	"""
	n=d*q+r
	n//d=q
	n%d=r
	
	q = r * k
	d = q * k = r * k*k
	n = d*q+r = r*r*k*k*k+r = r(r*k^3+1)
	
	but n is square number - let n=t*t
	t*t=r*(r*k^3+1), r, (r*k*k*k+1) are square
	k is rational: let k=a/b
	q = a*r/b
	d = r*a*a/(b*b)
	n = r * (r*a^3/b^3+1)
	"""
def euler142():
	"""
	a=x+y
	b=x-y
	c=x+z
	d=x-z
	e=y+z
	f=y-z
	{a>b,c>d,e>f,a>c,d>b,c>e}
	b+f=d
	b+e=c
	b=a-f-e
	x=(a+b)/2
	y=(e+f)/2
	z=c-x
	"""
	def isSquare(n):
		if n<0: return False
		else: return n==int(n**0.5)**2
	cap=1000
	max_sum=0
	for i in range(1,cap):
		print i, max_sum
		for j in range(1,i):
			for k in range(1,j):
				a=i*i
				e=j*j
				f=k*k
				b=a-f-e
				c=b+e
				d=b+f
				x=(a+b)/2
				y=(e+f)/2
				z=c-x
				if (a+b)%2==0 and (e+f)%2==0 and all([isSquare(n) for n in [b,c,d]]) and x!=y!=z:
					print sum([x,y,z]); break; break; break; break
				if max_sum<x+y+z: max_sum=x+y+z
def euler144():
	from math import sqrt
	"""
	E (ellipse): 4x^2+y^2=100
	l0: y-10.1=mx where m=-19.7/1.4
	
	intersection of line y-y0=m(x-x0) with E
	y = m*x-m*x0+y0
	4*x^2+(m*x-m*x0+y0)^2=100
	
	x_new, y_new
	slope=y/4x
	"""
	x0=0.
	y0=10.1
	m=-19.7/1.4
	# x1=((-(2*sqrt(-m^(2)*(x0^(2)-25)+2*m*x0*y0-y0^(2)+100)-m*(m*x0-y0)))/(m^(2)+4)) and y1=((-2*(m*sqrt(-m^(2)*(x0^(2)-25)+2*m*x0*y0-y0^(2)+100)+2*(m*x0-y0)))/(m^(2)+4)) or x2=((2*sqrt(-m^(2)*(x0^(2)-25)+2*m*x0*y0-y0^(2)+100)+m*(m*x0-y0))/(m^(2)+4)) and y2=((2*(m*sqrt(-m^(2)*(x0^(2)-25)+2*m*x0*y0-y0^(2)+100)-2*(m*x0-y0)))/(m^(2)+4))|x0=1.4 and y0=-9.6 and m=((y0)/(4*x0))
	count=2
	while True:
		x1=((-(2*sqrt(-m**(2)*(x0**(2)-25)+2*m*x0*y0-y0**(2)+100)-m*(m*x0-y0)))/(m**(2)+4))
		y1=((-2*(m*sqrt(-m**(2)*(x0**(2)-25)+2*m*x0*y0-y0**(2)+100)+2*(m*x0-y0)))/(m**(2)+4)) 
		x2=((2*sqrt(-m**(2)*(x0**(2)-25)+2*m*x0*y0-y0**(2)+100)+m*(m*x0-y0))/(m**(2)+4))
		y2=((2*(m*sqrt(-m**(2)*(x0**(2)-25)+2*m*x0*y0-y0**(2)+100)-2*(m*x0-y0)))/(m**(2)+4))
		if abs(x0-x1)>abs(x0-x2):
			x=x1
			y=y1
		else:
			x=x2
			y=y2
		tanA=m
		tanB=y/(4.*x)
		tan2B=(-2*tanB)/(1-tanB*tanB)
		m=(tanA+tan2B)/(1-tanA*tan2B)
		x0=x
		y0=y
		count+=1
		print count,x0,y0,m
		if abs(x0)<0.01: break
def euler146():
	# n^2+k is prime where k=1,3,7,9,13,27
	"""
	n cannot be a cube
	n has to be even
	
	all twin primes are in form of (6n-1,6n+1)
	
	"""
