def euler618():
    def fib(n):
        if n<=2: return 1
        else: return fib(n-1)+fib(n-2)
    for i in range(2,25):
        print i,fib(i)
    def is_prime(n):
        if n<2: return False
        if n==2: return True
        for i in range(2,int(n**0.5)+2):
            if n%i==0: return False
        return True
    primes = [i for i in range(fib(24)) if is_prime(i)]
    F = [fib(i) for i in range(2,25)]
    from itertools import combinations
    def solve(arr,n):
        subsets = (
            subset for length in range(1, len(arr))
            for subset in combinations(arr, length)
        )
        solution = next((subset for subset in subsets if sum(subset) == n), None)
        return list(solution)
    print solve([1,2,3,4,5],4)
print euler618()