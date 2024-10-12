from math import isqrt
from sympy import divisor_count
def A007955(n):
    d = divisor_count(n)
    return isqrt(n)**d if d % 2 else n**(d//2) # _Chai Wah Wu_, Jan 05 2022
print([A007955(n) for n in range(1,31)])
