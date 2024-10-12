from math import prod
from sympy import primefactors
def A003557(n): return n//prod(primefactors(n)) # _Chai Wah Wu_, Nov 04 2022
print([A003557(n) for n in range(1,31)])
