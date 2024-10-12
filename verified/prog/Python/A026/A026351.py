from math import isqrt
def A026351(n): return (n+isqrt(5*n**2)>>1)+1 # _Chai Wah Wu_, Aug 17 2022
print([A026351(n) for n in range(30)])
