from math import prod
from sympy import factorint
def A000224(n): return prod((p**(e+1)//((p+1)*(q:=1+(p==2)))>>1)+q for p, e in factorint(n).items()) # _Chai Wah Wu_, Oct 07 2024
print([A000224(n) for n in range(1,31)])
