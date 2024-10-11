from sympy.ntheory.factor_ import core
def ok(n): return core(n, 2) == n
print(list(filter(ok, range(1, 114)))) # _Michael S. Branicky_, Jul 31 2021