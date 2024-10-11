from math import isqrt
def A003849(n): return 2-(n+2+isqrt(m:=5*(n+2)**2)>>1)+(n+1+isqrt(m-10*n-15)>>1) # _Chai Wah Wu_, Aug 25 2022
print([A003849(n) for n in range(30)])
