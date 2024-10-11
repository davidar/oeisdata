from sympy import primefactors
def a(n): return sum(p**3 for p in primefactors(n))
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jul 11 2017