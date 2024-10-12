from math import prod
from sympy import primepi, factorint
def A003963(n): return prod(primepi(p)**e for p, e in factorint(n).items()) # _Chai Wah Wu_, Nov 17 2022
print([A003963(n) for n in range(1,31)])
