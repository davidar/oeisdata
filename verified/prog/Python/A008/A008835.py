from math import prod
from sympy import factorint
def A008835(n): return prod(p**(e&-4) for p, e in factorint(n).items()) # _Chai Wah Wu_, Aug 08 2024
print([A008835(n) for n in range(1,31)])
