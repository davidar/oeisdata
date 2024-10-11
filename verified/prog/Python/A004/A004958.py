from math import isqrt
def A004958(n): return (isqrt(20*n**2)>>1)+(n<<1)+1 if n else 0 # _Chai Wah Wu_, Aug 17 2022
print([A004958(n) for n in range(30)])
