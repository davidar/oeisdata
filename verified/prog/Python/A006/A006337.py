from math import isqrt
def A006337(n): return -isqrt(m:=n*n<<1)+isqrt(m+(n<<2)+2) # _Chai Wah Wu_, Aug 03 2022
print([A006337(n) for n in range(1,31)])
