from sympy.ntheory import discrete_log
def a(n): return discrete_log(19, n, 2)
print([a(n) for n in range(1, 19)]) # _Michael S. Branicky_, Aug 13 2021