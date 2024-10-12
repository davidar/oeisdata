from math import isqrt
def A022413(n): return (n+isqrt(5*n**2)>>1)+n+3 if n else 1 # _Chai Wah Wu_, Aug 29 2022
print([A022413(n) for n in range(30)])
