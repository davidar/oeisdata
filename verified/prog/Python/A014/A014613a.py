from sympy import factorint
def ok(n): return sum(factorint(n).values()) == 4
print([k for k in range(377) if ok(k)]) # _Michael S. Branicky_, Nov 19 2021