from sympy.ntheory import discrete_log
def a(n): return discrete_log(13, n, 2)
print([a(n) for n in range(1, 13)]) # _Michael S. Branicky_, Aug 22 2021