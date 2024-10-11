from sympy import primefactors
def a(n): return sum(1 for p in primefactors(n) if p%3==2)
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jul 11 2017