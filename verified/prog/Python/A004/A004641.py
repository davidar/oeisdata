from math import isqrt
def A004641(n): return [1, 0, 0, 1, 0, 1, 0, 1][n-1] if n < 9 else -1-isqrt(m:=(n-9)*(n-9)<<1)+isqrt(m+(n-9<<2)+2) # _Chai Wah Wu_, Aug 25 2022
print([A004641(n) for n in range(1,31)])
