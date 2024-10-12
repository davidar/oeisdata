from sympy import prime
def A001248(n): return prime(n)**2 # _Chai Wah Wu_, Aug 09 2024
print([A001248(n) for n in range(1,31)])
