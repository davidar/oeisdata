from math import isqrt
def A001182(n): return sum(isqrt(k*((n<<1)-k)) for k in range(1,n)) # _Chai Wah Wu_, Jul 18 2024
print([A001182(n) for n in range(1,31)])
