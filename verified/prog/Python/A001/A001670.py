from math import isqrt
def A001670(n): return (m:=isqrt(n))+int((n-m*(m+1)<<2)>=1)<<1 # _Chai Wah Wu_, Jul 29 2022
print([A001670(n) for n in range(1,31)])
