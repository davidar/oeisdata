from math import isqrt
def A027663(n): return (m:=isqrt(k:=n*10**10))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 30 2022
print([A027663(n) for n in range(1,31)])
