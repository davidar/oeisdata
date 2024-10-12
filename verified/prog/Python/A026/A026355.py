from math import isqrt
def A026355(n): return (n-1+isqrt(5*(n-1)**2)>>1)+2 if n else 1 # _Chai Wah Wu_, Aug 25 2022
print([A026355(n) for n in range(30)])
