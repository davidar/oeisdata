from math import isqrt
def A002821(n): return (m:=isqrt(k:=n**3))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 30 2022
print([A002821(n) for n in range(30)])
