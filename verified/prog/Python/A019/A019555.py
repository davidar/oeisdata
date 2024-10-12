from math import prod
from sympy import factorint
def A019555(n): return prod(p**((q%3 != 0)+(q//3)) for p, q in factorint(n).items()) # _Chai Wah Wu_, Aug 18 2021
print([A019555(n) for n in range(1,31)])
