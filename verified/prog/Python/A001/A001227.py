from functools import reduce
from operator import mul
from sympy import factorint
def A001227(n): return reduce(mul,(q+1 for p, q in factorint(n).items() if p > 2),1) # _Chai Wah Wu_, Mar 08 2021
print([A001227(n) for n in range(1,31)])
