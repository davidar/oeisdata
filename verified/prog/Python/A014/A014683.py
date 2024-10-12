from sympy import isprime
def A014683(n): return n+isprime(n) # _Chai Wah Wu_, Oct 03 2024
print([A014683(n) for n in range(1,31)])
