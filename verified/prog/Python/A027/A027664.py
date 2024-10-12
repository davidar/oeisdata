from math import isqrt
def A027664(n): return (m:=isqrt(k:=n*10**14))+int(k-m*(m+1)>=1) # _Chai Wah Wu_, Jul 31 2022
print([A027664(n) for n in range(1,31)])
