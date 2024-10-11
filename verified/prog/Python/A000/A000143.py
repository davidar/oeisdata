from math import prod
from sympy import factorint
def A000143(n): return prod((p**(3*(e+1))-(1 if p&1 else 15))//(p**3-1) for p, e in factorint(n).items())<<4 if n else 1 # _Chai Wah Wu_, Jun 21 2024
print([A000143(n) for n in range(30)])
