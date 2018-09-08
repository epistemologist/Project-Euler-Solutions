def fibonacci(n):
	if 0<n<3: return n
	else: return fibonacci(n-1)+fibonacci(n-2)
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
def numberDivisors(n):
	count = 0
	for i in range(1,int(n**0.5)+1):
		if n%i==0: count+=2
	a = int(count-(n**0.5)%1.0)-1
	if a==0: return 2
	else: return a
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
def euler1():
	total = 0
	for i in range(1000):
		if (i%3==0 or i%5==0):
			total+=i
	print total
def euler2():
	total = 0
	i = 1
	flag = True
	while flag:
		fib = fibonacci(i)
		if fib>4000000: flag = False
		if fib%2==0: total+=fib
		i+=1
	print total
def euler3():
	n = 600851475143
	p = 3
	while True:
		if n%p==0: n/=p
		p+=2
		if (n<1000000):
			if isPrime(n): break
	print n
def euler4():
	maxProduct = 0
	for i in range(1000):
		for j in range(1000):
			if (str(i*j)==str(i*j)[::-1]) and (i*j>maxProduct):
				maxProduct=i*j
	print maxProduct
def euler5():
	print 2**4*3**2*5*7*11*13*17*19
def euler6():
	sumOfSquares=100*(100+1)*(2*100+1)/6
	squareOfSum=(100/2*101)**2
	print abs(sumOfSquares-squareOfSum)
def euler7():
	primes = [2]
	p=3
	while len(primes)<10001:
		if isPrime(p): primes.append(p)
		p+=2
	print primes[10000]
def euler8():
	n="73167176531330624919225119674426574742355349194934 96983520312774506326239578318016984801869478851843 85861560789112949495459501737958331952853208805511 12540698747158523863050715693290963295227443043557 66896648950445244523161731856403098711121722383113 62229893423380308135336276614282806444486645238749 30358907296290491560440772390713810515859307960866 70172427121883998797908792274921901699720888093776 65727333001053367881220235421809751254540594752243 52584907711670556013604839586446706324415722155397 53697817977846174064955149290862569321978468622482 83972241375657056057490261407972968652414535100474 82166370484403199890008895243450658541227588666881 16427171479924442928230863465674813919123162824586 17866458359124566529476545682848912883142607690042 24219022671055626321111109370544217506941658960408 07198403850962455444362981230987879927244284909188 84580156166097919133875499200524063689912560717606 05886116467109405077541002256983155200055935729725 71636269561882670428252483600823257530420752963450".replace(" ","")
	def product(i):
		out=1
		for j in range(13):
			out*=int(n[i+j])
		return out
	output=0
	for i in range(987):
		if product(i)>output:
			output=product(i)
	return output
def euler9():
	import math
	for a in range(1000):
		b=1000*(a-500)/(a-1000) # solving system {a+b+c=1000, a2+b2=c2} for b knowing a
		if a*a+b*b==(1000-a-b)**2 and a<b and a>0 and b>0: print a*b*(1000-a-b)
def euler10():
	total = 2
	p = 3
	while p<2000000:
		if isPrime(p): total+=p
		#if p%1000==3: print p
		p+=2
	print total
def euler11():
	text = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
	a = [int(i) for i in text.split(" ")]
	maxProduct = 0
	for i in [j for j in range(400) if (0<=j%20<=15)]:
		if a[i]*a[i+1]*a[i+2]*a[i+3]>maxProduct:
			maxProduct=a[i]*a[i+1]*a[i+2]*a[i+3] # horizontal
	for i in range(320):
		if a[i]*a[i+20]*a[i+40]*a[i+60]>maxProduct:
			maxProduct=a[i]*a[i+20]*a[i+40]*a[i+60] # vertical
	for i in [j for j in range(320) if (0<=j%20<=15)]:
		if a[i]*a[i+21]*a[i+42]*a[i+63]>maxProduct:
			maxProduct=a[i]*a[i+21]*a[i+42]*a[i+63]#SE
	for i in [j for j in range(320) if (4<=j%20<=19)]:
		if a[i]*a[i+19]*a[i+38]*a[i+57]>maxProduct:
			maxProduct=a[i]*a[i+19]*a[i+38]*a[i+57]
	print maxProduct
def euler12():
	import matplotlib.pyplot as plt
	i = 0
	divisors = numberDivisors((i*(i+1))/2)
	y=[]
	x=[]
	while divisors<=500:
		i+=1
		divisors = numberDivisors((i*(i+1))/2)
		y.append(divisors)
		x.append(i)
		if i%1000==0: print i, (i*(i+1))/2, divisors
	plt.scatter(x,y)
	plt.show()
	print (i*(i+1))/2
