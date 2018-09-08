def euler549():
    from math import factorial
    def s(n):
        i=1
        while factorial(i)%n!=0:
            i+=1
        return i
    for i in range(2,101):
        print i, s(i)
print euler549()