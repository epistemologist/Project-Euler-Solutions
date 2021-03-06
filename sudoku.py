def solve(boardIn):
    ROWS = [[i for i in range(81) if i//9==j] for j in range(9)]
    COLS = [[i for i in range(81) if i%9==j] for j in range(9)]
    BOXS = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
    global iterations
    iterations=0

    def getLegalPositions(digit,board):
        positionsOfDigit = [i for i in range(81) if board[i]==digit]
        illegalPositions = []
        for j in positionsOfDigit:
            for i in ROWS:
                if j in i: illegalPositions+=i
            for i in COLS:
                if j in i: illegalPositions+=i
            for i in BOXS:
                if j in i: illegalPositions+=i
        return [i for i in range(81) if i not in illegalPositions]
    def getLegalDigits(pos,board):
        indiciesToCheck = []
        for i in ROWS:
            if pos in i: indiciesToCheck+=i
        for i in COLS:
            if pos in i: indiciesToCheck+=i
        for i in BOXS:
            if pos in i: indiciesToCheck+=i
        illegalDigits = [board[i] for i in indiciesToCheck]
        return [i for i in "123456789" if i not in illegalDigits]
    def boardFill(board):
        for i in range(81):
            if len(getLegalDigits(i,board))==1:
                board[i]=getLegalDigits(i,board)[0]
        for i in range(1,10):
            i=str(i)
            if len(getLegalPositions(i,board))==1:
                board[getLegalPositions(i,board)[0]] = i
        return board
    def check(board):
        rows = [[board[j] for j in i] for i in ROWS]
        cols = [[board[j] for j in i] for i in COLS]
        boxs = [[board[j] for j in i] for i in BOXS]
        groups = rows+cols+boxs
        for i in groups:
            for j in range(1,10):
                if i.count(str(j))>1: return False
        return True
    boardOut = boardFill(boardIn)
    def backtrack(position,board,iterations=0):
        if position==80:
            iterations+=1
            return True
        boardFill(boardIn)
        for x in range(1,10):
            board[position] = str(x)
            if check(board)==True:
                if backtrack(position+1,board,iterations=iterations+1)==True:
                    iterations+=1
                    return True
        board[position] = "0"
        return False
    backtrack(0,boardIn)
    possiblePositions = [(i,getLegalDigits(i,boardIn)) for i in range(81) if boardIn[i]=="0"]
    #if boardIn.count("0")>0: print reduce(lambda x,y:x*y,[len(i[1]) for i in possiblePositions])
    return boardIn
import urllib2
def finish(boardIn):
    ROWS = [[i for i in range(81) if i//9==j] for j in range(9)]
    COLS = [[i for i in range(81) if i%9==j] for j in range(9)]
    BOXS = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
    def subFill(groupType,index,boardIn):
        if groupType=="row":
            currentGroup = [boardIn[i] for i in ROWS[index]]
            if currentGroup.count("0")==1:
                missingDigit = [i for i in "123456789" if i not in currentGroup][0]
                for i in range(len(currentGroup)):
                    if currentGroup[i]=="0": currentGroup[i]=missingDigit
            for i in range(len(currentGroup)):
                boardIn[ROWS[index][i]]=currentGroup[i]
        if groupType=="col":
            currentGroup = [boardIn[i] for i in COLS[index]]
            if currentGroup.count("0")==1:
                missingDigit = [i for i in "123456789" if i not in currentGroup][0]
                for i in range(len(currentGroup)):
                    if currentGroup[i]=="0": currentGroup[i]=missingDigit
            for i in range(len(currentGroup)):
                boardIn[COLS[index][i]]=currentGroup[i]
        if groupType=="box":
            currentGroup = [boardIn[i] for i in BOXS[index]]
            if currentGroup.count("0")==1:
                missingDigit = [i for i in "123456789" if i not in currentGroup][0]
                for i in range(len(currentGroup)):
                    if currentGroup[i]=="0": currentGroup[i]=missingDigit
            for i in range(len(currentGroup)):
                boardIn[BOXS[index][i]]=currentGroup[i]
        return boardIn
    for i in range(9):
        boardIn=subFill("row",i,boardIn)
    for i in range(9):
        boardIn=subFill("col",i,boardIn)
    for i in range(9):
        boardIn=subFill("box",i,boardIn)
    return boardIn
puzzles = [i.strip("\n") for i in urllib2.urlopen("https://projecteuler.net/project/resources/p096_sudoku.txt").readlines()]
def f(lis):
    def factorial(n):
        if n<=1: return 1
        else: return n*factorial(n-1)
    out = factorial(sum(lis))
    for i in lis:
        out/=factorial(i)
    return out
def prettyPrint(board):
    for i in range(0,81,9):
        print "".join(board[i:i+9])
    print "\n"
def check(board):
    ROWS = [[i for i in range(81) if i//9==j] for j in range(9)]
    COLS = [[i for i in range(81) if i%9==j] for j in range(9)]
    BOXS = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
    rows = [[board[j] for j in i] for i in ROWS]
    cols = [[board[j] for j in i] for i in COLS]
    boxs = [[board[j] for j in i] for i in BOXS]
    groups = rows+cols+boxs
    for i in groups:
        for j in range(1,10):
            if i.count(str(j))>1: return False
    return True
out = []
out2 = []
count=0
b=[]
for i in range(0,500,10):
    temp = puzzles[i:i+10]
    temp.pop(0)
    temp = list("".join(temp))
    temp = solve(temp)
    prettyPrint(temp)
    a = ""

    while a.split(" ")[0]!="Yes":
        a=str(input("Continue?: "))
        b.append(a.split(" ")[1])
#    if temp.count("0")>0: prettyPrint(temp)
print b
