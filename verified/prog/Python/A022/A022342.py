from math import isqrt
def A022342(n): return (n+isqrt(5*n**2)>>1)-1 # _Chai Wah Wu_, Aug 17 2022
print([A022342(n) for n in range(1,31)])
