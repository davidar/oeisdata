from math import isqrt
def A000201(n): return (n+isqrt(5*n**2))//2 # _Chai Wah Wu_, Jan 11 2022
print([A000201(n) for n in range(1,31)])
