from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def a(n): return 1 if n==0 else 2**binomial(n, 2) - sum(a(k)*binomial(n, k) for k in range(n))
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Aug 12 2017