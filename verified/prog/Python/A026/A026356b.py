from math import isqrt
def A026356(n): return (n+1+isqrt(5*(n-1)**2)>>1)+n # _Chai Wah Wu_, Aug 11 2022
print([A026356(n) for n in range(1,31)])
