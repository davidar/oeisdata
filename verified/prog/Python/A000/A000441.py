from sympy import divisor_sigma
def A000441(n): return (n*(1-6*n)*divisor_sigma(n)+5*n*divisor_sigma(n,3))//24 # _Chai Wah Wu_, Jul 25 2024
print([A000441(n) for n in range(1,31)])
