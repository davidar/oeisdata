from math import isqrt
def A000194(n): return (m:=isqrt(n))+int(n-m*(m+1)>=1) # _Chai Wah Wu_, Jul 30 2022
print([A000194(n) for n in range(30)])
