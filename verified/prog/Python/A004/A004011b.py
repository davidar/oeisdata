from math import prod
from sympy import factorint
def A004011(n): return 24*prod((p**(e+1)-1)//(p-1) for p, e in factorint(n).items() if p > 2) if n else 1 # _Chai Wah Wu_, Nov 13 2022
print([A004011(n) for n in range(30)])
