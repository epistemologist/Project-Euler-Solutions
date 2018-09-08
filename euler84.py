from random import choice as r
def euler84(games=1000):
    global board
    def dice_roll():
        return r([(i,j) for i in range(1,5) for j in range(1,5)])
    board = ["GO","A1","CC1","A2","T1","R1","B1","CH1","B2","B3","JAIL","C1","U1","C2","C3","R2","D1","CC2","D2","D3","FP","E1","CH2","E2","E3","R3","F1","F2","U2","F3","G2J","G1","G2","CC3","G3","R4","CH3","H1","T2","H2"]
    def game(TURNS=50000):
        position = 0
        out = [0]*40
        rolls = []
        for _ in range(TURNS):
            currentroll = dice_roll()
            rolls.append(currentroll)
            if board[position] in ["CC1","CC2","CC3"]:
                community_card = r(range(16))
                if community_card == 0:
                    position = 0 # advance to go
                elif community_card == 1:
                    position = 10 # go to jail
            elif board[position] in ["CH1","CH2","CH3"]:
                chance_card = r(range(16))
                if chance_card == 0:
                    position = 0 # advance to go
                elif chance_card == 1:
                    position = 10 # go to jail
                elif chance_card == 2:
                    position= 11 # go to C1
                elif chance_card == 3:
                    position = 24 # go to E3
                elif chance_card == 4:
                    position = 39  # go to H2
                elif chance_card == 5:
                    position = 5 # go to R1
                elif chance_card == 6 or chance_card == 7:
                    while board[position] not in ["R1","R2","R3","R4"]:
                        position = (position + 1)%40
                elif chance_card == 8: 
                    while board[position] not in ["U1","U2"]:
                        position = (position + 1)%40
                elif chance_card == 9:
                    position = (position - 3) % 40
            elif len(rolls)>3 and all([i[0]==i[1] for i in rolls[-3:]]):
                position = 10
            elif board[position] == "G2J":
                position = 10
            else:
                position = (position + sum(currentroll))%40
            #print position
            out[position]+=1
        return out
    out = [0]*40
    for i in range(games):
        print i
        temp = game()
        for i in range(40):
            out[i]+=temp[i]
    for i in range(40):
        print i, 1.*out[i]/sum(out), out[i], board[i]
euler84(500000)
