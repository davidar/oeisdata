from math import isqrt
def A004976(n): return (isqrt(20*n**2)>>1)+(n<<1) # _Chai Wah Wu_, Aug 17 2022
print([A004976(n) for n in range(30)])
