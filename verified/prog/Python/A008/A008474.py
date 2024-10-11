from sympy import factorint
def a(n): return 0 if n == 1 else sum(p+k for p, k in factorint(n).items())
print([a(n) for n in range(1, 79)]) # _Michael S. Branicky_, Mar 28 2022