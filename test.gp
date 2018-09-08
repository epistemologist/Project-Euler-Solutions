a(n) = {my(f = factor(n)); for (i=1, #f~, if (f[i, 2] % f[i, 1], f[i, 2]--); ); factorback(f); }
print a(100)