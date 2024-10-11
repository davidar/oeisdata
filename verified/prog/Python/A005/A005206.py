from math import isqrt
def A005206(n): return (n+1+isqrt(5*(n+1)**2)>>1)-n-1 # _Chai Wah Wu_, Aug 09 2022
print([A005206(n) for n in range(30)])
