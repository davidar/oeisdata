from sympy import factorint, npartitions
from math import prod
def A000688(n): return prod(map(npartitions,factorint(n).values())) # _Chai Wah Wu_, Jan 14 2022
print([A000688(n) for n in range(1,31)])
