def euler148():
    def factorial_gen(n):
        factorials = [1]
        for i in range(1,n+1):
            factorials.append(i*factorials[-1])
        return factorials
    def pascal(n):
        factorial = factorial_gen(n)
        out = []
        for i in range(n+1):
            out.append(factorial[n]/factorial[i]/factorial[n-i])
        return out
    for i in range(1000): 
        if [_%7 for _ in pascal(i)].count(0)==0: print i
print euler148()
