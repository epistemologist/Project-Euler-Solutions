def euler572():
    import sympy
    import numpy as np
    a,b,c,d,e,f,g,h,i = sympy.symbols("a b c d e f g h i")
    M = np.array([[a,b,c],[d,e,f],[g,h,i]])
    return np.dot(M,M)
print euler572()
