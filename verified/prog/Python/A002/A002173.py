from math import prod
from sympy import factorint
def A002173(n): return prod(((m:=p**2*(0,1,0,-1)[p&3])**(e+1)-1)//(m-1) for p, e in factorint(n).items()) # _Chai Wah Wu_, Jun 21 2024
print([A002173(n) for n in range(1,31)])
