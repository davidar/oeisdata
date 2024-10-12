from sympy import lucas
def a(n): return 4 * lucas(n + 1) - 1
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Jul 27 2017