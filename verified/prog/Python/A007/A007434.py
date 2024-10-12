from math import prod
from sympy import factorint
def A007434(n): return prod(p**(e-1<<1)*(p**2-1) for p, e in factorint(n).items()) # _Chai Wah Wu_, Jan 29 2024
print([A007434(n) for n in range(1,31)])
