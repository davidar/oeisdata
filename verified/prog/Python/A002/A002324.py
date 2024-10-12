from math import prod
from sympy import factorint
def A002324(n): return prod(e+1 if p%3==1 else int(not e&1) for p, e in factorint(n).items() if p != 3) # _Chai Wah Wu_, Nov 17 2022
print([A002324(n) for n in range(1,31)])
