from sympy import divisor_sigma
def A001065(n): return divisor_sigma(n)-n # _Chai Wah Wu_, Nov 04 2022
print([A001065(n) for n in range(1,31)])
