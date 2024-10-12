from sympy import composite
def A018252(n): return 1 if n == 1 else composite(n-1) # _Chai Wah Wu_, Nov 15 2022
print([A018252(n) for n in range(1,31)])
