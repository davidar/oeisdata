from math import isqrt
def A003842(n): return n+2-((m:=(n+2+isqrt(5*(n+2)**2)>>1)-n-2)+isqrt(5*m**2)>>1) # _Chai Wah Wu_, Aug 26 2022
print([A003842(n) for n in range(30)])
