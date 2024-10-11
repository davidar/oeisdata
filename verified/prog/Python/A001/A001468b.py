from math import isqrt
def A001468(n): return (n+1+isqrt(m:=5*(n+1)**2)>>1)-(n+isqrt(m-10*n-5)>>1) # _Chai Wah Wu_, Aug 25 2022
print([A001468(n) for n in range(30)])
