from math import isqrt
def A017921(n): return isqrt(5**n)+(n&1) # _Chai Wah Wu_, Jun 19 2024
print([A017921(n) for n in range(30)])
