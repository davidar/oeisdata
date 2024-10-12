from sympy import integer_nthroot
def A001962(n): return 3*n+integer_nthroot(5*n**2,2)[0] # _Chai Wah Wu_, Mar 16 2021
print([A001962(n) for n in range(1,31)])
