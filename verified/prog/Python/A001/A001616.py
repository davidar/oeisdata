from math import prod
from sympy import factorint
def A001616(n): return prod(p**(e>>1)+p**(e-1>>1) for p, e in factorint(n).items()) # _Chai Wah Wu_, Jul 05 2024
print([A001616(n) for n in range(1,31)])
