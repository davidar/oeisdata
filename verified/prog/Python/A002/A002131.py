from math import prod
from sympy import factorint
def A002131(n): return prod(p**e if p == 2 else (p**(e+1)-1)//(p-1) for p, e in factorint(n).items()) # _Chai Wah Wu_, Dec 17 2021
print([A002131(n) for n in range(1,31)])
