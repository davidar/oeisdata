from math import isqrt
def A000037(n): return n+isqrt(n+isqrt(n)) # _Chai Wah Wu_, Mar 31 2022
print([A000037(n) for n in range(1,31)])
