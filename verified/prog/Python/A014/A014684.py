from sympy import isprime
def A014684(n): return n-int(isprime(n)) # _Chai Wah Wu_, Oct 14 2023
print([A014684(n) for n in range(1,31)])
