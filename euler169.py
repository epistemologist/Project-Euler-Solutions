def euler169():
    # Generating function: product of (1+x^2^k+x^(2*2^k)) for k = 0 to infinity
    # OEIS A2487
    """
    a(0)=0
    a(1)=1
    a(2n)=a(n)
    a(2n+1)=a(n)+a(n+1)

    a(10^25) = a(5^25)
    """
    def A002487(n):
        # based on Sage program by Peter Luschny
        M = [1,0]
        bits = [int(i) for i in bin(n)[2:]]
        for b in bits:
            M[b] = M[0]+M[1]
        return M[1]
    return A002487(10**25+1)
print euler169()