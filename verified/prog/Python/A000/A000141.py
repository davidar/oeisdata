from math import prod
from sympy import factorint
def A000141(n):
    if n == 0: return 1
    f = [(p,e,(0,1,0,-1)[p&3]) for p,e in factorint(n).items()]
    return (prod((p**(e+1<<1)-c)//(p**2-c) for p, e, c in f)<<2)-prod(((k:=p**2*c)**(e+1)-1)//(k-1) for p, e, c in f)<<2 # _Chai Wah Wu_, Jun 21 2024
print([A000141(n) for n in range(30)])
