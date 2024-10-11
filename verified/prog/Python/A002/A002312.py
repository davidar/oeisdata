from sympy import factorint
def ok(n): return max(factorint(n*n + 1)) < 2*n
print(list(filter(ok, range(1, 201)))) # _Michael S. Branicky_, Aug 30 2021