from math import isqrt
def A001030(n): return [2, 1, 1, 2, 1, 2, 1, 2][n-1] if n < 9 else -isqrt(m:=(n-9)*(n-9)<<1)+isqrt(m+(n-9<<2)+2) # _Chai Wah Wu_, Aug 25 2022
print([A001030(n) for n in range(1,31)])
