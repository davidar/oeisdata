from math import isqrt
def A027924(n): return isqrt((n*(n+1))**2<<1)+1>>1 # _Chai Wah Wu_, Jun 19 2024
print([A027924(n) for n in range(1,31)])
