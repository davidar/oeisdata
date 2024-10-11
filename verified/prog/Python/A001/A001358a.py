from sympy import factorint
def ok(n): return sum(factorint(n).values()) == 2
print([k for k in range(1, 190) if ok(k)]) # _Michael S. Branicky_, Apr 30 2022