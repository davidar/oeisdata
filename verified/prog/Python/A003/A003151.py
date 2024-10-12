from math import isqrt
def A003151(n): return n+isqrt(n*n<<1) # _Chai Wah Wu_, Aug 03 2022
print([A003151(n) for n in range(1,31)])
