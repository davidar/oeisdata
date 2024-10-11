from math import prod
from sympy import factorint
def A000161(n):
    f = factorint(n)
    return int(not any(e&1 for e in f.values())) + (((m:=prod(1 if p==2 else (e+1 if p&3==1 else (e+1)&1) for p, e in f.items()))+((((~n & n-1).bit_length()&1)<<1)-1 if m&1 else 0))>>1) if n else 1 # _Chai Wah Wu_, Sep 08 2022
print([A000161(n) for n in range(30)])