def euler13():
	numbers="37107287533902102798797998220837590246510135740250 46376937677490009712648124896970078050417018260538 74324986199524741059474233309513058123726617309629 91942213363574161572522430563301811072406154908250 23067588207539346171171980310421047513778063246676 89261670696623633820136378418383684178734361726757 28112879812849979408065481931592621691275889832738 44274228917432520321923589422876796487670272189318 47451445736001306439091167216856844588711603153276 70386486105843025439939619828917593665686757934951 62176457141856560629502157223196586755079324193331 64906352462741904929101432445813822663347944758178 92575867718337217661963751590579239728245598838407 58203565325359399008402633568948830189458628227828 80181199384826282014278194139940567587151170094390 35398664372827112653829987240784473053190104293586 86515506006295864861532075273371959191420517255829 71693888707715466499115593487603532921714970056938 54370070576826684624621495650076471787294438377604 53282654108756828443191190634694037855217779295145 36123272525000296071075082563815656710885258350721 45876576172410976447339110607218265236877223636045 17423706905851860660448207621209813287860733969412 81142660418086830619328460811191061556940512689692 51934325451728388641918047049293215058642563049483 62467221648435076201727918039944693004732956340691 15732444386908125794514089057706229429197107928209 55037687525678773091862540744969844508330393682126 18336384825330154686196124348767681297534375946515 80386287592878490201521685554828717201219257766954 78182833757993103614740356856449095527097864797581 16726320100436897842553539920931837441497806860984 48403098129077791799088218795327364475675590848030 87086987551392711854517078544161852424320693150332 59959406895756536782107074926966537676326235447210 69793950679652694742597709739166693763042633987085 41052684708299085211399427365734116182760315001271 65378607361501080857009149939512557028198746004375 35829035317434717326932123578154982629742552737307 94953759765105305946966067683156574377167401875275 88902802571733229619176668713819931811048770190271 25267680276078003013678680992525463401061632866526 36270218540497705585629946580636237993140746255962 24074486908231174977792365466257246923322810917141 91430288197103288597806669760892938638285025333403 34413065578016127815921815005561868836468420090470 23053081172816430487623791969842487255036638784583 11487696932154902810424020138335124462181441773470 63783299490636259666498587618221225225512486764533 67720186971698544312419572409913959008952310058822 95548255300263520781532296796249481641953868218774 76085327132285723110424803456124867697064507995236 37774242535411291684276865538926205024910326572967 23701913275725675285653248258265463092207058596522 29798860272258331913126375147341994889534765745501 18495701454879288984856827726077713721403798879715 38298203783031473527721580348144513491373226651381 34829543829199918180278916522431027392251122869539 40957953066405232632538044100059654939159879593635 29746152185502371307642255121183693803580388584903 41698116222072977186158236678424689157993532961922 62467957194401269043877107275048102390895523597457 23189706772547915061505504953922979530901129967519 86188088225875314529584099251203829009407770775672 11306739708304724483816533873502340845647058077308 82959174767140363198008187129011875491310547126581 97623331044818386269515456334926366572897563400500 42846280183517070527831839425882145521227251250327 55121603546981200581762165212827652751691296897789 32238195734329339946437501907836945765883352399886 75506164965184775180738168837861091527357929701337 62177842752192623401942399639168044983993173312731 32924185707147349566916674687634660915035914677504 99518671430235219628894890102423325116913619626622 73267460800591547471830798392868535206946944540724 76841822524674417161514036427982273348055556214818 97142617910342598647204516893989422179826088076852 87783646182799346313767754307809363333018982642090 10848802521674670883215120185883543223812876952786 71329612474782464538636993009049310363619763878039 62184073572399794223406235393808339651327408011116 66627891981488087797941876876144230030984490851411 60661826293682836764744779239180335110989069790714 85786944089552990653640447425576083659976645795096 66024396409905389607120198219976047599490197230297 64913982680032973156037120041377903785566085089252 16730939319872750275468906903707539413042652315011 94809377245048795150954100921645863754710598436791 78639167021187492431995700641917969777599028300699 15368713711936614952811305876380278410754449733078 40789923115535562561142322423255033685442488917353 44889911501440648020369068063960672322193204149535 41503128880339536053299340368006977710650566631954 81234880673210146739058568557934581403627822703280 82616570773948327592232845941706525094512325230608 22918802058777319719839450180888072429661980811197 77158542502016545090413245809786882778948721859617 72107838435069186155435662884062257473692284509516 20849603980134001723930671666823555245252804609722 53503534226472524250874054075591789781264330331690"
	total=sum([int(i) for i in numbers.split(" ")])
	print str(total)[0:10]
used_numbers=[]
def euler14():
	import time
	start = time.time()
	def collatz_length(n):
		counter = 1
		while n!=1:
			if n%2==0:
				n/=2
				counter+=1
			else:
				n=3*n+1
				counter+=1
		return counter
	num=0
	maxLength=0
	for i in range(1,1000001):
		length=collatz_length(i)
		if length>maxLength:
			num=i
			maxLength=length
		if i%10000==0: print i
	print num, maxLength
	print time.time()-start
def euler15():
	def factorial(n):
		if 0<n<3: return n
		else: return n*factorial(n-1)
	print factorial(40)/factorial(20)/factorial(20)
def euler16():
	print sum([int(i) for i in str(2**1000)])
