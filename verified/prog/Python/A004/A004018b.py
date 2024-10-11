from math import prod
from sympy import factorint
def A004018(n): return prod(1 if p==2 else (e+1 if p&3==1 else (e+1)&1) for p, e in factorint(n).items())<<2 if n else 1 # _Chai Wah Wu_, Jul 07 2022, corrected Jun 21 2024.
print([A004018(n) for n in range(30)])
