from math import prod
from sympy import factorint
def A007429(n): return prod((p*(p**(e+1)-1)-(p-1)*(e+1))//(p-1)**2 for p,e in factorint(n).items()) # _Chai Wah Wu_, Mar 28 2024
print([A007429(n) for n in range(1,31)])
