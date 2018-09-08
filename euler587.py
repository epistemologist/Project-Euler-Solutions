def euler587():
    from math import*; return [m for m in range(1,10000) if (0.5*((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))**2/m+0.5*((((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))-1)*sqrt(2*((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))-((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))**2)-2*((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))+asin(((-sqrt(2)*m**1.5+m**2+m)/(m**2+1))-1)+2))/(1-pi/4)<0.001][0]
print euler587()
