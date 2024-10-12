from math import isqrt
def A002541(n): return (sum(n//k for k in range(1,isqrt(n)+1))<<1)-isqrt(n)**2-n # _Chai Wah Wu_, Oct 20 2023
print([A002541(n) for n in range(1,31)])
