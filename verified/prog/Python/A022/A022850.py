from math import isqrt
def A022850(n): return (m:=isqrt(k:=7*n*n))+int(k-m*(m+1)>=1) # _Chai Wah Wu_, Jul 31 2022
print([A022850(n) for n in range(30)])
