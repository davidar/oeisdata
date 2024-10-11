from math import isqrt
def A000093(n): return isqrt(n**3) # _Chai Wah Wu_, Sep 08 2024
print([A000093(n) for n in range(30)])
