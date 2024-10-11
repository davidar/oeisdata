from sympy import factorint
def ok(n): f = factorint(n); return sum(f[p] for p in f) == 3
print(list(filter(ok, range(245)))) # _Michael S. Branicky_, Aug 12 2021