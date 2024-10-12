from math import prod
from sympy import factorint
def A019554(n): return n//prod(p**(q//2) for p, q in factorint(n).items()) # _Chai Wah Wu_, Aug 18 2021
print([A019554(n) for n in range(1,31)])
