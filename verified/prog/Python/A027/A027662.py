from math import isqrt
def A027662(n): return (m:=isqrt(k:=n*10**6))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 30 2022
print([A027662(n) for n in range(1,31)])
