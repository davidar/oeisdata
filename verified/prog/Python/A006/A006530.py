from sympy import factorint
def a(n): return 1 if n == 1 else max(factorint(n))
print([a(n) for n in range(1, 87)]) # _Michael S. Branicky_, Aug 08 2022