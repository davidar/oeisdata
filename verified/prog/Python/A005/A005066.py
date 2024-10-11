from sympy import primefactors
def a(n): return sum(p**2 for p in primefactors(n) if p % 2)
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jul 11 2017