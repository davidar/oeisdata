from sympy import factorint
def ok(n): f=factorint(n); return len(f) == 2 and sum(f[p] for p in f) == 2
print(list(filter(ok, range(1, 206)))) # _Michael S. Branicky_, Jun 10 2021