from math import isqrt
def A007067(n): return (isqrt(5*n**2<<2)>>1)+n+1>>1 # _Chai Wah Wu_, Aug 26 2022
print([A007067(n) for n in range(30)])
