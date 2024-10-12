from math import isqrt
def A007401(n): return n-1+(isqrt(n<<3)+1>>1) # _Chai Wah Wu_, Oct 18 2022
print([A007401(n) for n in range(1,31)])
