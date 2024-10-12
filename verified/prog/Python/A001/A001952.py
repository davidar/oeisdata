from sympy import integer_nthroot
def A001952(n): return 2*n+integer_nthroot(2*n**2,2)[0] # _Chai Wah Wu_, Mar 16 2021
print([A001952(n) for n in range(1,31)])
