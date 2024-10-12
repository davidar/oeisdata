from math import prod
from sympy import factorint
def A006579(n): return prod(p**(e-1)*((p-1)*e+p) for p, e in factorint(n).items()) - n # _Chai Wah Wu_, May 15 2022
print([A006579(n) for n in range(1,31)])
