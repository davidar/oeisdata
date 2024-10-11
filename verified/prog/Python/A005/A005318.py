from sympy import sqrt, floor
def a(n): return n if n<2 else 2*a(n - 1) - a(n - floor(sqrt(2)*sqrt(n - 1) + 1/2) - 1) # _Indranil Ghosh_, Jun 03 2017
print([a(n) for n in range(30)])
