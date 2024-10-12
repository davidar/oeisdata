from math import prod
from sympy import factorint
def A025426(n): return ((m:=prod(1 if p==2 else (e+1 if p&3==1 else (e+1)&1) for p, e in factorint(n).items()))+((((~n & n-1).bit_length()&1)<<1)-1 if m&1 else 0))>>1 # _Chai Wah Wu_, Jul 07 2022
print([A025426(n) for n in range(30)])
