from sympy import fibonacci
from sympy.core.cache import cacheit
@cacheit
def a(n): return 1 if n==0 else 0 if n==1 else a(n - 1) + a(n - 2) + fibonacci(n - 3)
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Jul 20 2017