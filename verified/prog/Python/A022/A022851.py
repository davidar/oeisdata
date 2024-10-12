from math import isqrt
def A022851(n): return (m:=isqrt(k:=n**2<<3))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 29 2022
print([A022851(n) for n in range(30)])
