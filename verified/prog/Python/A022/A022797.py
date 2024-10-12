from sympy import prime, composite
def A022797(n): return 3 if n == 1 else prime(n)+composite(n-1) # _Chai Wah Wu_, Aug 30 2021
print([A022797(n) for n in range(1,31)])
