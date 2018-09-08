def euler624():
    def mat_mul(m1,m2,m):
        a,b,c,d,e,f,g,h = m1[0],m1[1],m1[2],m1[3],m2[0],m2[1],m2[2],m2[3]
        return [(a*e+b*g)%m,(a*f+b*h)%m,(c*e+d*g)%m,(c*f+d*h)%m]
    def mat_pow(mat,n,m):
        result = [1,0,0,1]
        while n > 0:
            if n%2 == 1:
                result = mat_mul(result,mat,m)
            n /= 2
            mat = mat_mul(mat,mat,m)
        return result
    def mat_inv(mat,n):
        a,b,c,d = mat[0],mat[1],mat[2],mat[3]
        return [i*pow(a*d-b*c,10**9+7,10**9+9) for i in [d,-b,-c,a]]
    F = mat_pow([1,1,1,0],10**18,10**9+9)
    I = [pow(2,10**18,10**9+9),0,0,pow(2,10**18,10**9+9)]
    return mat_mul(F,mat_inv([I[i]-F[i] for i in range(4)],10**9+9),10**9+9)
print euler624()