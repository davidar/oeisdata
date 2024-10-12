from math import isqrt
def A003622(n): return (n+isqrt(5*n**2)>>1)+n-1 # _Chai Wah Wu_, Aug 11 2022
print([A003622(n) for n in range(1,31)])
