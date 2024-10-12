from sympy import divisor_sigma
def A013959(n): return divisor_sigma(n,11) # _Chai Wah Wu_, Nov 17 2022
print([A013959(n) for n in range(1,31)])
