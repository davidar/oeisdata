from math import isqrt
def A014675(n): return (n+2+isqrt(m:=5*(n+2)**2)>>1)-(n+1+isqrt(m-10*n-15)>>1) # _Chai Wah Wu_, Aug 10 2022
print([A014675(n) for n in range(30)])
