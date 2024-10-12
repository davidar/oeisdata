from math import prod, gcd
from sympy import factorint
def A009205(n):
    f = factorint(n).items()
    return gcd(prod(e+1 for p, e in f),prod((p**(e+1)-1)//(p-1) for p,e in f)) # _Chai Wah Wu_, Jul 27 2023
print([A009205(n) for n in range(1,31)])
