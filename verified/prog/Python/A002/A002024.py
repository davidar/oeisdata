from math import isqrt
def A002024(n): return (isqrt(8*n)+1)//2 # _Chai Wah Wu_, Feb 02 2022
print([A002024(n) for n in range(1,31)])
