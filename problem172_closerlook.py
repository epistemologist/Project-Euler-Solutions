def euler172():
    from itertools import combinations, permutations
    def count_ways(arr):
        from math import factorial
        digits = [arr.count(i) for i in range(10)]
        digits2 = [_ for _ in digits]
        digits2[0] -= 1
        expr1 = factorial(sum(digits))/reduce(lambda x,y: x*y, [factorial(i) for i in digits])
        try:
            expr2 = factorial(sum(digits2))/reduce(lambda x,y: x*y, [factorial(i) for i in digits2])
            return expr1-expr2
        except:
            return expr1
    out = 0
    out2 = 0
    index = 0
    for i in combinations([j for j in "00112233445566778899"],7):
        out+=count_ways(i)
        print index
        index+=1
        for j in permutations(i): 
            if len(str(int("".join(j))))==len(j):
                out2+=1
    return out,out2

print euler172()

def euler172_oneliner():
    from itertools import combinations
    from math import factorial
    def count_ways(arr):
        from math import factorial
        digits = [arr.count(i) for i in range(10)]
        digits2 = [arr.count(i) if i!=0 else arr.count(i)-1 for i in range(10)]
        expr1 = factorial(sum(digits))/reduce(lambda x,y: x*y, [factorial(i) for i in digits])
        if arr[0]==0: expr2 = factorial(sum(digits2))/reduce(lambda x,y: x*y, [factorial(i) for i in digits2])
        return expr1 if arr[0]==0 else expr1-expr2