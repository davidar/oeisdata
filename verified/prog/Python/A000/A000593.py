from math import prod
from sympy import factorint
def A000593(n): return prod((p**(e+1)-1)//(p-1) for p, e in factorint(n).items() if p > 2) # _Chai Wah Wu_, Sep 09 2021
print([A000593(n) for n in range(1,31)])
