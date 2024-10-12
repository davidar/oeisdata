from math import isqrt
def A003623(n): return (n+isqrt(5*n**2)&-2)+n # _Chai Wah Wu_, Aug 25 2022
print([A003623(n) for n in range(1,31)])
