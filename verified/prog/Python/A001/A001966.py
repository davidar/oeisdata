from math import isqrt
def A001966(n): return ((m:=(n<<1)+1)+isqrt(5*m**2)>>1)+m # _Chai Wah Wu_, Aug 25 2022
print([A001966(n) for n in range(30)])
