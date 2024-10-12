from sympy import primerange
def A013939(n): return sum(n//p for p in primerange(n+1)) # _Chai Wah Wu_, Oct 06 2024
print([A013939(n) for n in range(1,31)])
