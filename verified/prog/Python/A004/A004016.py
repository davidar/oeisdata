from math import prod
from sympy import factorint
def A004016(n): return 6*prod(e+1 if p%3==1 else int(not e&1) for p, e in factorint(n).items() if p != 3) if n else 1 # _Chai Wah Wu_, Nov 17 2022
print([A004016(n) for n in range(30)])
