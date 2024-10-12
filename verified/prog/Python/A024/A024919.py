from math import isqrt
def A024919(n): return (-(s:=isqrt(m:=n>>1))**2*(s+1) + sum((q:=m//k)*((k<<1)+q+1) for k in range(1,s+1))<<1)+((s:=isqrt(n))**2*(s+1)-sum((q:=n//k)*((k<<1)+q+1) for k in range(1,s+1))>>1) # _Chai Wah Wu_, Oct 22 2023
print([A024919(n) for n in range(1,31)])
