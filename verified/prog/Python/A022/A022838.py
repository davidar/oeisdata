from math import isqrt
def A022838(n): return isqrt(3*n*n) # _Chai Wah Wu_, Aug 06 2022
print([A022838(n) for n in range(1,31)])
