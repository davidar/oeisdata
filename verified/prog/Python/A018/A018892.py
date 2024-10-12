from math import prod
from sympy import factorint
def A018892(n): return prod((a<<1)+1 for a in factorint(n).values())+1>>1 # _Chai Wah Wu_, Aug 20 2023
print([A018892(n) for n in range(1,31)])
