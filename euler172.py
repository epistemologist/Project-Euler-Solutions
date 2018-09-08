def euler172():
    from itertools import combinations, permutations, product
    def count_ways(arr):
        from math import factorial
        a = lambda n: factorial(sum(n))/(reduce(lambda x,y:x*y,[factorial(i) for i in n]))
        return factorial(sum(arr))/(reduce(lambda x,y:x*y,[factorial(i) for i in arr])) if arr[0]==0 else factorial(sum(arr))/(reduce(lambda x,y:x*y,[factorial(i) for i in arr]))-factorial(sum([arr[i] if i!=0 else arr[i]-1 for i in range(10)]))/(reduce(lambda x,y:x*y,[factorial(i) for i in [arr[i] if i!=0 else arr[i]-1 for i in range(10)]]))
    out = 0
    index = 0
    for i in product([0,1,2,3],repeat=10):
        if sum(i)==18:
            out+=count_ways(i)
        if index%100000==0: print index,i
        index+=1
    return out



print e172()