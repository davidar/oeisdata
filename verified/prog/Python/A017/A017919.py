from math import isqrt
def A017919(n): return isqrt(5**n) # _Chai Wah Wu_, Jun 19 2024
print([A017919(n) for n in range(30)])
