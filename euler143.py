def euler143():
    # using law of cosines:
    # a^2 = q^2 + r^2 + qr
    # b^2 = p^2 + r^2 + pr
    # c^2 = p^2 + q^2 + pq
    # parametrized solution of x^2+xy+y^2=z^2
    # x = t^2-1, y = 2t-t^2, z = t^2-t+1
    out = []
    for t in range(-60000,60001):
        out.append((t*t-1,2*t-t*t,t*t-t+1))
    return [i[0]>0 and i[1]>0 and i[2]>0 for i in out].count(True)
print euler143()