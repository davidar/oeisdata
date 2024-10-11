from math import isqrt
def A017968(n): return (m:=isqrt(k:=21**n))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 29 2022
print([A017968(n) for n in range(30)])
