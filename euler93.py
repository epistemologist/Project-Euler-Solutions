def euler93():
    import itertools
    global BRACKETS
    BRACKETS = ["a!b@c#d","(a!b)@c#d","a!(b@c)#d","a!b@(c#d)","((a!b)@c)#d","(a!(b@c))#d","a!((b@c)#d)","a!(b@(c#d))","(a!b)@(c#d)"]
    def generate(array):
        out = []
        for l in itertools.permutations(array):
            for k in BRACKETS:
                for j in itertools.product("+-*/",repeat=3):
                    i=k.replace("!",j[0])
                    i=i.replace("@",j[1])
                    i=i.replace("#",j[2])
                    i=i.replace("a",str(l[0])+".")
                    i=i.replace("b",str(l[1])+".")
                    i=i.replace("c",str(l[2])+".")
                    i=i.replace("d",str(l[3])+".")
                    out.append(i)
        temp = []
        for i in out:
            try:
                temp.append(eval(i))
            except ZeroDivisionError:
                temp.append(-1)
        return sorted(set([int(i) for i in temp if i>0 and i%1.0==0.0]))
    def count_consecutive_numbers(array):
        first_differences = [array[i+1]-array[i] for i in range(len(array)-1)]
        count = 1
        for i in range(len(first_differences)):
            if first_differences[i]==1:
                count+=1
            else:
                break
        return count
    max_numbers = 0
    max_digits = 0
    for i in itertools.combinations(range(10),4):
        temp = count_consecutive_numbers(generate(i))
        if temp>max_numbers:
            max_numbers = temp
            max_digits = i
    return max_digits, max_numbers
print euler93()

