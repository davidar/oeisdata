from sympy import prime
def A001223(n): return prime(n+1)-prime(n) # _Chai Wah Wu_, Jul 07 2022
print([A001223(n) for n in range(1,31)])
