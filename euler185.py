def euler185():
    import z3
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16 = z3.Ints(
        "x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16")
    #x1,x2,x3,x4,x5 = z3.Ints("x1 x2 x3 x4 x5")
    variables = [x1, x2, x3, x4, x5, x6, x7, x8,
                 x9, x10, x11, x12, x13, x14, x15, x16]
    #variables = [x1,x2,x3,x4,x5]

    def none_correct(arr):
        return reduce(z3.And, [arr[i] != variables[i] for i in range(len(arr))])

    def one_correct(arr):
        return reduce(z3.Or, [
            reduce(z3.And, [
                arr[j] != variables[j] if i != j else arr[j] == variables[j] for j in range(len(arr))
            ]) for i in range(len(arr))
        ])

    def two_correct(arr):
        out = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i < j:
                    out.append(reduce(z3.And, [arr[k] == variables[k] if (
                        k == i or k == j) else arr[k] != variables[k] for k in range(len(arr))]))
        return reduce(z3.Or, out)

    def three_correct(arr):
        out = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i < j < k:
                        out.append(reduce(z3.And, [arr[l] == variables[l] if (
                            l == i or l == j or l == k) else arr[l] != variables[l] for l in range(len(arr))]))
        return reduce(z3.Or, out)
    s = []
    for i in variables:
        s.append(0 <= i)
        s.append(i <= 9)
    # s.append(z3.simplify(two_correct([int(i) for i in "90342"])))
    # s.append(z3.simplify(none_correct([int(i) for i in "70794"])))
    # s.append(z3.simplify(two_correct([int(i) for i in "39458"])))
    # s.append(z3.simplify(one_correct([int(i) for i in "34109"])))
    # s.append(z3.simplify(two_correct([int(i) for i in "51545"])))
    # s.append(z3.simplify(one_correct([int(i) for i in "12531"])))
    # print z3.solve(reduce(z3.And,s))
    """
    5616185650518293 ;2 correct
    3847439647293047 ;1 correct
    5855462940810587 ;3 correct
    9742855507068353 ;3 correct
    4296849643607543 ;3 correct
    3174248439465858 ;1 correct
    4513559094146117 ;2 correct
    7890971548908067 ;3 correct
    8157356344118483 ;1 correct
    2615250744386899 ;2 correct
    8690095851526254 ;3 correct
    6375711915077050 ;1 correct
    6913859173121360 ;1 correct
    6442889055042768 ;2 correct
    2321386104303845 ;0 correct
    2326509471271448 ;2 correct
    5251583379644322 ;2 correct
    1748270476758276 ;3 correct
    4895722652190306 ;1 correct
    3041631117224635 ;3 correct
    1841236454324589 ;3 correct
    2659862637316867 ;2 correct
    """

    guesses = "5616185650518293  3847439647293047  5855462940810587  9742855507068353  4296849643607543  3174248439465858  4513559094146117  7890971548908067  8157356344118483  2615250744386899  8690095851526254  6375711915077050  6913859173121360  6442889055042768  2321386104303845  2326509471271448  5251583379644322  1748270476758276  4895722652190306  3041631117224635  1841236454324589  2659862637316867".split(
        "  ")
    guesses = zip(guesses, [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2])
    for (i,j) in guesses:
        print i
        if j==0:
            s.append(z3.simplify(none_correct([int(k) for k in i])))
        elif j==1:
            s.append(z3.simplify(one_correct([int(k) for k in i])))
        elif j==2:
            s.append(z3.simplify(two_correct([int(k) for k in i])))
        else:
            s.append(z3.simplify(three_correct([int(k) for k in i])))
    return sorted(z3.solve(reduce(z3.And,s)))
print euler185()
