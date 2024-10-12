from math import isqrt
def A001950(n): return (n+isqrt(5*n**2)>>1)+n # _Chai Wah Wu_, Aug 10 2022
print([A001950(n) for n in range(1,31)])
