from sympy import fibonacci as F
def a(n): return F(n)*F(n + 1)
[a(n) for n in range(101)] # _Indranil Ghosh_, Aug 03 2017
print([a(n) for n in range(30)])
