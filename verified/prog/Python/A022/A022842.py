from sympy import integer_nthroot
def A022842(n): return integer_nthroot(8*n**2,2)[0] # _Chai Wah Wu_, Mar 16 2021
print([A022842(n) for n in range(1,31)])
