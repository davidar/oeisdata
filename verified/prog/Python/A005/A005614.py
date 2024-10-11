from math import isqrt
def A005614(n): return (n+isqrt(m:=5*(n+2)**2)>>1)-(n+1+isqrt(m-10*n-15)>>1) # _Chai Wah Wu_, Aug 17 2022
print([A005614(n) for n in range(30)])
