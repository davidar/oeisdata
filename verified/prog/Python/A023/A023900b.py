from math import prod
from sympy import primefactors
def A023900(n): return prod(1-p for p in primefactors(n)) # _Chai Wah Wu_, Sep 08 2023
print([A023900(n) for n in range(1,31)])
