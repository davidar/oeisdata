from math import isqrt
from sympy import mobius
def A013928(n): return sum(mobius(k)*((n-1)//k**2) for k in range(1,isqrt(n-1)+1)) # _Chai Wah Wu_, Jan 03 2024
print([A013928(n) for n in range(1,31)])
