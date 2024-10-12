from math import prod
from sympy import factorint, nextprime
def A003973(n): return prod(((q:=nextprime(p))**(e+1)-1)//(q-1) for p,e in factorint(n).items()) # _Chai Wah Wu_, Jul 05 2022
print([A003973(n) for n in range(1,31)])
