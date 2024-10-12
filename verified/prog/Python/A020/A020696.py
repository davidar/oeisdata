from math import prod
from sympy import divisors
def A020696(n): return prod(d+1 for d in divisors(n,generator=True)) # _Chai Wah Wu_, Jun 30 2022
print([A020696(n) for n in range(1,31)])
