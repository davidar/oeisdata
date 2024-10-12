from math import prod
from sympy import factorint
def A008457(n): return prod((p**(3*(e+1))-(1 if p&1 else 15))//(p**3-1) for p, e in factorint(n).items()) # _Chai Wah Wu_, Jun 21 2024
print([A008457(n) for n in range(1,31)])
