from sympy import divisor_sigma
def A024816(n): return (n*(n+1)>>1)-divisor_sigma(n) # _Chai Wah Wu_, Apr 28 2023
print([A024816(n) for n in range(1,31)])
