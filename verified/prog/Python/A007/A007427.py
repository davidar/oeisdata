from math import prod, comb
from sympy import factorint
def A007427(n): return prod(-comb(2,e) if e&1 else comb(2,e) for e in factorint(n).values()) # _Chai Wah Wu_, Jul 05 2024
print([A007427(n) for n in range(1,31)])
