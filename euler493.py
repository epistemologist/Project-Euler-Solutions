def euler493():
    from random import shuffle
    balls = []
    for i in range(10):
        for j in "roygbiv":
            balls.append(j)
    shuffle(balls)
    return len(set(balls[0:20]))
out = 0
out2 = 0
for i in range(10000):
    out+=euler493()
    out2+=1
print out,out2
