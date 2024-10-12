from math import isqrt
def A026352(n): return (n+isqrt(5*n**2)>>1)+n+1 # _Chai Wah Wu_, Aug 25 2022
print([A026352(n) for n in range(30)])
