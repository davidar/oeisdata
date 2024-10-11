from sympy import factorint
def a(n): return 1 if n == 1 else min(factorint(n))
print([a(n) for n in range(1, 98)]) # _Michael S. Branicky_, Dec 09 2021