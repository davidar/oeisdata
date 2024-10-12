from math import isqrt
def A007066(n): return (n+1+isqrt(5*(n-1)**2)>>1)+n if n > 1 else 1 # _Chai Wah Wu_, Aug 25 2022
print([A007066(n) for n in range(1,31)])
