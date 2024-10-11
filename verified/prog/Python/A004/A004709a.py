from sympy.ntheory.factor_ import core
def ok(n): return core(n, 3) == n
print(list(filter(ok, range(1, 86)))) # _Michael S. Branicky_, Aug 16 2021