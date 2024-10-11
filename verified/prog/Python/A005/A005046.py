from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def a(n): return 1 if n==0 else sum(binomial(2*n - 1, 2*k - 1)*a(n - k) for k in range(1, n + 1))
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Sep 11 2017, after Maple program by _Alois P. Heinz_