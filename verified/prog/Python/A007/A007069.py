from math import isqrt
def A007069(n): return isqrt(isqrt(n**2<<1)**2<<1) # _Chai Wah Wu_, Aug 29 2022
print([A007069(n) for n in range(1,31)])
