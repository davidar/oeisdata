from math import isqrt
def A022846(n): return isqrt(n**2<<3)+1>>1 # _Chai Wah Wu_, Feb 10 2023
print([A022846(n) for n in range(30)])
