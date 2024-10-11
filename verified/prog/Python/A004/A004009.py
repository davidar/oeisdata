from sympy import divisor_sigma
def a(n): return 1 if n == 0 else 240 * divisor_sigma(n, 3)
[a(n) for n in range(51)]  # _Indranil Ghosh_, Jul 15 2017
print([a(n) for n in range(30)])
