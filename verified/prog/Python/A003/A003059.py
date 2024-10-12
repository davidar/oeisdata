from math import isqrt
def A003059(n): return isqrt(n-1)+1 # _Chai Wah Wu_, Nov 14 2022
print([A003059(n) for n in range(1,31)])
