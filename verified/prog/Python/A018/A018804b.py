from sympy import factorint
from math import prod
def A018804(n): return prod(p**(e-1)*((p-1)*e+p) for p, e in factorint(n).items()) # _Chai Wah Wu_, Nov 29 2021
print([A018804(n) for n in range(1,31)])
