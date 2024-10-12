from sympy import divisor_sigma
def A023887(n): return divisor_sigma(n,n) # _Chai Wah Wu_, Jun 19 2022
print([A023887(n) for n in range(1,31)])
