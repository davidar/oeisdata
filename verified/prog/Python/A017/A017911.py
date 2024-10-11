from math import isqrt
def A017911(n): return -isqrt(m:=1<<n)+isqrt(m<<2) # _Chai Wah Wu_, Jun 18 2024
print([A017911(n) for n in range(30)])
