from math import prod
from collections import Counter
from sympy import factorint
def A027423(n): return prod(e+1 for e in sum((Counter(factorint(i)) for i in range(2,n+1)),start=Counter()).values()) # _Chai Wah Wu_, Jun 25 2022
print([A027423(n) for n in range(30)])
