from math import isqrt
from sympy import divisor_count
def A007956(n): return isqrt(n)**(d-2) if (d:=divisor_count(n))&1 else n**((d>>1)-1) # _Chai Wah Wu_, Jun 18 2023
print([A007956(n) for n in range(1,31)])
