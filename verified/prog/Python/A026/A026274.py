from math import isqrt
def A026274(n): return (n+1+isqrt(5*(n+1)**2)>>1)+n-1 # _Chai Wah Wu_, Aug 17 2022
print([A026274(n) for n in range(1,31)])
