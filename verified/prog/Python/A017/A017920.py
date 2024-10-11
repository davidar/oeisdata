from math import isqrt
def A017920(n): return (m:=isqrt(k:=5**n))+(k-m*(m+1)>=1) # _Chai Wah Wu_, Jun 19 2024
print([A017920(n) for n in range(30)])
