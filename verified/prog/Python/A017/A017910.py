from math import isqrt
def A017910(n): return isqrt(1<<n) if n&1 else 1<<(n>>1) # _Chai Wah Wu_, Jul 26 2022
print([A017910(n) for n in range(30)])