def euler17():
	units=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	def n2ws(n): #number to word (small)
		if 1<=n<=19: return units[n]
		elif 20<=n<=99: return tens[n//10]+" "+units[n%10]
		elif n==1000: return "one thousand"
		elif n%100==0: return units[n/100]+" hundred"
		else: return units[n//100]+" hundred and "+n2ws(n%100)
	out=""
	for i in range(1,1001):
		out+=n2ws(i)
	print len(out.replace(" ",""))
def euler18():
	def triangle(lis):
		out=[]
		i=0
		while ((i+1)*(i+2))/2<=len(lis):
			out.append(lis[int(i*(i+1)*0.5):int((i+1)*(i+2)*0.5)])
			i+=1
		return out
	def newRow(currentRow, prevRow):
		out = []
		for i in range(len(prevRow)):
			out.append(max(prevRow[i]+currentRow[i],prevRow[i]+currentRow[i+1]))
		return out
	text = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
	triangleNum = triangle([int(i) for i in text.split(" ")])
	while len(triangleNum)>1:
		tempRow = newRow(triangleNum[-1],triangleNum[-2])
		triangleNum.remove(triangleNum[-1])
		triangleNum[-1]=tempRow
	print triangleNum[0][0]
def euler19():
	total=0
	from datetime import date
	for year in range(1901,2001):
		for month in range(1,13):
			if date(year,month,1).weekday()==6:
				total+=1
	print total
def euler20():
	def factorial(n):
		if 0<n<3: return n
		else: return n*factorial(n-1)
	print sum([int(i) for i in str(factorial(100))])
def euler21():
	def sumOfDivisors(n):
		if 0<n<=3: return 1
		else:
			divisors=[]
			for i in range(1,int(n**0.5)):
				if n%i==0:
					divisors.append(i)
					divisors.append(n/i)
			return sum(list(set(divisors)))-n
	total=0
	print sumOfDivisors(2)
	for i in range(10000):
		if sumOfDivisors(sumOfDivisors(i))==i and sumOfDivisors(i)!=i:
			total+=i
	print total
def euler22():
	import urllib2
	text=sorted([i.replace("\"","") for i in urllib2.urlopen("https://projecteuler.net/project/resources/p022_names.txt").read().split(",")])
	total=0
	for i in range(len(text)):
		total+=(i+1)*(sum([ord(j)-64 for j in text[i]]))
	print total
def euler23(): # takes too long
	import itertools
	import time
	start = time.time()
	def sumOfDivisors(n):
		if 0<n<=3: return 1
		else:
			divisors=[]
			for i in range(1,int(n**0.5)+1):
				if n%i==0:
					divisors.append(i)
					divisors.append(n/i)
			return sum(list(set(divisors)))-n
	abundantNumbers=[i for i in range(1,30000) if sumOfDivisors(i)>i]
	print abundantNumbers[0:99]
	def testAbundantSum(n):
		differences = [(n-i) for i in abundantNumbers if i<n]
		#return [i in abundantNumbers for i in differences].count(True)!=0
		for i in differences:
			if i in abundantNumbers: return True
		return False
	total=0
	for i in range(1,28124):
		if testAbundantSum(i)==False:
			total+=i
		if i%200==0: print i
	print total
	print time.time()-start
def euler24():
	import itertools
	print list(itertools.permutations("0123456789",10))[999999]
def euler25():
	def fib(x):
		fibs=[1,1]
		while len(fibs)<x:
			fibs.append(fibs[-1]+fibs[-2])
		return fibs[x-1]
	i=1
	while len(str(fib(i)))<1000:
		i+=1
	print i
def euler26():
	def decimal_period_length(n):
		if n%2==0 or n%5==0 or n==1: return 0
		else:
			i=1
			while (10**i)%n!=1:
				i+=1
			return i
	temp=[decimal_period_length(i) for i in range(1000)]
	print temp.index(max(temp))
def euler27():
	def modFilter(a,b):
		if not(a%2==0 and b%2==1): return False
		elif not((b%3==1 and a%3==1)or(b%3==2 and a%3!=0)): return False
		elif (a<0 and b<0): return False
		else: return True
	maxPrime,maxA,maxB=0,0,0
	for a in range(-1000,1001):
		for b in range(-1000,1001):
			if (isPrime(b) and ((b==2 and a%2==0) or (a%2==1))):
				i=0
				while isPrime(abs(i*i+a*i+b)):
					i+=1
				if i>maxPrime:
					maxPrime,maxA,maxB=i,a,b
	print maxA*maxB
def euler28():
	def sumOfRing(n):
		if n==0: return 1
		else:
			return (2*n+1)**2+(2*n+1)**2-(2*n)+(2*n+1)**2-(4*n)+(2*n+1)**2-(6*n)
	total=0
	numberOfRings=500
	for i in range(0,numberOfRings+1):
		total+=sumOfRing(i)
	print total
def euler29():
	return len(list(set([a**b for a in range(2,101) for b in range(2,101)])))
def euler30():
	total=0
	for i in range(2,5*9**5):
		if sum([int(j)**5 for j in str(i)])==i:
			total+=i
			print i
	print total
def euler31():
	import sympy
	print int(sympy.mpmath.chop(sympy.mpmath.taylor(lambda x: 1/((1-x)*(1-x**2)*(1-x**5)*(1-x**10)*(1-x**20)*(1-x**50)*(1-x**100)),0,200))[-1])+1
def euler32():
	import itertools
	products=[]
	# assume all pandigital products are in the form of 2digit*3digit=4digit and 1digit*4digit=4digit
	for i in range(1,10):
		digitsLeft=[j for j in range(1,10) if j!=i]
		fourDigit=[1000*j[0]+100*j[1]+10*j[2]+j[3] for j in list(itertools.permutations(digitsLeft,4))]
		for j in fourDigit:
			if sorted(str(i*j)+str(i)+str(j))==list("123456789"):
				products.append(i*j)
	for i in range(1,100):
		digitsLeft=[j for j in range(1,10) if j!=i//10 and j!=i%10]
		threeDigit=[100*j[0]+10*j[1]+j[2] for j in list(itertools.permutations(digitsLeft,3))]
		for j in threeDigit:
			if sorted(str(i*j)+str(i)+str(j))==list("123456789"):
				products.append(i*j)
	print sum(list(set(products)))
def euler33():
	from fractions import gcd
	def reduc(p,q):
		return (p/gcd(p,q),q/gcd(p,q))
	def cancelableFraction(p,q):
		pp=p/gcd(p,q)
		qq=q/gcd(p,q)
		a=p//10
		b=p%10
		c=q//10
		d=q%10
		if a==c:
			return (pp,qq)==reduc(b,d)
		elif a==d:
			return (pp,qq)==reduc(b,c)
		elif b==c:
			return (pp,qq)==reduc(a,d)
		elif b==d:
			return (pp,qq)==reduc(a,c)
		else:
			return False
	num=1
	den=1
	for p in range(10,100):
		for q in range(10,100):
			if not(p%10==0 and q%10==0) and not(p%11==0 and q%11==0) and p<q:
				if cancelableFraction(p,q):
					num*=p
					den*=q
	print reduc(num,den)[1]
def euler34():
	def factorial(n):
		if n<=1: return n**n
		else: return n*factorial(n-1)
	total=0
	for i in range(1000000):
		if i==sum([factorial(int(j)) for j in str(i)]): total+=i
	print total-3
def euler35():
	def rotations(n):
		n=[i for i in str(n)]
		out=[]
		for i in range(len(n)):
			out.append(n[i:]+n[:i])
		return [int("".join(i)) for i in out]
	count=0
	for i in range(1000000):
		if isPrime(i):
			if all([isPrime(j) for j in rotations(i)]):
				count+=1
				print i
		if i%1000==0: print i,"index"
	print count
def euler36():
	total=0
	for i in range(1000000):
		b=bin(i)[2:]
		if (str(i)[::-1]==str(i)) and b[::-1]==b:
			total+=i
			print i
	print total
def euler37():
	def isTruncatablePrime(p):
		q=str(p)
		if (("0"in q)or("2"in q)or("4"in q)or("5"in q)or("6"in q)or("8"in q))and(p>100): return False
		elif isPrime(p)==False: return False
		else:
			for i in range(1,len(str(p))):
				if not(isPrime(int(str(p)[i:]))) or not(isPrime(int(str(p)[:i]))): return False
			return True
	truncPrimes=[]
	k=11
	while len(truncPrimes)<11:
		if isTruncatablePrime(k): truncPrimes.append(k)
		k+=2
		if k%200==1: print k, truncPrimes, sum(truncPrimes)
	print sum(truncPrimes)
def euler38():
	def f(n):
		out=""
		k=1
		while len(out)<9:
			out+=str(n*k)
			k+=1
		if sorted(out)==list("123456789"):
			return int(out)
			print out
		else:
			return 0
	maxPan=0
	print max([f(i) for i in range(10000)])
def euler39():
	from fractions import gcd
	primitivetriples=[]
	for n in range(1,1001):
		for m in range(n,1001):
			if gcd(m,n)==1:
				primitivetriples.append((m*m-n*n,2*m*n,m*m+n*n))
	triples=[]
	for triple in primitivetriples:
		a0=triple[0]
		b0=triple[1]
		c0=triple[2]
		i=1
		while i*(a0+b0+c0)<=1000:
			triples.append([a0*i,b0*i,c0*i])
			i+=1
	triples=[sorted(i) for i in triples if sum(i)<=1000]
	tripleSums=[sum(i) for i in triples]
	maxSolutions=0
	maxCount=0
	for i in range(1001):
		if tripleSums.count(i)>maxCount:
			maxSolutions=i
			maxCount=tripleSums.count(i)
	print maxSolutions
def euler40():
	d=""
	k=1
	while len(d)<1000000:
		d+=str(k)
		k+=1
	d=[int(i) for i in d]
	print d[0]*d[9]*d[99]*d[999]*d[9999]*d[99999]*d[999999]
def euler41():
	import itertools
	print max([int("".join(i)) for i in list(itertools.permutations("1234567")) if isPrime(int("".join(i)))])
	"""
	primes=[]
	for i in list(itertools.permutations("123456789")):
	if isPrime(int("".join(i))):
	primes.append(i)
	print i
	print max(primes)
	"""
def euler42():
	def isTri(n):
		return ((8*n+1)**0.5)%1==0
	def wordValue(word):
		return sum([ord(i)-64 for i in word])
	import urllib2
	text=sorted([i.replace("\"","") for i in urllib2.urlopen("https://projecteuler.net/project/resources/p042_words.txt").read().split(",")])
	count=0
	for i in range(len(text)):
		if isTri(wordValue(text[i])):
			count+=1
	print count
def euler43():
	def checkSubstringDivis(n):
		return (int(n[1:4])%2==0)and(int(n[2:5])%3==0)and(int(n[3:6])%5==0)and(int(n[4:7])%7==0)and(int(n[5:8])%11==0)and(int(n[6:9])%13==0)and(int(n[7:10])%17==0)
	import itertools
	total=0
	for i in list(itertools.permutations("0123456789")):
		string="".join(i)
		if checkSubstringDivis(string):
			total+=int(string)
	print total
def euler44():
	def p(n):
		return (n*(3*n-1))/2
	def isPentagonal(n):
		return ((24*n+1)**0.5+1)%6==0
	flag=False
	for i in range(1,100000):
		if flag: break
		for j in range(1,i):
			if isPentagonal(p(i)+p(j)) and isPentagonal(abs(p(i)-p(j))):
				print p(i)-p(j)
				flag=True
def euler45():
	def isPentagonal(n):
		return ((24*n+1)**0.5+1)%6==0
	def isHexagonal(n):
		return ((8*n+1)**0.5+1)%4==0
	for i in range(1000000):
		t=(i*(i+1))/2
		if isPentagonal(t) and isHexagonal(t) and t>40755:
			print t
			break
def euler46():
	def check(n):
		primes=[i for i in range(n) if isPrime(i)]
		return any([(((n-i)/2.)**0.5)%1==0 for i in primes])
	for i in range(3,100000,2):
		if i%15==0: print i,"index"
		if isPrime(i)==False and check(i)==False:
			print i
			break
			
def euler47():
	def numPrimeFactors(n):
		num = []
		while(n%2 == 0):
			num.append(2)
			n /= 2
		for i in xrange(3, int(n**0.5)+1, 2):
			while (n%i == 0):
				num.append(i)
				n /= i
		if n>2:
			num.append(n)
		return len(set(num))
	i=2
	while True:
		a=numPrimeFactors(i)
		b=numPrimeFactors(i+1)
		c=numPrimeFactors(i+2)
		d=numPrimeFactors(i+3)
		if a==b==c==d==4:
			print i
			break
		i+=1
def euler48():
	return int(str(sum([i**i for i in range(1,1001)])%(10**10)))
def euler49():
	import itertools
	def check(i):
		strs=list(itertools.combinations(list(itertools.permutations(i)),3))
		strs=[[int("".join(j)) for j in i] for i in strs]
		strs=[sorted(i) for i in strs]
		strs=[i for i in strs if ((i[1]-i[0])==(i[2]-i[1]))and(all([isPrime(j) for j in i]))and(i[0]!=i[1])and(i[1]!=i[2])]
		return strs
	out=[]
	for i in range(1000,10000):
		temp=check(list(str(i)))
		if len(temp)>0: out.append(temp)
		print i
	print out
def euler50():
	primes=primeGenerate(1000000)
	print len(primes)
	sums=[]
	for i in range(len(primes)-1):
		j=i+1
		temp=primes[i:j]
		while sum(temp)<=1000000:
			sums.append([sum(temp),len(temp)])
			j+=1
			temp=primes[i:j]
		if i%100==0: print i
	maxPrimeSum=0
	maxPrimeCount=0
	print len(sums)
	for i in sums:
		if (isPrime(i[0]) and i[1]>maxPrimeCount):
			maxPrimeSum=i[0]
			maxPrimeCount=i[1]
	print maxPrimeCount,maxPrimeSum
def euler51():
	def b11(n):
		out=[]
		while n>0:
			out=[n%11]+out
			n//=11
		out2=""
		for i in out:
			if i==10: out2+="*"
			else: out2+=str(i)
		return out2
	i=1
	flag=True
	while flag:
		temp=b11(i)
		if temp.count("*")==3:
			primeFamily=[int(temp.replace("*",str(j))) for j in range(10)]
			if [isPrime(k) for k in primeFamily].count(True)==8: print min([l for l in primeFamily if isPrime(l)]); flag=False
			if i%1000==0: print primeFamily
		i+=1
	"""
	for i in range(1,50):
		temp=[int(str(j)*i)%3 for j in range(10)]
		print i,temp.count(0),temp.count(1),temp.count(2)
	"""#shows that there must be 3,6,... repeated digits
def euler52():
	for i in range(1,1000000):
		if sorted(str(i))==sorted(str(2*i))==sorted(str(3*i))==sorted(str(4*i))==sorted(str(5*i))==sorted(str(6*i)):
			print i
			break
def euler53():
	def factorial(n):
		if 0<=n<=2: return n
		else: return n*factorial(n-1)
	def ncr(n,k):
		return factorial(n)/factorial(k)/factorial(n-k)
	count=0
	for i in range(1,101):
		for j in range(1,101):
			if i>j and ncr(i,j)>1000000:
				count+=1
	print count
def euler54():
	def hasRoyalFlush(hand):
		values=[card[0] for card in hand]
		suits=[card[1] for card in hand]
		return sorted(values)==sorted(["T","Q","K","J","A"]) and len(set(suits))==1
	def hasStraightFlush(hand):
		values=[card[0] for card in hand]
		possibleValues=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
		suits=[card[1] for card in hand]
		for i in range(0,len(possibleValues)-5):
			if sorted(possibleValues[i:i+5])==sorted(values) and len(set(suits))==1: return possibleValues[i:i+5][-1]
		return False
	def hasFourOfAKind(hand):
		values=[card[0] for card in hand]
		counts=[(i,values.count(i)) for i in set(values)]
		for i in counts:
			if i[1]==4: return i[0]
		return False
	def hasFullHouse(hand):
		values=[card[0] for card in hand]
		counts=[(i,values.count(i)) for i in set(values)]
		counts2=[i[1] for i in counts]
		if sorted(counts2)==[2,3]:
			for i in counts:
				if i[1]==3: return i[0]
		return False
	def hasFlush(hand):
		suits=[card[1] for card in hand]
		values=[card[0] for card in hand]
		if len(set(suits))!=1: return False
		else:
			possibleValues=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
			temp=""
			for i in possibleValues:
				if i in values:
					temp=i
			return i
	def hasStraight(hand):
		values=[card[0] for card in hand]
		possibleValues=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
		for i in range(0,len(possibleValues)-5):
			if sorted(possibleValues[i:i+5])==sorted(values): return possibleValues[i:i+5][-1]
		return False
	def hasThreeOfAKind(hand):
		values=[card[0] for card in hand]
		counts=[(i,values.count(i)) for i in set(values)]
		counts2=[i[1] for i in counts]
		if 3 in counts2:
			for i in counts:
				if i[1]==3: return i[0]
		return False
	def hasTwoPairs(hand):
		values=[card[0] for card in hand]
		counts=[(i,values.count(i)) for i in set(values)]
		counts2=[i[1] for i in counts]
		temp=[]
		temp2=""
		if counts2.count(2)==2:
			for i in counts:
				if i[1]==2: temp.append(i[0])
			possibleValues=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
			for i in possibleValues:
				if i in values:
					temp2=i
			#return temp
			# fudge
			return max([card_to_number(i) for i in temp])
		return False
	def hasOnePair(hand):
		values=[card[0] for card in hand]
		counts=[(i,values.count(i)) for i in set(values)]
		counts2=[i[1] for i in counts]
		temp=[]
		temp2=""
		if counts2.count(2)==1:
			for i in counts:
				if i[1]==2: return i[0]
		return False
	
	def card_to_number(card):
		if type(card)==type(""): card=card[0]
		elif type(card)==type(1): return card
		if card==False: return 0
		possibleValues=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
		for i in range(len(possibleValues)):
			if possibleValues[i]==card: return i+2
	def maxCard(hand):
		return max([card_to_number(card) for card in hand])
	def generate_score(hand):
		return [hasRoyalFlush(hand),hasStraightFlush(hand),hasFourOfAKind(hand),hasFullHouse(hand),hasFlush(hand),hasStraight(hand),hasThreeOfAKind(hand),hasTwoPairs(hand),hasOnePair(hand),maxCard(hand)]
	def compare(outcome1,outcome2):
		outcome1=card_to_number(outcome1)
		outcome2=card_to_number(outcome2)
		if outcome1>outcome2: return 1
		elif outcome1<outcome2: return 2
		else: return 0
	def win(hand1, hand2):
		score1=generate_score(hand1)
		score2=generate_score(hand2)
		for i in range(len(score1)):
			temp=compare(score1[i],score2[i])
			if temp!=0: return temp
	def testFn(hand):
		print "hand: ", hand
		print "royal flush: ", hasRoyalFlush(hand)
		print "straight flush: ", hasStraightFlush(hand)
		print "four of a kind: ", hasFourOfAKind(hand)
		print "full house: ", hasFullHouse(hand)
		print "flush: ", hasFlush(hand)
		print "straight: ", hasStraight(hand)
		print "three of a kind: ", hasThreeOfAKind(hand)
		print "two pairs: ", hasTwoPairs(hand)
		print "one pair: ", hasOnePair(hand)
		print generate_score(hand)
	
	#testhands = ["5H 5C 6S 7S KD","2C 3S 8S 8D TD","2D 9C AS AH AC","5D 8C 9S JS AC","2C 5C 7D 8S QH","3D 6D 7D TD QD","4D 6S 9H QH QC","3D 6D 7H QD QS","2H 2D 4C 4D 4S","3C 3D 3S 9S 9D"]
	t = "7D 8S 6D TS KD 7H AC 5S 7C 5D".split(" ")
	testhands = [t[0:5],t[5:]]
	for i in testhands: testFn(i)
	import urllib2
	hands = urllib2.urlopen("https://projecteuler.net/project/resources/p054_poker.txt").readlines()
	hands = [i.strip("\n").split(" ") for i in hands]
	fails=[]
	for i in hands:
		temp=win(i[0:5],i[5:])
		if temp==None: fails.append(i)
	hands = [win(i[0:5],i[5:]) for i in hands]
	print hands.count(1)
def euler55():
	def test_lychrel(n):
		count=1
		n+=int(str(n)[::-1])
		flag=False
		while count<50:
			if n==int(str(n)[::-1]):
				flag=True
			n+=int(str(n)[::-1])
			count+=1
		return flag
	count=0
	for i in range(10000):
		if test_lychrel(i)==False:
			count+=1
	print count
def euler56():
	print max([sum([int(k) for k in str(i**j)]) for i in range(100) for j in range(100)])
def euler57():
	def matrix_mult(m1,m2):
		a,b,c,d,e,f,g,h=m1[0],m1[1],m1[2],m1[3],m2[0],m2[1],m2[2],m2[3]
		return [a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h]
	def m_exp(m,n):
		temp=m
		for i in range(n-1):
			temp=matrix_mult(temp,m)
		return temp
	def convergent(n):
		temp=m_exp([2,1,1,0],n)
		return (temp[3]+temp[2],temp[2])
	count=0
	for i in range(2,1003):
		if len(str(convergent(i)[0]))>len(str(convergent(i)[1])): count+=1
	print count
def euler58():
	def corner_numbers(n):
		if i==1: return [1]
		else: return sorted([4*i*i-4*i+1,4*i*i-10*i+7,4*i*i-8*i+5,4*i*i-6*i+3])
	primes=[]
	total=[1]
	i=2
	flag=True
	while flag:
		for j in corner_numbers(i):
			if isPrime(j): primes.append(j)
			total.append(j)
		i+=1
		if (len(primes)*1./len(total))<=0.1: flag=False
	print 2*((total-1)/4)+1
def euler59():
	values=[79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68,4,7,5,23,27,1,21,79,85,78,79,85,71,38,10,71,27,12,2,79,6,2,8,13,9,1,13,9,8,68,19,7,1,71,56,11,21,11,68,6,3,22,2,14,0,30,79,1,31,6,23,19,10,0,73,79,44,2,79,19,6,28,68,16,6,16,15,79,35,8,11,72,71,14,10,3,79,12,2,79,19,6,28,68,32,0,0,73,79,86,71,39,1,71,24,5,20,79,13,9,79,16,15,10,68,5,10,3,14,1,10,14,1,3,71,24,13,19,7,68,32,0,0,73,79,87,71,39,1,71,12,22,2,14,16,2,11,68,2,25,1,21,22,16,15,6,10,0,79,16,15,10,22,2,79,13,20,65,68,41,0,16,15,6,10,0,79,1,31,6,23,19,28,68,19,7,5,19,79,12,2,79,0,14,11,10,64,27,68,10,14,15,2,65,68,83,79,40,14,9,1,71,6,16,20,10,8,1,79,19,6,28,68,14,1,68,15,6,9,75,79,5,9,11,68,19,7,13,20,79,8,14,9,1,71,8,13,17,10,23,71,3,13,0,7,16,71,27,11,71,10,18,2,29,29,8,1,1,73,79,81,71,59,12,2,79,8,14,8,12,19,79,23,15,6,10,2,28,68,19,7,22,8,26,3,15,79,16,15,10,68,3,14,22,12,1,1,20,28,72,71,14,10,3,79,16,15,10,68,3,14,22,12,1,1,20,28,68,4,14,10,71,1,1,17,10,22,71,10,28,19,6,10,0,26,13,20,7,68,14,27,74,71,89,68,32,0,0,71,28,1,9,27,68,45,0,12,9,79,16,15,10,68,37,14,20,19,6,23,19,79,83,71,27,11,71,27,1,11,3,68,2,25,1,21,22,11,9,10,68,6,13,11,18,27,68,19,7,1,71,3,13,0,7,16,71,28,11,71,27,12,6,27,68,2,25,1,21,22,11,9,10,68,10,6,3,15,27,68,5,10,8,14,10,18,2,79,6,2,12,5,18,28,1,71,0,2,71,7,13,20,79,16,2,28,16,14,2,11,9,22,74,71,87,68,45,0,12,9,79,12,14,2,23,2,3,2,71,24,5,20,79,10,8,27,68,19,7,1,71,3,13,0,7,16,92,79,12,2,79,19,6,28,68,8,1,8,30,79,5,71,24,13,19,1,1,20,28,68,19,0,68,19,7,1,71,3,13,0,7,16,73,79,93,71,59,12,2,79,11,9,10,68,16,7,11,71,6,23,71,27,12,2,79,16,21,26,1,71,3,13,0,7,16,75,79,19,15,0,68,0,6,18,2,28,68,11,6,3,15,27,68,19,0,68,2,25,1,21,22,11,9,10,72,71,24,5,20,79,3,8,6,10,0,79,16,8,79,7,8,2,1,71,6,10,19,0,68,19,7,1,71,24,11,21,3,0,73,79,85,87,79,38,18,27,68,6,3,16,15,0,17,0,7,68,19,7,1,71,24,11,21,3,0,71,24,5,20,79,9,6,11,1,71,27,12,21,0,17,0,7,68,15,6,9,75,79,16,15,10,68,16,0,22,11,11,68,3,6,0,9,72,16,71,29,1,4,0,3,9,6,30,2,79,12,14,2,68,16,7,1,9,79,12,2,79,7,6,2,1,73,79,85,86,79,33,17,10,10,71,6,10,71,7,13,20,79,11,16,1,68,11,14,10,3,79,5,9,11,68,6,2,11,9,8,68,15,6,23,71,0,19,9,79,20,2,0,20,11,10,72,71,7,1,71,24,5,20,79,10,8,27,68,6,12,7,2,31,16,2,11,74,71,94,86,71,45,17,19,79,16,8,79,5,11,3,68,16,7,11,71,13,1,11,6,1,17,10,0,71,7,13,10,79,5,9,11,68,6,12,7,2,31,16,2,11,68,15,6,9,75,79,12,2,79,3,6,25,1,71,27,12,2,79,22,14,8,12,19,79,16,8,79,6,2,12,11,10,10,68,4,7,13,11,11,22,2,1,68,8,9,68,32,0,0,73,79,85,84,79,48,15,10,29,71,14,22,2,79,22,2,13,11,21,1,69,71,59,12,14,28,68,14,28,68,9,0,16,71,14,68,23,7,29,20,6,7,6,3,68,5,6,22,19,7,68,21,10,23,18,3,16,14,1,3,71,9,22,8,2,68,15,26,9,6,1,68,23,14,23,20,6,11,9,79,11,21,79,20,11,14,10,75,79,16,15,6,23,71,29,1,5,6,22,19,7,68,4,0,9,2,28,68,1,29,11,10,79,35,8,11,74,86,91,68,52,0,68,19,7,1,71,56,11,21,11,68,5,10,7,6,2,1,71,7,17,10,14,10,71,14,10,3,79,8,14,25,1,3,79,12,2,29,1,71,0,10,71,10,5,21,27,12,71,14,9,8,1,3,71,26,23,73,79,44,2,79,19,6,28,68,1,26,8,11,79,11,1,79,17,9,9,5,14,3,13,9,8,68,11,0,18,2,79,5,9,11,68,1,14,13,19,7,2,18,3,10,2,28,23,73,79,37,9,11,68,16,10,68,15,14,18,2,79,23,2,10,10,71,7,13,20,79,3,11,0,22,30,67,68,19,7,1,71,8,8,8,29,29,71,0,2,71,27,12,2,79,11,9,3,29,71,60,11,9,79,11,1,79,16,15,10,68,33,14,16,15,10,22,73]
	v1=[]
	v2=[]
	v3=[]
	for i in range(len(values)):
		if i%3==0: v1.append(values[i])
		if i%3==1: v2.append(values[i])
		if i%3==2: v3.append(values[i])
	from collections import Counter
	# print Counter(v1), Counter(v2), Counter(v3)
	# most common characters are 71,79,68
	# since most common character is probably space (ascii value 32), we thus have key values
	# 103, 111, 100
	decrypt=[]
	for i in range(len(values)):
		if i%3==0: decrypt.append(int(values[i]^103))
		if i%3==1: decrypt.append(int(values[i]^111))
		if i%3==2: decrypt.append(int(values[i]^100))
	#print "".join([chr(i) for i in decrypt])
	print sum(decrypt)
def euler60():
	limit=10000
	primes=primeGenerate(limit)
	def primeConcat(p1,p2):
		if p1==5: return False
		if (p1+p2)%3==0: return False
		
		else: return miller_rabin(int(str(p1)+str(p2))) and miller_rabin(int(str(p2)+str(p1)))
	potentials=[]
	for p1 in primes:
		for p2 in [i for i in primes if i>p1]:
			if p2 in [997, 1997, 2999, 4001, 4999, 6007, 7001, 7993, 8999, 9973]: print p1,p2
			if primeConcat(p1,p2):
				for p3 in [i for i in primes if i>p2]:
					if primeConcat(p1,p3) and primeConcat(p2,p3):
						for p4 in [i for i in primes if i>p3]:
							if primeConcat(p1,p4) and primeConcat(p2,p4) and primeConcat(p3,p4):
								for p5 in [i for i in primes if i>p4]:
									if primeConcat(p1,p5) and primeConcat(p2,p5) and primeConcat(p3,p5) and primeConcat(p4,p5):
										potentials.append([p1,p2,p3,p4,p5])
	print "\n"*10
	print potentials
def euler61():
	def triangle(n): return (n*(n+1))/2
	def square(n): return n*n
	def pentagon(n): return (n*(3*n-1))/2
	def hexagon(n): return n*(2*n-1)
	def heptagon(n): return (n*(5*n-3))/2
	def octagon(n): return n*(3*n-2)
	def isTriangle(n):
		return ((8*n+1)**0.5)%1==0
	def isSquare(n):
		return n**.5%1==0
	def isPentagon(n):
		return ((24*n+1)**.5)%6==5
	def isHexagon(n):
		return ((8*n+1)**.5)%4==3
	def isHeptagon(n):
		return ((40*n+9)**.5)%10==7
	def isOctagon(n):
		return ((3*n+1)**.5)%3==2
	figures=[]
	for i in [[3,j] for j in range(1000,10000) if isTriangle(j)]: figures.append(i)
	for i in [[4,j] for j in range(1000,10000) if isSquare(j)]: figures.append(i)
	for i in [[5,j] for j in range(1000,10000) if isPentagon(j)]: figures.append(i)
	for i in [[6,j] for j in range(1000,10000) if isHexagon(j)]: figures.append(i)
	for i in [[7,j] for j in range(1000,10000) if isHeptagon(j)]: figures.append(i)
	for i in [[8,j] for j in range(1000,10000) if isOctagon(j)]: figures.append(i)
	p=[]
	for i1 in [i for i in figures]:
		for i2 in [i for i in figures if i1[1]%100==i[1]//100 and i[0] not in [i1[0]]]:
			for i3 in [i for i in figures if i2[1]%100==i[1]//100 and i[0] not in [i1[0],i2[0]]]:
				for i4 in [i for i in figures if i3[1]%100==i[1]//100 and i[0] not in [i1[0],i2[0],i3[0]]]:
					for i5 in [i for i in figures if i4[1]%100==i[1]//100 and i[0] not in [i1[0],i2[0],i3[0],i4[0]]]:
						for i6 in [i for i in figures if i5[1]%100==i[1]//100 and i[0] not in [i1[0],i2[0],i3[0],i4[0],i5[0]]]:
							p.append([j[1] for j in [i1,i2,i3,i4,i5,i6]])
	q=[]
	for i in p:
		if (sorted(i) not in q): q.append(i)
	for i in q:
		if i[-1]%100==i[0]//100: print sum(i); break
def euler62():
	import itertools
	i=1
	cubes=[]
	flag=True
	while flag:
		cubes.append(sorted(str(i**3)))
		if cubes.count(sorted(str(i**3)))==5:
			for j in range(len(cubes)):
				if cubes[j]==sorted(str(i**3)): print (j+1)**3;flag=False;break
		i+=1
def euler63():
	def f(k):
		return [len(str(i**k)) for i in range(1,10)].count(k)
	total=0
	i=1
	while True:
		temp=f(i)
		if temp==0: break
		total+=temp
		i+=1
	print total
	
def euler64():
	def continued_fraction(S):
		if (S**0.5)%1==0: return 0
		else:
			m=0
			d=1
			a=int(S**0.5)
			period=0
			while a!=2*int(S**0.5):
				m=d*a-m
				d=(S-m*m)/d
				a=int((S**0.5+m)/d)
				period+=1
			return period
	total=0
	for i in range(2,10000):
		if continued_fraction(i)%2==1: total+=1
	print total
def euler65():
	out=[0]*102
	out[0]=1
	out[1]=1
	out[2]=2
	for n in range(3,102):
		if n%3==0 or n%3==2: out[n]=out[n-1]+out[n-2]
		else: out[n]=2*(n-1)*out[n-1]/3+out[n-2]
	print sum([int(i) for i in str(out[101])])
def euler66():
	def continued_fraction(S):
		m=0
		d=1
		a=int(S**0.5)
		out=[a]
		while a!=2*int(S**0.5):
			m=d*a-m
			d=(S-m*m)/d
			a=int((S**0.5+m)/d*1.)
			out.append(a)
		temp=out[1:]
		while len(out)<S+1:
			out+=temp
		temp2=[]
		for i in range(S+1):
			temp2.append(out[i])
		return temp2
	def convergents(n):
		continued_frac=continued_fraction(n)
		out=[[0,1],[1,0]]+[0]*(n+1)
		for i in range(len(continued_frac)):
			out[i+2]=[continued_frac[i]*out[i+1][0]+out[i][0],continued_frac[i]*out[i+1][1]+out[i][1]]
		return out
	def pellSolve(D): # returns lowest solution to x^2-D*y^2=1
		if not((int(D**0.5))**2==D):
			for i in convergents(D)[2:]:
				if i[0]**2-D*i[1]**2==1:
					return i
	max=0
	out=0
	for i in range(1000):
		if pellSolve(i)!=None and pellSolve(i)[0]>max:
			max=pellSolve(i)[0]
			out=i
	return out
def euler67():
	def triangle(lis):
		out=[]
		i=0
		while ((i+1)*(i+2))/2<=len(lis):
			out.append(lis[int(i*(i+1)*0.5):int((i+1)*(i+2)*0.5)])
			i+=1
		return out
	def newRow(currentRow, prevRow):
		out = []
		for i in range(len(prevRow)):
			out.append(max(prevRow[i]+currentRow[i],prevRow[i]+currentRow[i+1]))
		return out
	import urllib2
	temp = [i.split(" ") for i in urllib2.urlopen("https://projecteuler.net/project/resources/p067_triangle.txt").read().split("\n")]
	temp2=[]
	for i in temp:
		for j in i:
			temp2.append(j)
	temp3=[]
	for i in temp2:
		if i!="":
			temp3.append(i)
	triangleNum = triangle([int(i) for i in temp3])
	while len(triangleNum)>1:
		tempRow = newRow(triangleNum[-1],triangleNum[-2])
		triangleNum.remove(triangleNum[-1])
		triangleNum[-1]=tempRow
	print triangleNum[0][0]
def euler68():
	"""
	5 inner vertices, 5 outer vertices
	the "branch" of magic 5-gon ring has inner vertex will be labelled with a then going clockwise, labeling rest of inner vertices with b,c,d,e
	
	then outer vertices will be labeled as follows:
	f connected with a
	g "" b
	h "" c
	i "" d
	j "" e
	
	it then follows that these conditions must be fullfilled:
	min(f,g,h,i,j)=f
	f+a+b=g+b+c=h+c+d=i+d+e=j+e+a
	
	tostring: fabgbchcdidejea
	
	"""
	import itertools
	possible=[]
	for p in itertools.permutations([1,2,3,4,5,6,7,8,9,10]):
		a,b,c,d,e,f,g,h,i,j=p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]
		if min(f,g,h,i,j)==f and f+a+b==g+b+c==h+c+d==i+d+e==j+e+a: possible.append(str(f)+str(a)+str(b)+str(g)+str(b)+str(c)+str(h)+str(c)+str(d)+str(i)+str(d)+str(e)+str(j)+str(e)+str(a))
	print max([int(i) for i in possible if len(i)==16])
def euler69():
	from fractions import gcd
	def phi(n):
		return [gcd(i,n) for i in range(n)].count(1)
	p=primeGenerate(100000)
	out=1
	for i in p:
		out*=i
		if out>1000000: out/=i; break
	print out
def euler71():
	# Farey sequences to the rescue :D
	# this post helped https://math.stackexchange.com/questions/39582/how-to-compute-next-previous-representable-rational-number
	"""
	p=3
	q=7
	n=1e6
	r=1/p mod q
	3*r=1 mod 7 => r=5
	b = q*x+r < n
	7x+5<1e6
	x=142856 => b = 7x+5 = 999997
	a = (bp-1)/q =
	"""
	print (999997*3-1)/7
def euler72():
	# length of Farey sequence
	import sympy
	import time
	start=time.time()
	def phi(n):
		return sympy.ntheory.factor_.totient(n)
	total=1
	for i in range(1,1000001):
		if i%1000==0: print i
		total+=phi(i)
	print total-2
	print "time",time.time()-start
def euler73():
	# Farey sequences again
	# first fraction is 1/3, next needs to satisfy p*3-q=1 and q<=12000
	# 1/3, 4000/11999
	fraction=[(1,3),(4000,11999)]
	i=0
	flag=True
	while flag:
		f1=fraction[-2]
		f2=fraction[-1]
		a,b,c,d=f1[0],f1[1],f2[0],f2[1]
		temp = ((int((12000.+b)/d)*c-a,int((12000.+b)/d)*d-b))
		fraction.append((int((12000.+b)/d)*c-a,int((12000.+b)/d)*d-b))
		i+=1
		if (0.5-float(temp[0])/temp[1])==0: flag=False
		if i%20000==0: print i, 0.5-float(temp[0])/temp[1]
	print len(fraction)-2
def euler74():
	def f(n):
		return [1,1,2,6,24,120,720,5040,40320,362880][n]
	def next(n):
		return sum([f(int(i)) for i in str(n)])
	def chain_length(n):
		out=[n]
		while True:
			temp=next(out[-1])
			if temp in out: break
			else: out.append(temp)
		return out
	count=0
	for i in range(1000000):
		if len(chain_length(i))==60: count+=1
		if i%1000==0: print i, count
	print count
def euler75():
	from fractions import gcd
	from collections import Counter
	primitivetriples=[]
	for n in range(1,1500):
		for m in range(n,1500):
			if gcd(m,n)==1 and (m+n)%2==1:
				primitivetriples.append((m*m-n*n,2*m*n,m*m+n*n))
	triples=[]
	for triple in primitivetriples:
		a0=triple[0]
		b0=triple[1]
		c0=triple[2]
		i=1
		while i*(a0+b0+c0)<=1500000:
			triples.append([a0*i,b0*i,c0*i])
			i+=1
	triples=[sorted(i) for i in triples if sum(i)<=1500000]
	print "triples generated"
	tripleSums=[sum(i) for i in triples]
	print "sums generated"
	tripleSums=Counter(tripleSums)
	print "counted"
	print tripleSums.values().count(1)
def euler76():
	import sympy
	x=sympy.symbols("x")
	poly=1
	for i in range(1,101):
		poly*=1/(1-x**i)
	print (sympy.series(poly,x,0,101)).coeff(x**100)-1
def euler77():
	import sympy
	x=sympy.symbols("x")
	poly=1
	for i in range(100):
		if isPrime(i): poly*=1/(1-x**i)
	print "multiplied terms"
	temp=sympy.series(poly,x,0,100)
	print "series calculated"
	def nth_coeff(n):
		return temp.coeff(x**n)
	n=1
	while nth_coeff(n)<5000:
		print n,nth_coeff(n)
		n+=1
	print n
def euler78():
	def memoize(f):
		memo = {}
		def helper(x):
			if x not in memo:
				memo[x] = f(x)
			return memo[x]
		return helper
	def partition(n): # based off OEIS code
		if n == 0: return 1
		S = 0; J = n-1; k = 2
		while 0 <= J:
			T = partition(J)
			S = S+T if (k//2)%2==1 else S-T
			J -= k if k%2==1 else k//2
			k += 1
		return S
	partition = memoize(partition)
	i=1
	while True:
		if partition(5*i+4)%1000000==0: # due to Ramanujan
			print 5*i+4; break
		i+=1
def euler80():
	import decimal
	decimal.getcontext().prec = 110
	d=decimal.Decimal
	def digitalrootsum(i):
		return int(i**0.5)+sum([int(i) for i in str(d(i)**d(0.5)).split(".")[1][0:99]])
	print sum([digitalrootsum(i) for i in range(1,101)])
def euler81():
	import urllib2
	f=urllib2.urlopen("https://projecteuler.net/project/resources/p081_matrix.txt")
	matrix = [[int(j) for j in i.strip("\n").split(",")] for i in f.readlines()]
	for i in reversed(range(len(matrix)-1)):
		matrix[79][i]+=matrix[79][i+1]
		matrix[i][79]+=matrix[i+1][79]
	for i in reversed(range(len(matrix)-1)):
		for j in reversed(range(len(matrix)-1)):
			matrix[i][j]+=min(matrix[i][j+1],matrix[i+1][j])
	print matrix[0][0]
def euler82():
	import urllib2
	f=urllib2.urlopen("https://projecteuler.net/project/resources/p082_matrix.txt")
	grid = [[int(j) for j in i.strip("\n").split(",")] for i in f.readlines()]
	currentColumn=[0]*80
	for i in range(80):
		currentColumn[i]=grid[i][79]
	for i in reversed(range(79)):
		currentColumn[0]+=grid[0][i]
		for j in range(80):
			currentColumn[j]=min(currentColumn[j-1]+grid[j][i],currentColumn[j]+grid[j][i])
		for j in reversed(range(79)):
			currentColumn[j]=min(currentColumn[j],currentColumn[j+1]+grid[j][i])
	print min(currentColumn)
def euler83():
	INFINITY=2<<100
	def dijstkra(grid, source=(0,0)):
		length=len(grid)
		Q=[(i,j,False) for i in range(legnth) for j in range(length)]
		dist=[0 for i in range(length**2)]
		prev=["?" for i in range(length**2)]
		dist[0]=0 #distance to soruce is 0
		while [i[2] for i in Q].count(False)!=0:
			
"""
def failedeuler61():
        def isTriangle(n):
                return ((8*n+1)**0.5)%1==0
        def isSquare(n):
                return n**.5%1==0
        def isPentagon(n):
                return ((24*n+1)**.5)%6==5
        def isHexagon(n):
                return ((8*n+1)**.5)%4==3
        def isHeptagon(n):
                return ((40*n+9)**.5)%10==7
        def isOctagon(n):
                return ((3*n+1)**.5)%3==2
        for a in [i for i in range(1000,10000) if isTriangle(i)]:
                print a
                for b in [i for i in range(100*a%100,(100*a%100)+100) if isSquare(i) and 1000<i<10000]:
                        for c in [i for i in range(100*b%100,(100*b%100)+100) if isPentagon(i) and 1000<i<10000]:
                                for d in [i for i in range(100*c%100,(100*c%100)+100) if isHexagon(i) and 1000<i<10000]:
                                        for e in [i for i in range(100*d%100,(100*d%100)+100) if isHeptagon(i) and 1000<i<10000]:
                                                for f in [i for i in range(100*e%100,(100*e%100)+100) if isOctagon(i) and 1000<i<10000]:
                                                        print a,b,c,d,e,f
"""

