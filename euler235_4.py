temp = "1.0"
while len(temp)<16:
    temp+=str([i for i in range(10) if sum([(900-3*k)*float(temp+str(i))**(k-1) for k in range(5001)])+(600000000000.)>0][-1])
  