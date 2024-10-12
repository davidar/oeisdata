from math import isqrt
def A022839(n): return isqrt(5*n**2) # _Chai Wah Wu_, Sep 07 2022
print([A022839(n) for n in range(1,31)])
