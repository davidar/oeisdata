from math import prod
from sympy import factorint
def A008834(n): return prod(p**(e-e%3) for p, e in factorint(n).items()) # _Chai Wah Wu_, Aug 08 2024
print([A008834(n) for n in range(1,31)])
