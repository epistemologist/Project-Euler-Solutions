

f[n_]: = Module[{l, b, d}, l= Divisors [n]
                b = l[[-2]]
                n-1 + (6*n+2)*(n-b) + 2*Sum[Floor[n/d], {d, b, n-1}]]
a[n_]: = a[n] = If[n == 1, f[2], a[n-1] + Sum[f[i], {i, Prime[n-1]+1, Prime[n]}]]
Table[a[n], {n, 1, 32}]
