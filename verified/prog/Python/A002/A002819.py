from functools import reduce
from operator import ixor
from sympy import factorint
def A002819(n): return sum(-1 if reduce(ixor, factorint(i).values(),0)&1 else 1 for i in range(1,n+1)) # _Chai Wah Wu_, Dec 19 2022
print([A002819(n) for n in range(30)])
