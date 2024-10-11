from sympy.polys.specialpolys import cyclotomic_poly
def a(n): return 8 if n == 0 else cyclotomic_poly(n, x=8)
print([a(n) for n in range(27)]) # _Michael S. Branicky_, Aug 07 2021