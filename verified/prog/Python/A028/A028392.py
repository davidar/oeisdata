from math import isqrt
def A028392(n): return n+isqrt(n) # _Chai Wah Wu_, May 16 2023
print([A028392(n) for n in range(30)])
