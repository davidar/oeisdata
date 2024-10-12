from math import isqrt
def A019446(n): return (n+isqrt(5*n**2)>>1)-n+1 # _Chai Wah Wu_, Aug 09 2022
print([A019446(n) for n in range(1,31)])
