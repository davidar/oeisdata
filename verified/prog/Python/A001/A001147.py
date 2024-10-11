from sympy import factorial2
def a(n): return factorial2(2 * n - 1)
print([a(n) for n in range(101)])  # _Indranil Ghosh_, Jul 22 2017