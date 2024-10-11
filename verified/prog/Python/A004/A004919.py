from math import isqrt
def A004919(n): return (3*n+isqrt(45*n**2)>>1)+(n<<1) # _Chai Wah Wu_, Aug 17 2022
print([A004919(n) for n in range(30)])
