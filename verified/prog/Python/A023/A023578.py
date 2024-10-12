from sympy import factorint, prime
def A023578(n): return min((p for p in factorint(prime(n)+3) if p > 2), default=1) # _Chai Wah Wu_, Feb 03 2022
print([A023578(n) for n in range(1,31)])
