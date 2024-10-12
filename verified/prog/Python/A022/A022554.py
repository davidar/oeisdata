from math import isqrt
def A022554(n): return (m:=isqrt(n))*(m*(-(m<<1)-3)+6*n+5)//6 # _Chai Wah Wu_, Aug 03 2022
print([A022554(n) for n in range(30)])
